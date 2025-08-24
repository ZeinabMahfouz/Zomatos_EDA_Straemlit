
import streamlit as st
import pandas as pd
import plotly.express as px

# Data Loading and Preprocessing
@st.cache_data
def load_and_preprocess_data():
    zomato = pd.read_csv("Zomato-Restaurants-EDA_Streamlit/zomato.csv", encoding="latin-1")
    country_code = pd.read_excel("Zomato-Restaurants-EDA_Streamlit/Country-Code.xlsx")
    data = pd.merge(zomato, country_code, on="Country Code", how="left")

    unnecessary_columns = [
        'Restaurant ID', 'Country Code', 'Address', 'Locality',
        'Locality Verbose', 'Switch to order menu'
    ]
    data.drop(columns=unnecessary_columns, inplace=True, errors='ignore')
    data['Cuisines'].fillna('Unspecified', inplace=True)
    
    # Drop duplicates
    data = data.drop_duplicates(subset=["Restaurant Name", "City", "Longitude", "Latitude", "Cuisines"], keep="first")

    # Feature Engineering
    data['Number of Cuisines'] = data['Cuisines'].apply(lambda x: len(str(x).split(',')))
    data['Average Cost per Person'] = data['Average Cost for two'] / 2

    return data

data = load_and_preprocess_data()

st.set_page_config(layout="wide", page_title="Zomato Restaurant Insights")

st.title("🍽️ Restaurant Insights Dashboard")
st.markdown("An interactive dashboard to uncover insights for **Restaurant Owners**, **Food Delivery Platforms**, and **Market Analysts**.")

# Sidebar Filters
st.sidebar.header("Filter Data")

# Country selector
country = st.sidebar.selectbox("Select Country", sorted(data["Country"].unique()))

# City selector (depends on country)
cities = sorted(data[data["Country"] == country]["City"].unique())
city = st.sidebar.selectbox("Select City", ["All"] + cities)

subset = data[data["Country"] == country]
if city != "All":
    subset = subset[subset["City"] == city]

# Stakeholder selector
stakeholder = st.sidebar.radio(
    "I am a...",
    ["Restaurant Owner", "Food Delivery Platform", "Market Analyst"]
)

# --- Insights Functions ---
def show_restaurant_owner_insights(subset):
    st.header("Insights for Restaurant Owners")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Rating", f"{subset['Aggregate rating'].mean():.2f}")
    col2.metric("Average Cost for Two", f"{subset['Average Cost for two'].mean():,.0f} {subset['Currency'].mode().iloc[0]}")
    col3.metric("Total Votes", f"{int(subset['Votes'].sum()):,}")

    st.subheader("Ratings Distribution")
    fig1 = px.histogram(subset, x="Aggregate rating", nbins=20, title="Distribution of Ratings")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Most Popular Cuisines")
    cuisine_counts = subset['Cuisines'].str.split(', ').explode().str.strip().value_counts().head(10).reset_index()
    cuisine_counts.columns = ['Cuisine', 'Count']
    fig2 = px.bar(cuisine_counts, x='Count', y='Cuisine', orientation='h', title='Top 10 Most Common Cuisines')
    st.plotly_chart(fig2, use_container_width=True)

def show_delivery_platform_insights(subset):
    st.header("Insights for Food Delivery Platforms")
    st.subheader("Online Delivery vs. Dine-in (Average Rating)")
    delivery_ratings = subset.groupby('Has Online delivery')['Aggregate rating'].mean().reset_index()
    delivery_ratings.columns = ['Has Online Delivery', 'Average Rating']
    fig3 = px.bar(delivery_ratings, x='Has Online Delivery', y='Average Rating',
                   color='Has Online Delivery', title='Average Rating by Online Delivery Availability')
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Cost vs. Rating for Online Delivery Restaurants")
    online_delivery_data = subset[subset['Has Online delivery'] == 'Yes']
    if not online_delivery_data.empty:
        fig4 = px.scatter(online_delivery_data, x="Average Cost per Person", y="Aggregate rating",
                          size="Votes", hover_data=["Restaurant Name", "Cuisines"],
                          title="Cost vs. Rating (Online Delivery Restaurants)")
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.info("No restaurants with online delivery in this selection.")

def show_market_analyst_insights(subset, data):
    st.header("Insights for Market Analysts")
    st.subheader("Global Geographic Overview")
    fig5 = px.scatter_mapbox(data,
                             lat="Latitude",
                             lon="Longitude",
                             hover_name="Restaurant Name",
                             hover_data=["City", "Country", "Cuisines", "Aggregate rating"],
                             color="Aggregate rating",
                             color_continuous_scale=px.colors.sequential.Viridis,
                             zoom=1,
                             title='Interactive Map of Restaurant Locations and Ratings')
    fig5.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Price Range Distribution")
    price_range_counts = subset['Price range'].value_counts().sort_index().reset_index()
    price_range_counts.columns = ['Price Range', 'Count']
    fig6 = px.bar(price_range_counts, x='Price Range', y='Count',
                   title='Distribution of Restaurants by Price Range')
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("Restaurant Count by Country")
    country_counts = data['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    fig7 = px.bar(country_counts, x='Country', y='Count', title='Number of Restaurants by Country')
    st.plotly_chart(fig7, use_container_width=True)

# --- Display according to stakeholder ---
if stakeholder == "Restaurant Owner":
    show_restaurant_owner_insights(subset)
elif stakeholder == "Food Delivery Platform":
    show_delivery_platform_insights(subset)
elif stakeholder == "Market Analyst":
    show_market_analyst_insights(subset, data)
