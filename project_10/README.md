# Introduction
The Sure Tomorrow insurance company wants to solve several tasks related to the customer insurance benefits. This project aims to solve the given tasks with machine learning models and secure the privacy of customer data.

# Purpose
To solve the following tasks given by the Sure Tomorrow insurance company:

- Task 1: Find customers who are similar to a given customer. This will help the company's agents with marketing.
- Task 2: Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
- Task 3: Predict the number of insurance benefits a new customer is likely to receive using a linear regression model.
- Task 4: Protect clients' personal data without breaking the model from the previous task. It's necessary to develop a data transformation algorithm that would make it hard to recover personal information if the data fell into the wrong hands. This is called data masking, or data obfuscation. But the data should be protected in such a way that the quality of machine learning models doesn't suffer. You don't need to pick the best model, just prove that the algorithm works correctly.
 
# Data
**Description of data**

*Features*

- Gender -  insured person's gender
- Age -  insured person's age
- Salary -  insured person's yearly income
- Family members -  number of insured person's famliy members

*Target*
- Insurance benefits - number of insurance benefits received by an insured person over the last five years

# Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn

# Table of Contents
1. Introduction
2. Data Exploration and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Solving the Tasks Given by the Sure Tomorrow Company
   - Similar Customers
   - Is Customer Likely to Receive Insurance Benefit?
   - Regression (with Linear Regression)
   - Obfuscating Data
5. Proving That Data Obfuscation Can Work with Linear Regression
6. Test Linear Regression With Data Obfuscation
7. General Conclusion
