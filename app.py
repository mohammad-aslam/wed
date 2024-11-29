from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/country')
def country():
    return render_template('country.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dataoverview')
def dataoverview():
    return render_template('dataoverview.html')

@app.route('/trends')
def trends():
    return render_template('trends.html')
if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5002,debug=True)