# Simple web application using Flask framework
#   - Use of Env Variables to configure
from flask import Flask
import os # (1) library for operating system calls

PORT = os.getenv('PORT', 8080) # (2) get env

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT) # (3) pass port as an arg
