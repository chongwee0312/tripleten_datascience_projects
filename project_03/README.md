# Introduction
This project is to perform an analysis for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget. 500 randomly selected costumers data in 2018 are provided by the company.

# Purpose
This project aims to answer the following quesions:

1. Between the two plans, surf and ultimate, which of them generates more revenue for the Megaline company?
2. Do the users from different areas/regions generate different amount of revenue?

# Hypothesis
To answer the questions above, the following hypotheses are formulated:
1. The average revenue from users of the Ultimate and Surf calling plans differs.
2. The average revenue from users in the NY-NJ area is different from that of the users in the other regions.

# Data
**Description of the data**
- plan_name - calling plan name
- usd_monthly_fee — monthly charge in US dollars
- minutes_included — monthly minute allowance
- messages_included — monthly text allowance
- mb_per_month_included — data volume allowance (in megabytes)
- usd_per_minute — price per minute after exceeding the package limits (e.g., if the package includes 100 minutes, the 101st minute will be charged)
- usd_per_message — price per text after exceeding the package limits
- usd_per_gb — price per extra gigabyte of data after exceeding the package limits (1 GB = 1024 megabytes)

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scipy

# Table of Contents
1. Introduction
2. Data Exploration
   - Conclusion
3. Data Cleaning and Data Enrichment
   - Plan Data
   - User Data
   - Message Data
   - Internet Data
   - Anomalies
4. Data Aggregation
   - Monthly Data Per User
   - Merging Monthly Data Per User
   - Plan and User Statistics
5. Study User Behaviour
   - Number of Calls
   - Call Duration
   - Number of Messages
   - Volume of Internet Traffic
   - Revenue
   - Conclusion
6. Hypothesis Testing
   - Hypothesis 1
   - Hypothesis 2
7. General Conclusion 
