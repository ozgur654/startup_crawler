import requests
import json
import pickle
json_data = {
    'operationName': 'GIMGetSearchResults',
    'variables': {
        'where': {
            'query': 'si',
        },
    },
    'query': 'query GIMGetSearchResults($where: searchBarWhere) {\n  searchBar(where: $where)\n}\n',
}

response = requests.post('https://ranking.glassdollar.com/graphql', json=json_data)

alphabet = list(map(chr, range(97, 123)))
alphabet.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' '])
company_ids = set()
count = 0

for i in range(len(alphabet)):
  for j in range(len(alphabet)):
    word = alphabet[i] + alphabet[j]
    json_data['variables']["where"]['query'] = word
    response = requests.post('https://ranking.glassdollar.com/graphql', json=json_data)
    parsed_data = json.loads(response.text)

    if parsed_data["data"]["searchBar"]:
      ids = [corporate["id"] for corporate in parsed_data["data"]["searchBar"]["corporates"]]


    # Print the ids
      for id in ids:
        if id not in company_ids:
          company_ids.add(id)
          count += 1
      if len(ids) == 5:
          for k in range(len(alphabet)):
              word = alphabet[i] + alphabet[j] + alphabet[k]
              json_data['variables']["where"]['query'] = word
              response = requests.post('https://ranking.glassdollar.com/graphql', json=json_data)
              parsed_data = json.loads(response.text)

              if parsed_data["data"]["searchBar"]:
                  ids = [corporate["id"] for corporate in parsed_data["data"]["searchBar"]["corporates"]]

              # Print the ids
                  for id in ids:
                      if id not in company_ids:
                          company_ids.add(id)
                          count += 1
      print(count, word)


for i in range(len(alphabet)):
  for j in range(len(alphabet)):
    word = "the " + alphabet[i] + alphabet[j]
    json_data['variables']["where"]['query'] = word
    response = requests.post('https://ranking.glassdollar.com/graphql', json=json_data)
    parsed_data = json.loads(response.text)

    if parsed_data["data"]["searchBar"]:
      ids = [corporate["id"] for corporate in parsed_data["data"]["searchBar"]["corporates"]]

    # Print the ids
      for id in ids:
        if id not in company_ids:
          company_ids.add(id)
          count += 1
      print(count, word)

with open('list_data.pkl', 'wb') as file:
    pickle.dump(list(company_ids), file)