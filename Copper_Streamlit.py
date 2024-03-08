# import
import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu

#___________________________________________________________________________

# Functions to predict ststus
def predict_status(type,quatity, customer, country, application, thickness, width, product_ref, SP):


    # model file of the classification
    with open("Classification_Model.pkl", "rb") as m1:
        status_check = pickle.load(m1)

    user_data = np.array([[type,quatity, customer, country, application, thickness, width, product_ref, SP]])
    
    y_pred = status_check.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0
#___________________________________________________________________________
    
def predict_selling_price(status,type,quatity, customer, country, application, thickness, width, product_ref):

    #model file of the classification
    with open("Regression_Model.pkl","rb") as m2:
        price_checker = pickle.load(m2)

    user_data = np.array([[status,type,quatity, customer, country, application, thickness, width, product_ref]])
    
    y_pred= price_checker.predict(user_data)

    y_pred_exp = np.exp(y_pred[0])

    return y_pred_exp
    

#___________________________________________________________________________

st.set_page_config(layout = "wide")

st.markdown("<h1 style='text-align: center; color: #af4424;'>INDUSTRIAL COPPER MODELING</h1>", unsafe_allow_html=True)


option = option_menu(None, ["PREDICT - STATUS", "PREDICT - SELLING PRICE"], 
                     icons=["highlighter","currency-dollar"], 
                     orientation="horizontal",
                     styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "#af4424", "font-size": "20px"},
                               "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "#6495ED"}})

if option == "PREDICT - STATUS":

    st.header("PREDICT STATUS (Win / Lose)")
    st.write("")
    col1,col2,col3 = st.columns([5,1,5])
    with col1:
        item_type = st.number_input(min_value=0,max_value=6,value="min", 
                                    label="Enter the Value for ITEM TYPE / Min:0, Max:6")
        quantity_tons_log = st.number_input(min_value=-11.51,max_value=20.72,value="min",
                                            label="Enter the Value for QUANTITY TONS (Log Value) / Min:-11.51, Max:20.72",format="%0.4f")
        customer_log = st.number_input(min_value=17.219,max_value=17.230,value="min",
                                       label="Enter the Value for CUSTOMER (Log Value) / Min:17.219, Max:17.230",format="%0.4f")
        country = st.number_input(min_value=3.218,max_value=4.727,value="min",
                                  label="Enter the Value for COUNTRY (Log Value) / Min:3.218, Max:4.727",format="%0.4f")
        application = st.number_input(min_value=0.693,max_value=4.595,value="min",
                                      label="Enter the Value for APPLICATION (Log Value) / Min:0.693, Max:4.595",format="%0.4f")
        
    with col3:  
        thickness_log = st.number_input(min_value=-1.714,max_value=7.824,value="min",
                                        label="Enter the Value for THICKNESS (Log Value) / Min:-1.714, Max:7.824",format="%0.4f")
        width = st.number_input(min_value=6.713,max_value=7.673,value="min",
                                label="Enter the Value for WIDTH (Log Value) / Min:6.713, Max:7.673",format="%0.4f")
        product_ref = st.number_input(min_value=13.324,max_value=21.266,value="min",
                                      label="Enter the Value for PRODUCT REF (Log Value) / Min:13.324, Max:21.266",format="%0.4f")
        selling_price_log = st.number_input(min_value=5.975,max_value=7.390,value="min",
                                            label="Enter the Value for SELLING PRICE (Log Value) / Min:5.975, Max:7.390",format="%0.4f")

    predict = st.button(":violet[***PREDICT THE STATUS***]",use_container_width=True)

    if predict:
        status= predict_status(item_type,quantity_tons_log, customer_log,country,application,thickness_log,width,product_ref,selling_price_log)
        
        if status == 1:
            st.write("## :green[The Status is WIN! 😎]")

        else:
            st.write("## :red[The Status is LOSE 😥]")

#_______________________________________________________________________________________________________
if option == "PREDICT - SELLING PRICE":

    st.header("PREDICT SELLING PRICE")
    st.write(" ")

    col1,col2,col3 = st.columns([5,1,5])

    with col1:
        status = st.number_input(min_value=0,max_value=8,value="min", 
                                    label="Enter the Value for STATUS / Min:0, Max:8")
        item_type = st.number_input(min_value=0,max_value=6,value="min", 
                                    label="Enter the Value for ITEM TYPE / Min:0.0, Max:6.0",format="%i")
        quantity_tons_log = st.number_input(min_value=-11.51,max_value=20.72,value="min",
                                            label="Enter the Value for QUANTITY TONS (Log Value) / Min:-11.51, Max:20.72",format="%0.4f")
        customer_log = st.number_input(min_value=17.219,max_value=17.230,value="min",
                                       label="Enter the Value for CUSTOMER (Log Value) / Min:17.219, Max:17.230",format="%0.4f")
        country = st.number_input(min_value=3.218,max_value=4.727,value="min",
                                  label="Enter the Value for COUNTRY (Log Value) / Min:3.218, Max:4.727",format="%0.4f")

    with col3:
        application = st.number_input(min_value=0.693,max_value=4.595,value="min",
                                      label="Enter the Value for APPLICATION (Log Value) / Min:0.693, Max:4.595",format="%0.4f")
        thickness_log = st.number_input(min_value=-1.714,max_value=7.824,value="min",
                                        label="Enter the Value for THICKNESS (Log Value) / Min:-1.714, Max:7.824",format="%0.4f")
        width = st.number_input(min_value=6.713,max_value=7.673,value="min",
                                label="Enter the Value for WIDTH (Log Value) / Min:6.713, Max:7.673",format="%0.4f")
        product_ref = st.number_input(min_value=13.324,max_value=21.266,value="min",
                                      label="Enter the Value for PRODUCT REF (Log Value) / Min:13.324, Max:21.266",format="%0.4f")

        

    button= st.button(":violet[PREDICT]",use_container_width=True)

    if button:
        price= predict_selling_price(status,item_type,quantity_tons_log, customer_log,country,application,thickness_log,width,product_ref)
        
        
        st.write("## :green[The Selling Price is :]",price)
