# Introduction

A recommendation system is a powerful tool designed to analyse user data and preferences to generate personalised suggestions, thereby enhancing user experience and facilitating decision-making process. Recommedation systems play a crucial role in various domain such as e-commerce, streaming services, and content platforms, by helping users discover relevant products, movies, music, or information amidst the overwheming abundance of availabel choices. These systems not only increase user engagement and satisfaction but also drive revenue growth and forter customer loyalty by delivering tailored content.

# Objective
This project aims to develop two anime recommendation systems - collaborative filtering and content-based filtering.

# Data
The datasets used in this project are available at [Kaggle](https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020).

**Anime Dataset**
- `MAL_ID`: A unique identifier for an anime.
- `Name`: The name of the anime.
- `Score`: The average score rated by users.
- `Genres`: The genres which an anime belongs to.
- `Aired`: The airing schedule of the anime.
- `Producers`: The name of the production company.
- `Licensors`: The name of the company that hold the licensing rights for an anime.
- `Studios`: The name of studio which is responsible for producint the anime.
- `Source`: The source material (e.g. manga, game, and etc.) from which an anime is adapted.
- `Synopsis`: An overview of the plot, characters, themes, and setting of an anime.

**User Rating Dataset**
- `user_id`: A unique identifier for a user.
- `anime_id`: A unique identifier for an anime.
- `rating`: The rating given to the anime by the user.

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Tensorflow

# Table of Contents
1. Introduction
   - 1.1 Objective
2. Initialisation
3. Data Exploration and Data Preprocesing
4. Exploratory Data Analysis (EDA)
   - 4.1 Number of Animes Released
   - 4.2 Top Genres
   - 4.3 Top Animes
5. Collaborative Filtering Recommendation System
   - 5.1 Data Preparation
   - 5.2 Modeling
   - 5.3 Recommend the Existing Animes with the Highest Predicted Ratings to an Existing User
   - 5.4 Recommend an Existing Anime to the Existing Users who Have the Highest Predicted Ratings
   - 5.5 Recommend the Existing Animes which are Most Similar to the Highest Rated Animes by an Existing User (Item Based Recommendation)
   - 5.6 Recommend the Exisitng Highest Rated Animes by the Most Similar Users to an Existing User (User Based Recommendation)
6. Content-Based Filtering Recommendation System
   - 6.1 Data Preparation
   - 6.2 Modeling
   - 6.3 New Anime and New User
   - 6.4 Existing Anime and User Contents
   - 6.5 Recommend the Existing Animes with the Highest Predicted Rating to a New User
   - 6.6 Recommend a New Anime to the Existing Users who Have the Highest Precticted Ratings
   - 6.7 Recommend a New Anime to the Existing Users who Have the Highest Ratings on Similar Animes (Item Based Recommendation)
   - 6.8 Recommend the Exisitng Highest Rated Animes by the Most Similar Users to a New User (User Based Recommendation)
7. References
