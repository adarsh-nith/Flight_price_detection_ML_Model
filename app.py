from flask import (Flask,url_for,render_template)
from forms import InputForm
import pandas as pd
import joblib


app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

model=joblib.load('model3.joblib')
@app.route("/")
def home():
    return render_template("home.html",title="Home")


@app.route("/predict",methods=["GET","POST"])
def predict():
    form=InputForm()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(airline=[form.airline.data],
                                source_city=[form.source_city.data],
                                departure_time=[form.departure_time.data],
                                stops=[form.stops.data],
                                arrival_time=[form.arrival_time.data],
                                destination_city=[form.destination_city.data],
                                Class=[form.Class.data],
                                duration=[form.duration.data],
                                days_left=[form.days_left.data]
        ))

                                
        prediction=model.predict(x_new)[0]
        message=f"The predicted price of flight is {prediction:,.0f} INR"
        
    else:
        message="Please provide valid input"    
                                
    return render_template("predict.html",title="Predict",form=form,output=message)

if __name__=="__main__":
    app.run(debug=True)
    
