import requests
import json
import pickle

json_data = {
    'variables': {
        'id': '8483fc50-b82d-5ffa-5f92-6c72ac4bdaff',
    },
    'query': 'query ($id: String!) {\n  corporate(id: $id) {\n    id\n    name\n    description\n    logo_url\n    hq_city\n    hq_country\n    website_url\n    linkedin_url\n    twitter_url\n    startup_partners_count\n    startup_partners {\n      master_startup_id\n      company_name\n      logo_url: logo\n      city\n      website\n      country\n      theme_gd\n      __typename\n    }\n    startup_themes\n    startup_friendly_badge\n    __typename\n  }\n}\n',
}
with open('list_data_companies.pkl', 'rb') as file:
    my_list = pickle.load(file)

json_data = {
    'variables': {
        'id': '8483fc50-b82d-5ffa-5f92-6c72ac4bdaff',
    },
    'query': 'query ($id: String!) {\n  corporate(id: $id) {\n    id\n    name\n    description\n    logo_url\n    hq_city\n    hq_country\n    website_url\n    linkedin_url\n    twitter_url\n    startup_partners_count\n    startup_partners {\n      master_startup_id\n      company_name\n      logo_url: logo\n      city\n      website\n      country\n      theme_gd\n      __typename\n    }\n    startup_themes\n    startup_friendly_badge\n    __typename\n  }\n}\n',
}

name = []
description = []
logo_url = []
hq_city = []
hq_country = []
website_url = []
linkedin_url = []
twitter_url = []
startup_partners_count = []
startup_partners = []
startup_themes = []
categories = ['name', 'description', 'logo_url', 'hq_city', 'hq_country', 'website_url', 'linkedin_url', 'twitter_url', 'startup_partners_count', 'startup_partners']

for i in range(len(my_list)):
    json_data['variables']['id'] = my_list[i]
    response = requests.post('https://ranking.glassdollar.com/graphql', json=json_data)
    parsed_data = json.loads(response.text)
    name.append(parsed_data["data"]['corporate']['name'])
    description.append(parsed_data["data"]['corporate']['description'])
    logo_url.append(parsed_data["data"]['corporate']['logo_url'])
    hq_city.append(parsed_data["data"]['corporate']['hq_city'])
    hq_country.append(parsed_data["data"]['corporate']['hq_country'])
    website_url.append(parsed_data["data"]['corporate']['website_url'])
    linkedin_url.append(parsed_data["data"]['corporate']['linkedin_url'])
    twitter_url.append(parsed_data["data"]['corporate']['twitter_url'])
    startup_partners_count.append(parsed_data["data"]['corporate']['startup_partners_count'])
    startup_partners.append(parsed_data["data"]['corporate']['startup_partners'])

with open('startup_partners.json', 'w') as f:
    json.dump(startup_partners, f)
with open('startup_partners_count.json', 'w') as f:
    json.dump(startup_partners_count, f)
with open('twitter_url.json', 'w') as f:
    json.dump(twitter_url, f)
with open('linkedin_url.json', 'w') as f:
    json.dump(linkedin_url, f)
with open('hq_country.json', 'w') as f:
    json.dump(hq_country, f)
with open('hq_city.json', 'w') as f:
    json.dump(hq_city, f)
with open('logo_url.json', 'w') as f:
    json.dump(logo_url, f)
with open('description.json', 'w') as f:
    json.dump(description, f)
with open('name.json', 'w') as f:
    json.dump(name, f)

