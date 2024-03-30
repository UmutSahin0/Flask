from flask import Flask
import pandas as pd

app = Flask(__name__)

# Örnek bir veri dosyası yolu
DATA_FILE_PATH = 'data.xlsx'

def read_data(file_path):
    data = pd.read_excel(file_path)
    return data

# data.xlsx dosyasını oku
data = read_data(DATA_FILE_PATH)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/name/<name>')
def print_name_with_name(name):
    return 'Hi, {}'.format(name)

@app.route('/id/<id>')
def find_name_with_id(id):
    # Veri dosyasından gelen veriyi kullanarak istenen işlemi yap
    filtered_data = data[data['id'] == int(id)]
    if not filtered_data.empty:
        return 'Name : {}'.format( filtered_data['ad'].iloc[0])
    else:
        return 'Name not found!'

if __name__ == '__main__':
    app.run()