import requests

FOLDER_NAME = 'Unit'
TOKEN = '-'


def folder_creation():

    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            headers={'Authorization': TOKEN}, params={'path': FOLDER_NAME})

    code = response.status_code
    print(code)



print(folder_creation())