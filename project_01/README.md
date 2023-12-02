# Introduction
This project is to prepare a report for a bank's loan division. This report will analyse the impact of customer's marital status, number of children, total income, purpose of loan on default rate.

This report will be considered when building the credit score of a potential customer. The credit score is used to evaluate the ability of a potential borrower to repay the loan.

# Purpose
This project aims to answer the following questions:
1. Is there a correlation between having children and paying back on time?
2. Is there a correlation between family status and paying back on time?
3. Is there a correlation between income level and paying back on time?
4. How does loan purpose affect the default rate?

# Hypothesis
To answer the questions above, the following hypotheses are formulated:
1. Customers who have no children have a lower default rate compared to those have children.
2. Customers who are married have a lower default rate compared to those are unmarried
3. Customers with high income have the lowest default rate.
4. Customers who borrow a loan for education have the highest default rate.

# Data
**Description of the data**
- `children` - the number of children in the family
- `days_employed` - work experience in days
- `dob_years` - client's age in years
- `education` - client's education
- `education_id` - education identifier
- `family_status` - marital status
- `family_status_id` - marital status identifier
- `gender` - gender of the client
- `income_type` - type of employment
- `debt` - was there any debt on loan repayment
- `total_income` - monthly income
- `purpose` - the purpose of obtaining a loan

# Libraries Used
pandas

# Table of Contents
1. Introduction
2. Data Exploration
3. Data Preprocessing
   - Finding and Analysing Missing Values
   - Data Transformation
   - Working with Missing Values
   - Data Categorisation
4. Hypothesis Testing
5. General Conclusion 
