import requests
import json

class Boats:
    def __init__(self, token):
        self.token = token
        self.base = "https://discord.boats/api/v2"

    def get_bot(self, botid):
        r = requests.get(f"{self.base}/bot/{botid}")
        return r.json()

    def get_voted(self, botid, userid):
        r = requests.get(f"{self.base}/bot/{botid}/voted?id={userid}")        
        return r.json()["voted"]

    def get_user(self, userid):
        r = requests.get(f"{self.base}/user/{userid}")
        return r.json()

    def post_stats(self, servercount, botid):
        data = {"server_count": servercount}
        headers = {
                "content-type": "APPLICATION/JSON",
                "Authorization": self.token
                }
        r = requests.post(f"{self.base}/bot/{botid}", data=json.dumps(data), headers=headers)
        return r.status_code

