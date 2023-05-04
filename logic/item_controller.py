import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.item import item


class itemController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'itemStorage.json')

    def add(self, item: item = item()) -> str:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['Items'].append(item.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return item.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r', encoding='utf-8') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object