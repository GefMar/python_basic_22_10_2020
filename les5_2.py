import requests
import json

#
# url = 'https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png'
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"
# }
#
# response = requests.get(url, headers=header)
#
# with open('gb_image.png', 'wb') as file:
#     file.write(response.content)


user = {
    'name': 'USERNAME',
    'STAGE': 'LEVEL1',
    'NEW': 'ПРИВЕТ МИР',
    'Money': 1,
    'box': [1, 2, 3, 4, 5, 6],
    'is_admin': False,
    'box2': (1, 2, 3, 4, 5),
}


with open('gb.json', 'w') as file:
    json.dump(user, file, ensure_ascii=False)
    # print(json.load(file))


# data = json.dumps(user)
# print(type(data))
# print(data)

# j_data = '{"name": "USERNAME", "STAGE": "LEVEL1", "Money": 1, "box": [1, 2, 3, 4, 5, 6], "is_admin": false, "box2": [1, 2, 3, 4, 5]}'
#
# n_data = json.loads(j_data)
# print(type(n_data))
# print(n_data)
