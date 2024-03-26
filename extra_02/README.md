# Introduction
A retailer wants to identify the itemsets which are most frequent bought by customers. A dataset of past transactions will be analysed and potential itemsets will be identified. Based on the identified itemsets, the retailer can develop corresponded strategies to improve customer satisfaction and increase profit.

# Objective
This project aims to find the most frequent bought itemsets for a retailer.

# Data
**Description of Data**

- BillNo: A unique identifier for each transaction
- Itemname: The product name
- Quantity: The quantity of each product purchased in the transaction
- Date: The date when the transaction occured
- Price: The price for one unit of the item
- CustomerID: A unique identifier for the customer
- Country: The country where the transaction took place

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Apyori

# Table of Contents
1. Introduction
   - 1.1 Objective
2. Initialisation
3. Data Exploration and Data Preprocesing
4. Exploratory Data Analysis (EDA)
   - 4.1 Total Transactions Per Country
   - 4.2 Total Sales Per Country
   - 4.3 Total Sales Per Day of Week / Month
   - 4.4 Popular Items
5. Market Basket Analysis
6. Conclusion
