from base import Session
# Functions for use during the item hunt for the luck potion

def ingest_brew(message_text):
    #shin stopped the brew they started 10 seconds using a Rock, a Log and a Lemon.
    result = message_text.lower().split('\n')[1].split("They got a ",1)[1].replace('.','')
    brew = message_text.lower().split('\n')[0].replace(' and ', ' ').replace('.','')
    user = brew.split(' ')[0]
    time = brew.split(' ')[6]
    ingredients = {}
for x in brew.split("using ",1)[1].replace(", ",",").split(','):
    item = x.split(' ')
    quantity = 1 if item[0] == "a" else item[0]
    ingredients.update({item[1]:quantity})

    print(ingredients)
    recipe_string = ''
    for key, value in sorted(ingredients):
        recipe_string = key + " " + value + " "

    exists = session.query(Brew).filter(Brew.recipe == recipe_string)

    if exists is None:
        def __init__(self, recipe, is_tested, duration):
        new_recipe = Brew(recipe=recipe_string, is_tested=True, duration=time, user=user)
        session.add(new_recipe)
        print("added a new recipe to the db!")

    return recipe_string + ": " + result
