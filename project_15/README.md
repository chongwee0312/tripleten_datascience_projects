# Introduction
The telecom opertor *Interconnect* would like to identify potential leaving customers. If they discover a customer is planning to leave, they will offer the customer promotional codes and special plan options. The Interconnect's marketing team has collected some of their clientele's personal data, including the information about the clientele's plan and contract.

# Purpose
1. To identify the characteristics and behaviours that distinguish between active customers and those who are likely to leave.
2. To develop a machine learning model to predict customer churn with a AUC-ROC score of at least 0.85.

# Data

**Description of `contract` data**

- `customerID`: A unique identifier for the customer.
- `BeginDate`: The date when the customer started using the service(s).
- `EndDate`: The date when the customer terminated the service. A value of `No` indicates that the customer is still using the service(s) at the time when the data is extracted (February 1, 2020).
- `Type`: The contract type (e.g. Month-to-month, One year, etc.).
- `PaperlessBilling`: A binary value which indicates whether the customer has opted for paperless billing.
- `PaymentMethod`: The method to make payments for the subsribed service(s) (e.g. Electronic check, Mailed check, etc.).
- `MonthlyCharges`: The amount charged to the customer on a monthly basis.
- `TotalCharges`: The accumulated amount charged to the customer over the entire subcription duration.

**Description of `personal` data**

- `customerID`: A unique identifier for the customer.
- `gender`: The gender of the customer (e.g. Female, Male)
- `SeniorCitizen`: A binary value to indicate whether the customer is a senior citizen.
- `Partner`: A binary value to indicate whether the customer has a partner.
- `Dependents`: A binary value to indicate whether the customer has dependents, such as children or other individuals who rely on them

**Description of `internet` data**

- `customerID` - A unique identifier for the customer.
- `InternetService` The type of internet service subsribed by the customer (e.g. DSL, Fiber optic)
- `OnlineSecurity`: A binary value which indicates if the customer has online security feature for the internet connection.
- `OnlineBackup`: A binary value which indicates if the customer has online backup service for the data.
- `DeviceProtection`: A binary value which indicates if the customer has device protection service for the connected device.
- `TechSupport`: A binary value which indicates if the customer has access to the technical support service.
- `StreamingTV`: A binary value which indicates if the customer has subscribed for the streaming TV service.
- `StreamingMovies`: A binary value which indicates if the customer has subscribed for the streaming movie service.

**Description of `phone` data**

- `customerID`: A unique identifier for the customer.
- `MultipleLines`: A binary value which indicates whether the customer has subcribed for the multiple lines.

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, XGBoost, CatBoost, Optuna

# Table of Contents
1. Introduction
   - 1.1 Project Description
   - 1.2 Problems
   - 1.3 Objectives
2. Methodology
3. Initialisation
4. Data Exploration
   - 4.1 Conclusion
5. Data Preprocessing
   - 5.1 Merging the Datasets
   - 5.2 Solving Identified Issues in Data Exploration
   - 5.3 Feature Engineering
6. Exploratory Data Analysis (EDA)
   - 6.1 Monthly Payment Distributions for Active Customers and Customers who Have Left
   - 6.2 Customer Share Per Service Type
   - 6.3 Customer Inflow and Outflow
   - 6.4 Distribution of Key Variables Per Service Type
   - 6.5 Churn Rate Per Categorical Feature
   - 6.6 Correlation Coefficients of Numerical Features and Target
   - 6.7 Distributions of Numercical Features Per Target Class
   - 6.8 Distribution of Target Classes
   - 6.9 Conclusion
7. Modeling
   - 7.1 Model Training
      - 7.1.1 Constant Model
      - 7.1.2 Logistic Regression
      - 7.1.3 Decision Tree
      - 7.1.4 LightGBM
      - 7.1.5 CatBoost
      - 7.1.6 XGBoost
8. Model Evaluation
   - 8.1 Final Model Selection
   - 8.2 Feature Importances
   - 8.3 Evaluation of the Final Model on the Test Set
9. General Conclusion
10. Recommendations
