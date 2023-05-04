import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.event import event


class eventController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'eventStorage.json')

    def add(self, event: event = event()) -> str:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['events'].append(event.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return event.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r', encoding='utf-8') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object