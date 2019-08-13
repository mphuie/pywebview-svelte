import os
import webview
import json
from pathlib import Path
from jinja2 import Template
import json

USER_HOME = str(Path.home())
CONFIG_FILE = '.pywebview-svelte'
config_file_absolute_path = os.path.join(USER_HOME, CONFIG_FILE)

class Api():
    def hello(self, param):
        print(param)
        print('world!')
        return(['Hello!', 'from Python'])

    def get_config(self, param):
        
        config_file_absolute_path = os.path.join(USER_HOME, CONFIG_FILE)
        print(config_file_absolute_path)
        if not os.path.exists(config_file_absolute_path):
            with open(config_file_absolute_path, 'w') as fh:
                fh.write('{}')
            return {}
        with open(config_file_absolute_path) as fh:
            return json.load(fh)
    
    def save_config(self, config):
        with open(config_file_absolute_path, 'w') as fh:
            fh.write(config)


    # def addItem(self, title):
    #     print('Added item %s' % title)

    # def removeItem(self, item):
    #     print('Removed item %s' % item)

    # def editItem(self, item):
    #     print('Edited item %s' % item)

    # def toggleItem(self, item):
    #     print('Toggled item %s' % item)

if __name__ == '__main__':

    initial_variables = { "hi": "there"}

    with open('public/index.jinja2') as fh:
        template = Template(fh.read())

    with open('public/index.html', 'w') as fh:
        fh.write(template.render(initial_variables=initial_variables))


    api = Api()
    webview.create_window('Sample', 'public/index.html', js_api=api, min_size=(600, 450), text_select=True)
    webview.start(debug=True)