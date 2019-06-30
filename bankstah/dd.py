import json
import requests
import config

api_url_base = 'https://api.discorddungeons.me/v3/'
headers = {'accept': 'application/json', 'Authorization': '{0}'.format(config.dd_key)}

def get_user(userid):
    api_url = '{0}user/'.format(api_url_base)+userid

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_guild(guildid):
    api_url = '{0}guild/'.format(api_url_base)+guildid

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
