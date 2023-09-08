# Introduction
This project is to perform an analysis for Crankshaft List to find which factors affecting the price of a vehicle.
Hundreds of free advertisements for vechicles are published on Crankshaft List website everyday, this project will analyse the data collected over the last few years and determine which factors have impacts on the price of a vehicle.

# Purpose
This project aims to answer the following questions:

1. Among the categorical variables (number of cylinders, condition, paint colour and transmission type), which of them will influence the price of a vehicle?
2. Is there any correlation between the numerical variable (odometer value and vehicle's age) and the price of a vehicle?

# Hypothesis
To answer the questions above, the following hypotheses are formulated:

1. The condition of a vehicle and the transmission type are the categorical factors which influence the price of a vehicle.
2. Both the odometer value and the vehicle's age are correlated with the price of a vehicle and there is a strong negative correlations between each of these two variables and the price.

# Data
**Description of the data**
- `price` - price of the vehicle
- `model_year` - model year of the vehicle
- `model` - model of the vehicle
- `condition` - condition of the vehicle
- `cylinders` - number of cylinders of the vehicle
- `fuel` — gas, diesel, etc.
- `odometer` — the vehicle's mileage when the ad was published
- `transmission` - auto, manual, etc.
- `paint_color` - colour of the vehicle
- `is_4wd` — whether the vehicle has 4-wheel drive (Boolean type)
- `date_posted` — the date the ad was published
- `days_listed` — from publication to removal

# Libraries Used
pandas, matplotlib.pyplot, seaborn

# Table of Contents
1. Introduction
2. Data Exploration
3. Data Cleaning
   - Finding and Analysing Missing Values
   - Fixing Data Types
   - Enrichment of Data
4. Exploratory Data Analysis
   - Categorical Variables
   - Numerical Variables
   - Lifetime of Advertisements
   - Average Price for Each Type of Vechivle
5. Hypothesis Testing
   - Hypothesis 1
   - Hypothesis 2
7. General Conclusion 
