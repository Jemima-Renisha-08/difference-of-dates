from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_date_difference(date1, date2):
    # Convert the strings to datetime objects
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Calculate the difference between the two dates
    delta = abs((d2 - d1).days)
    
    return delta

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the two dates from the form
        date1 = request.form['date1']
        date2 = request.form['date2']
        
        # Calculate the difference
        difference = calculate_date_difference(date1, date2)
        
        return render_template('index.html', difference=difference)
    
    return render_template('index.html', difference=None)

if __name__ == '__main__':
    app.run(debug=True)
