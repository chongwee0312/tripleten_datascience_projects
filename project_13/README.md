# Introduction
The Film Junky Union, a new edgy community for classic movie enthusiasts, is developing a system for filtering and categorising movie reviews to detect negative reviews. 

# Purpose
To build a model for classifying positive and negative reviews by using a dataset of IMBD movie reviews with polarity labelling. **The model should have a F1 score of at least 0.85.**

# Data
**Description of data**
- `tconst`: A unique identifier for each movie in the IMDb database.
- `title_type`: The type or category of the title (e.g movis).
- `primary_title`: The primary title of the movie.
- `original_title`: The original title of the movie (in its original language).
- `start_year`: The year when the movie was released or started.
- `end_year`: The year when the movie ended (if applicable).
- `runtime_minutes`: The duration of the movie in minutes.
- `is_adult`: A binary indicator (1 or 0) indicating whether the movie is classified as "adult."
- `genres`: The genres associated with the movie.
- `average_rating`: The average rating given to the movie.
- `votes`: The number of votes the movie hasvie review.
- `rating`: The rating given in the review.
- `sp`: Sentiment polar orty (posittive, neutral) o
- `ds_part`: The part of the dataset (train or test).
- `idx`: An identifier for the data point in the dataset.

***Feature***
- `review`: The movie review in text.

***Target***
- `pos`: A binary indicator (1 or 0) indicating the sentiment polarity of the review.

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, Tensorflow, PyTorch, Optuna, NLTK, SpaCy, Transformers

# Table of Contents
1. Introduction
2. Data Exploration and Preprocessing
3. Exploratory Data Analysis (EDA)
   - 3.1 Number of Movies and Reviews Per Year
   - 3.2 Distribution of Number of Reviews per Movie
   - 3.3 The Top 10 Genres
   - 3.4 Distributions of Ratings in Train and Test Sets
   - 3.5 Distributions of Number of Reviews in Train and Test Sets
   - 3.6 Distribution of Target Classes
4. Model Development
   - 4.1 Text Normalisation
   - 4.2 Train / Test Split
   - 4.3 Model Development and Evaluation
       - 4.3.1 NLTK / Bag-of-Words
       - 4.3.2 NLTK / TF-IDF
       - 4.3.3 spaCy/ TF-IDF
       - 4.3.4 BERT
       - 4.3.5 Bidirectional Long-short Term Memory
   - 4.4 Final Evaluation
5. My Reviews
6. Model Deployment
7. General Conclusion
