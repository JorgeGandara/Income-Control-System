import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.objeto import objeto


class ObjetoController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage4.json')

    def add(self, objeto: objeto = objeto()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['objetos'].append(objeto.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return objeto.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object