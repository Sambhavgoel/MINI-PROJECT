from flask import Flask, render_template, request
import pickle
import pandas as pd
# from tensorflow.keras.models import load_model

app = Flask(__name__)


model= pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():

    # date_dep = request.form["Dep_Time"]
    # day = int(pd.to_datetime(date_dep, format="%d-%m-%Y").day)
    # month = int(pd.to_datetime(date_dep, format ="%d-%m-%Y").month)
    # year = int(pd.to_datetime(date_dep, format ="%d-%m-%Y").year)
    
    MinTemp=float(request.form['MinTemp'])
    MaxTemp=float(request.form['MaxTemp'])
    Rainfall=float(request.form['Rainfall'])
    Evaporation=float(request.form['Sunshine'])
    WindGustSpeed=float(request.form['WindGustSpeed'])
    WindSpeed9am=float(request.form['WindSpeed9am'])
    WindSpeed3pm=float(request.form['WindSpeed3pm'])
    Sunshine=float(request.form['Sunshine'])
    Humidity9am=float(request.form['Humidity9am'])
    Humidity3pm=float(request.form['Humidity3pm'])
    Pressure9am=float(request.form['Pressure9am'])
    Pressure3pm=float(request.form['Pressure3pm'])

    Cloud9am=float(request.form['Cloud9am'])
    Cloud3pm=float(request.form['Cloud3pm'])
    Temp9am=float(request.form['Temp9am'])
    Temp3pm=float(request.form['Temp3pm'])
    RainToday=float(request.form['RainToday'])
    # RainTomorrow=float(request.form['RainTomorrow'])
    WindSpeed9am=float(request.form['WindSpeed9am'])
    WindSpeed3pm=float(request.form['WindSpeed3pm'])
    location_Albany=0
    location_Albury=0
    location_AliceSprings=0
    location_BadgerysCreek=0
    location_Ballarat=0 
    location_Bendigo=0
    location_Brisbane=0 
    location_Cairns=0 
    location_Canberra=0
    location_Cobar=0 
    location_CoffsHarbour=0 
    location_Dartmoor=0
    location_Darwin=0 
    location_GoldCoast=0 
    location_Hobart=0
    location_Katherine=0 
    location_Launceston=0 
    location_Melbourne=0
    location_MelbourneAirport=0 
    location_Mildura=0 
    location_Moree=0
    location_MountGambier=1 
    location_MountGinini=0 
    location_Newcastle=0
    location_Nhil=0
    location_NorahHead=0
    location_NorfolkIsland=0
    location_Nuriootpa=0 
    location_PearceRAAF=0 
    location_Penrith=0
    location_Perth=0 
    location_PerthAirport=0 
    location_Portland=0
    location_Richmond=0 
    location_Sale=0 
    location_SalmonGums=0
    location_Sydney=0
    location_SydneyAirport=0 
    location_Townsville=0
    location_Tuggeranong=0 
    location_Uluru=0 
    location_WaggaWagga=0
    location_Walpole=0 
    location_Watsonia=0 
    location_Williamtown=0
    location_Witchcliffe=0 
    location_Wollongong=0 
    location_Woomera=0

    Source1 = request.form["Source"]


    if (Source1 == 'MountGambier'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=0
        location_Ballarat=0 
        location_Bendigo=0
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=1 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0
    elif (Source1 == 'Wollongong'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=0
        location_Ballarat=0 
        location_Bendigo=0
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=1 
        location_Woomera=0


    elif (Source1 == 'AliceSprings'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=1
        location_BadgerysCreek=0
        location_Ballarat=0 
        location_Bendigo=0
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0
    elif (Source1 == 'BadgerysCreek'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=1
        location_Ballarat=0 
        location_Bendigo=0
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0

    elif (Source1 == 'Ballarat'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=0
        location_Ballarat=1
        location_Bendigo=0
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0
    elif (Source1 == 'Bendigo'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=0
        location_Ballarat=0
        location_Bendigo=1
        location_Brisbane=0 
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0
    elif (Source1 == 'Brisbane'):
        location_Albany=0
        location_Albury=0
        location_AliceSprings=0
        location_BadgerysCreek=0
        location_Ballarat=0
        location_Bendigo=0
        location_Brisbane=1
        location_Cairns=0 
        location_Canberra=0
        location_Cobar=0 
        location_CoffsHarbour=0 
        location_Dartmoor=0
        location_Darwin=0 
        location_GoldCoast=0 
        location_Hobart=0
        location_Katherine=0 
        location_Launceston=0 
        location_Melbourne=0
        location_MelbourneAirport=0 
        location_Mildura=0 
        location_Moree=0
        location_MountGambier=0 
        location_MountGinini=0 
        location_Newcastle=0
        location_Nhil=0
        location_NorahHead=0
        location_NorfolkIsland=0
        location_Nuriootpa=0 
        location_PearceRAAF=0 
        location_Penrith=0
        location_Perth=0 
        location_PerthAirport=0 
        location_Portland=0
        location_Richmond=0 
        location_Sale=0 
        location_SalmonGums=0
        location_Sydney=0
        location_SydneyAirport=0 
        location_Townsville=0
        location_Tuggeranong=0 
        location_Uluru=0 
        location_WaggaWagga=0
        location_Walpole=0 
        location_Watsonia=0 
        location_Williamtown=0
        location_Witchcliffe=0 
        location_Wollongong=0 
        location_Woomera=0


    day = 25
    month = 4
    year = 2010




    result=model.predict([[MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine,
       WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am,
       Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm,
       Temp9am, Temp3pm, RainToday,location_Albany, location_Albury, location_AliceSprings,
       location_BadgerysCreek, location_Ballarat, location_Bendigo,
       location_Brisbane, location_Cairns, location_Canberra,
       location_Cobar, location_CoffsHarbour, location_Dartmoor,
       location_Darwin, location_GoldCoast, location_Hobart,
       location_Katherine, location_Launceston, location_Melbourne,
       location_MelbourneAirport, location_Mildura, location_Moree,
       location_MountGambier, location_MountGinini, location_Newcastle,
       location_Nhil, location_NorahHead, location_NorfolkIsland,
       location_Nuriootpa, location_PearceRAAF, location_Penrith,
       location_Perth, location_PerthAirport, location_Portland,
       location_Richmond, location_Sale, location_SalmonGums,
       location_Sydney, location_SydneyAirport, location_Townsville,
       location_Tuggeranong, location_Uluru, location_WaggaWagga,
       location_Walpole, location_Watsonia, location_Williamtown,
       location_Witchcliffe, location_Wollongong, location_Woomera,day,month,year]])# Replace with your actual prediction result
    return render_template('index.html',**locals())
        # return render_template('result.html', result=result)

        # return render_template('result.html', result=result)


  

if __name__ == '__main__':
    app.run(debug=True)
