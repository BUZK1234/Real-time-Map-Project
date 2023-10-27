from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

data = []  # Store the CSV data

def read_csv_data():
    global data
    with open('/home/bilal-zaman/Self_Learning/project/night_activity_1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [{'lat': float(row['Latitude']), 'lon': float(row['Longitude'])} for row in reader]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    read_csv_data()  # Read the data from the CSV file once
    app.run(debug=True, port=8080)

