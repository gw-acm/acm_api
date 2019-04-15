from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/acm-events-images')
def gdrive():
    apiKey = config['google-drive']['api-key']
    folderId = config['google-drive']['folder-id']
    driveURL = "https://www.googleapis.com/drive/v3/files?q='{}'+in+parents&key={}".format(folderId, apiKey)
    return requests.get(driveURL).text

def loadconfig():
    with open('./config.json', 'r+') as configFile:
        config = configFile.read()
        return json.loads(config)

if __name__ == '__main__':
    config = loadconfig()
    app.run('0.0.0.0', 8080)
