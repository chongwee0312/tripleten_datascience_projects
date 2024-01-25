# Introduction
The customers of Beta Bank are leaving little by little every month. The bankers figured out that it is more cost-effective to retain the existing customers rather than attract new ones. This project aims to build a model to predict whether a customer will leave the bank soon.

# Purpose
To develop a binary classification model which analyses the data on customers' past behaviour and termination of contracts to identify potential leaving customers. The f1-score of the model has to be 59% and above as requested by Beta Bank.

# Data
**Description of data**
*Features*
- RowNumber — data string index
- CustomerId — unique customer identifier
- Surname — surname
- CreditScore — credit score
- Geography — country of residence
- Gender — gender
- Age — age
- Tenure — period of maturation for a customer’s fixed deposit (years)
- Balance — account balance
- NumOfProducts — number of banking products used by the customer
- HasCrCard — customer has a credit card
- IsActiveMember — customer’s activeness
- EstimatedSalary — estimated salary

*Target*
- Exited — сustomer has left

# Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, CatBoost, Imbalanced-Learn

# Table of Contents
1. Introduction
2. Data Exploration
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
   - 4.1 Distributions of the Numerical Features Data
   - 4.2 Distributions of the Numerical Features Data Per Target Class
   - 4.3 Distributions of the Categorical Features Data based on Target Classes
   - 4.4 Distribution of the Target Classes
5. Feature Processing
6. Development and Fine Tuning of Different Models
   - 6.1 Without Resampling
   - 6.2 Class Weight Adjustment
   - 6.3 Upsampling (Oversampling)
   - 6.4 Downsampling (Undersampling)
   - 6.5 Resampling by a Combination of Upsampling and Downsampling (SMOTETomek)
7. Final Model Selection and Evaluation
   - 7.1 Threshold Adjustment
   - 7.2 F1-score, Precision and Recall
   - 7.3 ROC Curve and AUC-ROC Score
8. General Conclusion 
