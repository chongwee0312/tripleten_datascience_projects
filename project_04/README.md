# Introduction
This project is to perform an analysis for the online gaming store Ice, which sells video games all over the world. User and expert reviews, genres, platforms (e.g. Xbox or PlayStation), and historical data on game sales are available from open sources. This project will analyse these data and identify patterns that determine whether a game succeeds or not. This will allow the store to plan a campaign for 2017.

# Purpose
This project aims to answer the following quesions:
1. What are the signs or patterns of a successful game?
2. Which game genres or platforms achieve a better sales?
3. Do user and professional scores affects sales?

# Hypothesis
Two hypotheses are formulated:
1. Average user scores of the Xbox One and PC platforms are the same.
2. Average user scores for the Action and Sports genres are different.

# Data
**Description of data**
- Name: the name of the game
- Platform: PS2, Wii, X360, etc
- Year_of_Release: the year when the game is first released
- Genre: role-playing, action, puzzle, etc
- NA_sales: sales in North American in million USD
- EU_sales: sales in Europe in million USD
- JP_sales: sales in Japan in million USD
- Other_sales: sales in other countries in million USD
- Critic_Score: score (out of a maximum of 100) rated by professionals
- User_Score: score (out of a maximum of 10) rated by users
- Rating: the age and content rating of the game

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scipy

# Table of Contents
1. Introduction
2. Data Exploration
   - Conclusion
3. Data Cleaning
   - MIssing Values
     - Name and Genre
     - Year of Release
     - Critic and User Scores
     - Rating
4. Exploratory Data Analysis (EDA)
   - Number of Released Games per Year
   - Overall Global Sales per Platform
   - Emerging and Declining Platforms
   - Current Growth Status of Platforms
   - Effect of User and Professional Reviews on Sales
   - Sales of the Same Games from Different Platforms
   - Distribution and Sales of Games per Genre
5. Regional Sales Analysis
   - Regional Market Shares per Platform
   - Regional Market Shares per Genre
   - Relationship between ESRB Rating and Game Sales
6. Hypothesis Testing
   - Hypothesis 1
   - Hypothesis 2
7. General Conclusion 
