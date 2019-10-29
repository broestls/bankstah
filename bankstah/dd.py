import json
import requests
import config

api_url_base = 'https://api.discorddungeons.me/v3/'
headers = {'accept': 'application/json', 'Authorization': '{0}'.format(config.dd_key)}

def get_user(user_id):
    api_url = '{0}user/'.format(api_url_base)+user_id
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_guild(guild_id):
    api_url = '{0}guild/'.format(api_url_base)+guild_id
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_all_items():
    api_url = '{0}all/items'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_item_by_id(item_id):
    api_url = '{0}item/'.format(api_url_base)+str(item_id)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def generate_item_table():
    item_hash = {}
    for i in get_all_items()['data']:
        item_hash.update({i['name']:i['id'], i['plural']:i['id']})
    return item_hash
