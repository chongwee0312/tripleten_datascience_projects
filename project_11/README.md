# Introduction
A used car sales service provider Rusty Bargain intends to develop an app to attract new customers. The app allows users to quickly find out the market values of their cars. 

# Purpose
This project aims to build a regression model to predict the car prices. The model performance should based on the following criteria as requested by Rusty Bargain:

- The quality of the prediction
- The speed of the prediction
- The time required for training

# Data
**Description of data**

*Features*
- DateCrawled: date profile when the data was downloaded from the database
- VehicleType: vehicle body type
- RegistrationYear: vehicle registration year
- Gearbox: gearbox type
- Power: horsepower (hp)
- Model: vehicle model
- Mileage: mileage (measured in km due to dataset's regional specifics)
- RegistrationMonth — vehicle registration month
- FuelType: petrol, gasoline, etc.
- Brand: vehicle brand
- NotRepaired: whether vehicle has ever been repaired or not
- DateCreated: date of profile creation
- NumberOfPictures: number of vehicle pictures
- PostalCode: postal code of profile owner (user)
- LastSeen: date of the last activity of the user

*Target*
- Price: price (in Euro) of the vehicle

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, XGBoost, CatBoost, LightGBM, Optuna

# Table of Contents
1. Introduction
2. Data Exploration
3. Data Preprocessing
   - 3.1 Missing Values
   - 3.2 Anomalies
   - 3.3 Feature Engineering
4. Exploratory Data Analysis (EDA)
   - 4.1 Correlation between Numerical Features and Target
   - 4.2 Top Categories with the Highest Mean Prices in Categorical Features
5. Model Training
   - 5.1 Linear Regression
   - 5.2 Random Forest
   - 5.3 LightGBM
   - 5.4 CatBoost
   - 5.5 XGBoost
6. Model Evaluation and Analysis
7. Model Testing on Simulated Cases
8. General Conclusion
