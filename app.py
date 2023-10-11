import json
from flask import Flask, redirect, url_for, render_template
from blueprint_query.route import blueprint_query

app = Flask(__name__)
with open('DB/db_config.json') as f:
    app.config['db_config'] = json.load(f)

app.register_blueprint(blueprint_query, url_prefix='/query')

@app.route('/')
def main_menu():
    return render_template('main_menu.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
