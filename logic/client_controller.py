import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0} data {0}'.format(os.sep)
from logic.client import client


class clientController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'clientStorage.json')

    def add(self, client: client = client()) -> str:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['clients'].append(client.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return client.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r', encoding='utf-8') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object