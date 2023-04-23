import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.evento import evento


class EventoController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage2.json')

    def add(self, evento: evento = evento()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['eventos'].append(evento.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return evento.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object