import pandas as pd
from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired 



train=pd.read_csv('Clean_Dataset.csv')

class InputForm(FlaskForm):
    airline=SelectField(
        label="Airline",
        choices=train.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    source_city=SelectField(
        label="Source_city",
        choices=train.source_city.unique().tolist(),
        validators=[DataRequired()]
    )
    departure_time=SelectField(
        label="Departure_time",
        choices=train.departure_time.unique().tolist(),
        validators=[DataRequired()]
    )
    stops=SelectField(
        label="Stops",
        choices=train.stops.unique().tolist(),
        validators=[DataRequired()]
    )
    arrival_time=SelectField(
        label="Arrival_time",
        choices=train.arrival_time.unique().tolist(),
        validators=[DataRequired()]
    )
    destination_city=SelectField(
        label="Destination_city",
        choices=train.destination_city.unique().tolist(),
        validators=[DataRequired()]
    )
    Class=SelectField(
        label="Class",
        choices=train.Class.unique().tolist(),
        validators=[DataRequired()]
    )
    duration=IntegerField(
        label="Duration_in_hours",
        validators=[DataRequired()]
    )
    days_left=IntegerField(
        label="Day_left",
        validators=[DataRequired()]
    )
    submit=SubmitField("Predict")
    
    
    