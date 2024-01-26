# Introduction
The OilyGiant mining company plans to choose a region and develops new oil wells. This project aims to  select the region with the highest profit margin.

# Purpose
To develop a machine learning model which predicts the volume of reserves in the new wells. By using the prediction in conjuction with the bootstrapping technique, select the oil wells with the highest estimated values and the region with the highest profit for the selected oil wells.

# Data
**Description of data**

*Features*
- id — unique oil well identifier
- f0, f1, f2 — three features of points (their specific meaning is not important, but the features themselves are significant to predict the target)

*Target*
- product — volume of reserves in the oil well (thousand barrels)

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn

# Table of Contents
1. Introduction
2. Data Exploration
3. Exploratory Data Analysis (EDA)
   - 3.1 Distribution of the Features Data
   - 3.2 Distribution of the Target Data
   - 3.3 Correlation between the Numerical Data
4. Development of Models
   - 4.1 Model Performance and Results
5. Profit Calculation and Risk Assessment
   - 5.1 Conditions and the Key Values
   - 5.2 Minimum Volume of Reserves Per Oil Well Without Losses
   - 5.3 Profit from the 200 Oil Wells with the Highest Predicted Volumes Per Region
   - 5.4 Distribution of Profit for Each Region
6. General Conclusion 
