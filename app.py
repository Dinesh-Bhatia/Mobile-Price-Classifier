# -*- coding: utf-8 -*-
"""

@author: Dinesh
"""
import streamlit as st 
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)
model = pickle.load(open('/content/drive/My Drive/mobilelinearregression.pkl','rb'))
run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    Battery_Power= float(request.args.get('Battery_Power'))
    Blue= float(request.args.get('Blue'))
    clock_speed= float(request.args.get('clock_speed'))
    dual_sim= float(request.args.get('dual_sim'))
    fc= float(request.args.get('fc'))

    four_g= float(request.args.get('four_g'))
    int_memory= float(request.args.get('int_memory'))
    m_dep= float(request.args.get('m_dep'))
    mobile_wt= float(request.args.get('mobile_wt'))
    n_cores= float(request.args.get('n_cores'))

    pc= float(request.args.get('pc'))
    px_height= float(request.args.get('px_height'))
    px_width= float(request.args.get('px_width'))
    ram= float(request.args.get('ram'))
    sc_h= float(request.args.get('sc_h'))

    sc_w= float(request.args.get('sc_w'))
    talk_time= float(request.args.get('talk_time'))
    three_g= float(request.args.get('three_g'))
    touch_screen= float(request.args.get('touch_screen'))
    wifi= float(request.args.get('wifi'))	
    
    prediction =int(model.predict([[Battery_Power, Blue, clock_speed, dual_sim, fc, four_g, int_memory,m_dep,mobile_wt,n_cores,pc, px_height,px_width,ram, sc_h, sc_w, talk_time,three_g , touch_screen, wifi ]]))
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given internal memory is Rs.  : {}'.format(prediction))



if __name__ == "__main__":
    app.run(debug=True)
