import streamlit as st
import pickle
import numpy as np
#from sklearn.preprocessing import StandardScaler
st.title("Welcome to Car Price Predictor")
st.header("Please fill in your details")
#scaler = StandardScaler()
car_name = st.text_input("Enter your car name: ")
car_brand = st.text_input("Enter your car brand: ")
vehicle_age = st.slider("Select the age of you vehicle[Years]",0,20,3)
engine = st.number_input("Enter the engine for your vehile: ",1197)
max_power = st.slider("Select the maximum power",0,200,1)
mileage = st.number_input("Enter the mileage of the vehicle: ",0,100,22)
transmission=["Auto","Manual"]
transmission_type = st.selectbox("Select the transmission type",transmission)
fuel_type = st.radio("choose your fuel tye",options = ["Petrol","Diesel"])
models = ["Audi","BMW","Maluti"]
car_model = st.selectbox("Choose an option", models)
if transmission_type == "Manual":
    transmission_manual = True
else:
    transmission_manual = False
if fuel_type =="Petrol":
    fuel_type_Diesel = False
    Fuel_type_petrol =True
else:
    fuel_type_Diesel = True
    Fuel_type_petrol =False

predict_clicked = st.button("Predict")
Reset_options = st.button("Reset")

if predict_clicked==True:
    model=pickle.load(open("rfr.pkl", 'rb'))

    #load the test data into numpy array
    data=[np.array([vehicle_age,mileage,engine,max_power,transmission_manual,fuel_type_Diesel,Fuel_type_petrol])]
    
    #call the model to predict the price
    result=model.predict(data)
    st.write("The price for the selected vehicle is: ",result)
elif Reset_options ==True:
    st.session_state.clear

