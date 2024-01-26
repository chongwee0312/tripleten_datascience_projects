# Introduction
Zyfra is a digital solution provider which improve the efficiency and safety of the mining, oil & gas, chemical and engineering industries. This project aims to build a machine learning model for Zyfra to predict the gold recovery.

# Purpose
To develop a regression model which predicts the gold recovery by using the data gathered at different stages of the gold extraction process.

# Data
**Description of data**

- date: exact datetime value of the gold extraction process to be carried out

Other columns are named with the format *[stage].[parameter_type].[parameter_name]*

*Possible values for [stage]*
- rougher: flotation
- primary_cleaner: primary purification
- secondary_cleaner: secondary purification
- final: final characteristics

*Possible values for [parameter_type]*
- input: raw material parameters
- output: product parameters
- state: parameters characterising the current state of the stage
- calculation: calculation characteristics

*Possible values for [parameter_name]*
- _air: volume of air
- _level: fluid level
- feed_size: size of the feed particle
- feed_rate: feeding speed
- concentrate_: percentage of the substance in the concentrate
- tail_: percentage of the substance in the rougher tails
- recovery - gold recovery in percentage

**Targets**

- **rougher.output.recovery**
- **final.output.recovery**

# Main Libraries Used
Pandas, Numpy, Statsmodels, Matplotlib, Seaborn, Scikit-Learn, XGBoost, CatBoost, LightGBM, Optuna

# Table of Contents
1. Introduction
2. Data Exploration
3. Data Preprocessing
   - 3.1 Checking the Values of Targets
   - 3.2 Analysing the Features Not Available in the Test Data
   - 3.3 Missing Values
4. Exploratory Data Analysis (EDA)
   - 4.1 Concentrations of Metals in Different Stages
   - 4.2 The Distributions of the Feed Particle Size in The Training and Test Datasets
   - 4.3 Distributions of the Total Concentration of Metals at Different Stages
   - 4.4 Distributions of the Target Data
5. Development of Models
   - 5.1 Separate the Data into Features and Targets
   - 5.2 Feature Selection
   - 5.3 Feature Scaling
   - 5.4 Training Different Models
   - 5.5 Fine-tuning Selected Models
   - 5.6 Evaluation of the Final Model on the Test Set
6. General Conclusion
7. Appendix
