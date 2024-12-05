from utils.db import db

class Country(db.Model):

    # Defining the columns for the table
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(255), nullable=False)
    literacy_rate = db.Column(db.String(255), nullable=False)
    enrollment_rate = db.Column(db.Integer, nullable=False)
    primary_education = db.Column(db.Integer, nullable=False)
    secondary_education = db.Column(db.Integer, nullable=False)