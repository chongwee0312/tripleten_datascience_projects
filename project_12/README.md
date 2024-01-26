# Introduction
Sweet Lift Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, we need to predict the amount of taxi orders for the next hour.

# Purpose
To develop a regression model to predict the hourly taxi orders. 

**As request by the Sweet Lift Taxi Company, the RMSE metric on the test set should not be more than 48 orders per hour.**

# Data
The dataset contains the number of taxi orders for every 10 minutes.

# Main Libraries Used
Pandas, Numpy, Statmodels, Matplotlib, Seaborn, Plotly, Scikit-Learn, XGBoost, CatBoost, LightGBM, Optuna

# Table of Contents
1. Introduction
2. Data Exploration and Preprocessing
3. Exploratory Data Analysis (EDA)
   - 3.1 Distribution of Hourly Taxi Orders
   - 3.2 Hourly, Daily and Monthly Time Series Graphs of Taxi Orders
   - 3.3 Mean Daily and Hourly Taxi Orders
   - 3.4 Trend and Seasonality
   - 3.5 Rolling Mean and Standard Deviation (Check for Stationarity)
4. Model Development
   - 4.1 Feature Creation
   - 4.2 Model Training
5. Model Evaluation
6. General Conclusion
