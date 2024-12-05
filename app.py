from flask import Flask, render_template, request, redirect, jsonify

from utils.db import db

from models.country import *




app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/country')
def country():
    return render_template('country.html')

@app.route('/country_specific_data')
def country_specific_data():
    country = (Country.query.all())
    return render_template('country_specific_data.html', content=country)

@app.route('/dataoverview')
def dataoverview():
    return render_template('dataoverview.html')

@app.route('/trends')
def trends():
    return render_template('trends.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    country_id = form_data.get('country_id')
    country_name = form_data.get('country_name')
    literacy_rate = form_data.get('literacy_rate')
    enrollment_rate = form_data.get('enrollment_rate')
    primary_education = form_data.get('primary_education')
    secondary_education = form_data.get('secondary_education')

    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        country = Country(country_id=country_id, country_name=country_name, literacy_rate=literacy_rate, enrollment_rate=enrollment_rate, primary_education=primary_education,secondary_education=secondary_education)
        db.session.add(country)
        db.session.commit()
    print("sumitted successfully")
    return redirect('/')



@app.route('/delete/<int:country_id>', methods=['GET', 'DELETE'])
def delete(country_id):
    country = Country.query.get(country_id)
    print("task: {}".format(country_id))

    if not country:
        return jsonify({'message': 'country not found'}), 404
    try:
        db.session.delete(country)
        db.session.commit()
        return jsonify({'message': 'country deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the data {}'.format(e)}), 500


@app.route('/update/<int:country_id>', methods=['GET', 'POST'])
def update(country_id):
    country = Country.query.get_or_404(country_id)
    print(country.country_id)
    if not country:
        return jsonify({'message': 'country not found'}), 404

    if request.method == 'POST':
        country.country_id = request.form['country_id']
        country.country_name = request.form['country_name']
        country.literacy_rate = request.form['literacy_rate']
        country.enrollment_rate = request.form['enrollment_rate']
        country.primary_education = request.form['primary_education']
        country.secondary_education = request.form['secondary_education']

        try:
            db.session.commit()
            return redirect('/country_specific_data')

        except Exception as e:
            db.session.rollback()
            return "there is an issue while updating the record"
    return render_template('update.html', country=country)


if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5003,debug=True)

