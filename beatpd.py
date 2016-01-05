import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

app = Flask(__name__)
app.config.from_envvar('BEATPD_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()