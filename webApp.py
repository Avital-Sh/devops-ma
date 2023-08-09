import os
import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route('/uselessfact')
def uselessfact():
    url = os.environ.get('URL_TO_CONSUME')
    if url:
        response = requests.get(url)
        return Response(response.text)
    else:
        return "URL not specified in environment variable."

@app.route('/funnyfact')
def funnyfact():
    url = os.environ.get('URL_TO_CONSUME')
    if url:
        response = requests.get(url)
        return Response(response.text)
    else:
        return "URL not specified in environment variable."

@app.route('/ready')
def ready():
    url = os.environ.get('URL_TO_CONSUME')
    return '', 200


if __name__ == '__main__':
    app.run()
