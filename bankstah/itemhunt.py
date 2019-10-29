from base import Session
from models import Brew
from dd import generate_item_table,get_item_by_id
# Functions for use during the item hunt for the luck potion

item_hash = generate_item_table()

def ingest_brew(message_text):
    session = Session()
    #shin stopped the brew they started 10 seconds using a Rock, a Log and a Lemon.
    #shin stopped the brew they started 3 seconds using a Rock, a Log and a Lemon.\nThey got a Sludge Vial.
    result = message_text.lower().split('\n')[1].split("they got a ",1)[1].replace('.','')
    brew = message_text.lower().split('\n')[0].replace(' and ',', ').replace('.','').split("using ",1)[1]
    user = message_text.split(' ')[0]
    time = message_text.split(' ')[6] if 'minute' in brew.split(' ')[7] else 0
    ingredients = {}
    # Need to figure out what to do with prefixes and how to handle multi-space ones
    for x in brew.split("using ",1)[1].replace(", ",",").split(','):
        item = x.split(' ')
        quantity = 1 if item[0] == "a" else item[0]
        ingredients.update({item[1]:quantity})

    recipe_string = ''
    return_text = ''
    for key, value in sorted(ingredients.items()):
        recipe_string = recipe_string + key + " " + str(value) + " "

    recipe_string = recipe_string.rstrip()
    q = session.query(Brew).filter_by(recipe = recipe_string).filter_by(duration = time)

    if session.query(q.exists()).scalar() is False:
        new_recipe = Brew(recipe=recipe_string, result=result, is_tested=True, duration=time, user=user)
        session.add(new_recipe)
        session.commit()
        session.close()
        return_text = "Today " + user + " showed me that putting " + recipe_string + \
        " in a jar for " + time + "minutes gives you a " + result + "!"
    else:
        return_text = "I already learned that recipe!"


    return return_text
