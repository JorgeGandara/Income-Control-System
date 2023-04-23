import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.cliente import cliente


class ClienteController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage3.json')

    def add(self, cliente: cliente = cliente()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['clientes'].append(cliente.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return cliente.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object