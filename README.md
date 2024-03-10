# Churn Prediction App

Churn prediction app is an app that allows a user to predict the likelihood of a customer churning based on a number of factors. The app also provides a probability based on the factor therefore giving you the predict and the probability of the predict.

## Defination of terms:

* Gender-- Whether the customer is a male or a female
* SeniorCitizen -- Whether a customer is a senior citizen or not
* Partner -- Whether the customer has a partner or not
* Dependents -- Whether the customer has dependents or not
* Tenure -- Number of months the customer has stayed with the company
* Phone Service -- Whether the customer has a phone service or not
* MultipleLines -- Whether the customer has multiple lines or not
* InternetService -- Customer's internet service provider (DSL, Fiber Optic, No)
* OnlineSecurity -- Whether the customer has online security or not (Yes, No, No Internet)
* OnlineBackup -- Whether the customer has online backup or not (Yes, No, No Internet)
* DeviceProtection -- Whether the customer has device protection or not (Yes, No, No internet service)
* TechSupport -- Whether the customer has tech support or not (Yes, No, No internet)
* StreamingTV -- Whether the customer has streaming TV or not (Yes, No, No internet service)
* StreamingMovies -- Whether the customer has streaming movies or not (Yes, No, No Internet service)
* Contract -- The contract term of the customer (Month-to-Month, One year, Two year)
* PaperlessBilling -- Whether the customer has paperless billing or not (Yes, No)
* Payment Method -- The customer's payment method 
* MonthlyCharges -- The amount charged to the customer monthly



## Built With:

* GUI:streamlit

* Database:Proprietory data from Vodafone

* Language:Python

## Key Features

* Home - That summarizes details about the project
* Data -  That shows the sample data used for model training
* Dashboard - That gives visual insights to the data
* predict - Shows customer churn prediction
* Feedback - for users comment and feedback

## Prerequisites Libraries:
* Please  Check in requirements .txt for the necessary libraries


## How to get Started
1) Clone this repository into your desired folder

```sh
   git clone https://github.com/qochieng/P4-ML-Streamlit-app
```  

2) Create a Virtual environment

```sh
   python -m venv
```   

3) Activate the Virtual environment

```sh
    venv/Scripts/activate
```

4) install the necessary Libraries in requirements.txt

```sh
    pip install -r requiremnts.txt
```

## How to run

To run the program, run the follwing code in your terminal

~~ Streamlit run Login.py

* A Login webpage will open
* To continue login using the provided credentials on the sidebar:[Username=guest] and [Password=guest123]
* Proceed to the predict page to perform prediction
![Alt text](<Pics/Screenshot 2024-03-09 192214.png>)

Predict page overview
![Alt text](<Pics/Screenshot 2024-03-09 193127.png>)

## Authors:

Quintor Ochieng'

- Github: [Github Profile](https://github.com/qochieng/P4-ML-Streamlit-app)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/quintor-ochieng)
- Medium: [Medium Profile](https://medium.com/@qochieng88/streamlit-churn-prediction-app-042a190d2aa2)

## LICENSE:
- MIT