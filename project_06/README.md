# Introduction
This project is to develop a binary classification model for a mobile carrier Megaline to recommend one of the two newer phone plans, Smart and Ultra. The model will be developed by analysing the existing subscriber's behaviour data.

# Purpose
To develop a binary classification model which analyses user behaviour and recommends the most suitable phone plan. The accuracy of the model has to be 75% and above as requested by the Megaline company.

# Data
**Description of data**
- calls: number of calls
- minutes: total call duration in minutes
- messages: number of text messages
- mb_used: internet traffic used in MB
- is_ultra: plan for the current month (Ultra - 1, Smart - 0)

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn

# Table of Contents
1. Introduction
2. Data Exploration
3. Exploratory Data Analysis (EDA)
4. Development and Fine Tuning of Different Models
   - Decision Tree
   - Random Forest
   - Logistic Regression
   - Naive Bayes
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (Linear and Non-Linear)
   - Decision Tree with Adaptive Boosting
   - Random Forest with Adaptive Boosting
5. Final Model Selection and Evaluation
6. Sanity Check on the Final Model
   - Learning Curve Analysis
   - Classification Report Analysis
   - ROC Curve and AUC-ROC Score
7. General Conclusion 
