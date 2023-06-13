import pickle 
import streamlit as st
import pandas as pd
import numpy as np
import sklearn

st.title("Hello streamlit")

st.header("Header")

st.subheader("Subheader")

st.text("Welcome to my first eer streamlit app")

st.markdown("""

## h2 tag
### h3 tag 
:moon: <br>
:sunglasses:

""", True)

def predict(names):
    # model = pickle.load(open(
    #     r"C:\Users\Prince\OneDrive\Desktop\Projects\Water quality Prediction\models\model.pkl",  "rb"))
    model = pickle.load(open(
        r"C:\Users\Prince\OneDrive\Desktop\Projects\Water quality Prediction\models\model.pkl",  "rb"))
    names = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    result = model.predict([names])
    # result = model.predict(names)

    return result

def main():
    CRIM = st.number_input("CRIM")

    ZN = st.number_input("proportion of residential land zoned")

    INDUS = st.number_input("proportion of non-retail business acres per town")

    CHAS = st.number_input(
        "Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)")
    
    NOX = st.number_input("nitric oxides concentration")

    RM = st.number_input("average number of rooms per dwelling")

    AGE = st.number_input(
        "proportion of owner-occupied units built prior to 1940")
    
    DIS = st.number_input(
        "weighted distances to ﬁve Boston employment centers")
    
    RAD = st.number_input("index of accessibility to radial highways")

    TAX = st.number_input("full-value property-tax rate per $10,000")

    PTRATIO = st.number_input("pupil-teacher ratio by town")

    B = st.number_input("B")

    LSTAT = st.number_input("LSTAT")

    names = [CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]

    if st.button("prediction"):

        result = [names]
        ans = predict(result)
        st.success(f"your home price could be {result}")
        print(result)


if __name__ == "__main__":
    main()
