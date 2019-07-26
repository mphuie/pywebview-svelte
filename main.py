import os
import webview

class Api():
    def hello(self, param):
        print(param)
        print('world!')
        return(['Hello!', 'from Python'])


    # def addItem(self, title):
    #     print('Added item %s' % title)

    # def removeItem(self, item):
    #     print('Removed item %s' % item)

    # def editItem(self, item):
    #     print('Edited item %s' % item)

    # def toggleItem(self, item):
    #     print('Toggled item %s' % item)

if __name__ == '__main__':
    api = Api()
    webview.create_window('Todos magnificos', 'public/index.html', js_api=api, min_size=(600, 450), text_select=True, frameless=True)
    webview.start(debug=True)