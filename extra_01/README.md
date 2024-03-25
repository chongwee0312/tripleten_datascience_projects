# Introduction
With thousands of uniservisities and colleges spread across the US, each with its own unique blend of programs and resources, categorising and understanding these institutions can be a challenging task. The insights gained through the cluster analysis of these colleges can be beneficial for students and families in the college selection process.

# Objective
This project aims to identifies the similarity and differences among the US colleges from different perspective.

# Data
**Description of data**

- Unnamed: 0: The college name
- Private: A factor with levels No and Yes indicating private or public university
- Apps: Number of applications received
- Accept: Number of applications accepted
- Enroll: Number of new students enrolled
- Top10perc: Percentage of new students from top 10% of H.S. class
- Top25perc: Percentage of new students from top 25% of H.S. class
- F.Undergrad: Number of fulltime undergraduates
- P.Undergrad: Number of parttime undergraduates
- Outstate: Out-of-state tuition
- Room.Board: Room and board costs
- Books: Estimated book costs
- Personal: Estimated personal spending
- PhD: Pct. of faculty with Ph.D.’s
- Terminal: Pct. of faculty with terminal degree
- S.F.Ratio: Student/faculty ratio
- perc.alumni: Pct. alumni who donate
- Expend: Instructional expenditure per student
- Grad.Rate: Graduation rate

# Main Libraries Used
Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, Scipy

# Table of Contents
1. Introduction
   - 1.1 Objective
2. Initialisation
3. Data Exploration and Data Preprocesing
4. Exploratory Data Analysis (EDA)
   - 4.1 Distribution of Public and Private Universities/Colleges
   - 4.2 Distributions of Popularity Features
   - 4.3 Distributions of Quality Features
   - 4.4 Distributions of Cost Features
5. Cluster Analysis
   - 5.1 Popularity
   - 5.2 Quality
   - 5.3 Cost
6. Conclusion
