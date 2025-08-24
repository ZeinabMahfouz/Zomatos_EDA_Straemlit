📊 Zomato Restaurant Insights Dashboard
This repository contains the code and analysis for a data science project focusing on the Zomato restaurant dataset. The project includes a Jupyter Notebook for Exploratory Data Analysis (EDA) and a Streamlit application that visualizes key insights for different stakeholders.

📁 Project Structure
Zomatos_EDA.ipynb: A Jupyter Notebook containing the data cleaning, feature engineering, and exploratory data analysis. It uses libraries like pandas, matplotlib, seaborn, and plotly.express to uncover patterns and relationships within the dataset.

Zomatos_Streamlit .py: A Python script for the interactive dashboard. This Streamlit application allows users to filter data and view insights tailored for specific roles: Restaurant Owner, Food Delivery Platform, and Market Analyst.

📝 Dataset Description
The dataset used in this project is a collection of restaurant information from Zomato's platform, primarily focusing on India. It includes various attributes for each restaurant, such as its name, city, location coordinates, cuisines offered, average cost for two, aggregate rating, number of votes, and whether it offers online delivery or table booking. The data provides a rich foundation for analyzing restaurant trends and performance metrics.

🚀 Getting Started
Prerequisites
To run this project, you'll need Python installed, along with the following libraries:

pip install pandas numpy matplotlib seaborn plotly-express streamlit


How to Run the App
Clone the repository:

git clone https://github.com/ZeinabMahfouz/Zomatos_EDA_Straemlit
.git
cd your-repo-name


Run the Streamlit app:

streamlit run "Zomatos_Streamlit .py"


The app will open in your web browser, where you can interact with the dashboard.

📈 Key Insights & Analysis
The analysis focuses on several key questions to provide actionable insights for different stakeholders.

General Insights
Data Concentration: The dataset is heavily concentrated in India, which accounts for over 90% of all restaurants. This is an important consideration for any conclusions drawn from the data.

Online Presence vs. Popularity: Restaurants with both online delivery and table booking options tend to receive more votes, suggesting that offering multiple convenient services correlates with higher popularity.

Stakeholder-Specific Insights
For Restaurant Owners:
The dashboard can help you identify top-performing cuisines and price ranges in specific cities, allowing you to tailor your business strategy.

For Food Delivery Platforms:
You can analyze the relationship between online delivery availability and restaurant ratings, helping you to understand the impact of your service on a restaurant's success.

For Market Analysts:
The interactive map visualizes the geographic distribution of restaurants and their ratings, which is useful for identifying potential new markets or areas for expansion.

You can explore which countries and cities have the highest average ratings, as well as the distribution of restaurants by price range.

🖼️ Visuals
Here are some examples of the key visualizations included in the project:

Chart Title

Description

Votes vs. Rating

A scatter plot showing the relationship between a restaurant's votes and its aggregate rating.

Average Votes by Service

A bar chart comparing the average votes for restaurants based on whether they offer online delivery, table booking, or both.

Interactive Map of Restaurants

An interactive map displaying restaurant locations with color-coding based on their aggregate rating.

Price Range Distribution

A bar chart showing the distribution of restaurants across different price ranges.

⏭️ Future Work
This project can be expanded upon in several exciting ways:

Advanced Analytics: Implement a collaborative filtering-based recommendation system to suggest restaurants to users.

Geospatial Analysis: Conduct a deeper dive into geospatial data to identify "food deserts" or areas with a high density of specific cuisine types.

Time-Series Analysis: If historical data were available, analyze trends in ratings, votes, and restaurant openings over time.

Deployment: Deploy the Streamlit dashboard on a public cloud platform like Streamlit Community Cloud or Heroku for wider accessibility.

🤝 Contribution
Feel free to open issues or submit pull requests if you have suggestions for improvements or new features.
