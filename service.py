from flask import Flask,request
import pandas as pd

app = Flask(__name__)

DATA_FILE_PATH = 'data.xlsx'


def read_data(file_path):
    data = pd.read_excel(file_path)
    return data


data = read_data(DATA_FILE_PATH)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/name/<name>')
def print_name_with_name(name):
    return 'Hi, {}'.format(name)


@app.route('/id/<id>', methods=['GET'])
def find_name_with_id(id):
    if request.method == 'GET':
        filtered_data = data[data['id'] == int(id)]
        if not filtered_data.empty:
            return 'Name : {}'.format(filtered_data['ad'].iloc[0])
        else:
            return 'Name not found!'


if __name__ == '__main__':
    app.run()
