import streamlit as st
import pandas as pd
import numpy as np

pipe = pd.read_pickle("pipe.pkl")
df = pd.read_pickle("df.pkl")

st.title("Laptop Price Predictor")


#brand
company = st.selectbox('Brand',df['Company'].unique())

#type of laptop
type = st.selectbox('Type',df['TypeName'].unique())

#RAM
ram = st.selectbox('RAM-GB',[2,4,6,8,12,16,24,32,64])

#Weight
weight = st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen = st.selectbox('TouchScreen',['No','Yes'])

#IPS
ips = st.selectbox('IPS',['No','Yes'])

#ScreenSize
screen_size = st.number_input('Screen Size')

# Resolution
resolutioin = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#CPU
cpu = st.selectbox('CPU',df['cpu_brand'].unique())

hdd = st.selectbox('HDD(GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(GB)',[0,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

os = st.selectbox('Operating System',df['os'].unique())

if st.button('Predict Price'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else :
        touchscreen = 0

    if ips == 'yes':
        ips = 1
    else :
        ips = 0

    x_res = int(resolutioin.split('x')[0])
    y_res = int(resolutioin.split('x')[1])

    ppi = (((x_res**2) + (y_res**2))**0.5/screen_size)

    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.header("The predicted price for this configuration is : ")
    st.title("₹" +str(round(int(np.exp(pipe.predict(query)[0])))) + "/-")


















