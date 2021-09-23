import requests


def pythonlambda():
    response = requests.get("https://dy9zfzh264.execute-api.eu-central-1.amazonaws.com/test2/")
    print(response.text)
    print(response.json())
    print(response.headers['content-type'])

