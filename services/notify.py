import requests

class Notify:

    def __init__(self):
        self.url = 'https://webhook.site'

    def send_event(self, data):
        response = requests.post(
            url=f'{self.url}/e16ed808-10d8-48bf-865d-c30eee9a4cfa',
            json=data
        )
        return response.text
