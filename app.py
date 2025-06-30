import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("healthy_meals_plan.csv")

# Sidebar filters
st.sidebar.title("Filters")
selected_diet = st.sidebar.multiselect("Select Diet Type", options=df['Diet'].unique(), default=df['Diet'].unique())
filtered_df = df[df['Diet'].isin(selected_diet)]

# Main Title
st.title("Healthy Meal Plan Dashboard")
st.markdown("This dashboard provides insights into healthy meal planning trends, preferences, and nutritional factors for management decision-making.")

# Tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Nutritional Analysis", "Prep Insights"])

with tab1:
    st.subheader("1. Meal Healthiness Distribution")
    st.markdown("This chart helps visualize the overall balance between healthy and non-healthy meals.")
    fig1 = px.pie(df, names='is_healthy', title='Healthy vs Non-Healthy Meals')
    st.plotly_chart(fig1)

    st.subheader("2. Diet Type Count")
    st.markdown("Shows the distribution of different diet categories.")
    fig2 = px.histogram(filtered_df, x='Diet', color='is_healthy', barmode='group')
    st.plotly_chart(fig2)

with tab2:
    st.subheader("3. Calories Distribution")
    st.markdown("Distribution of calorie counts across all meals.")
    fig3 = px.box(filtered_df, x='is_healthy', y='Calories')
    st.plotly_chart(fig3)

    st.subheader("4. Macronutrient Correlation")
    st.markdown("This heatmap identifies relationships between nutrition variables.")
    corr = df[['Calories', 'Fat', 'Protein', 'Carbs']].corr()
    fig4, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig4)

with tab3:
    st.subheader("5. Prep Time vs Calories")
    st.markdown("This scatter plot shows how calories relate to meal preparation time.")
    fig5 = px.scatter(filtered_df, x='prep_time', y='Calories', color='is_healthy')
    st.plotly_chart(fig5)

    st.subheader("6. Ingredients Count Distribution")
    st.markdown("Analyzes how the number of ingredients varies by meal type.")
    fig6 = px.histogram(filtered_df, x='num_ingredients', color='is_healthy', nbins=20)
    st.plotly_chart(fig6)

# You can continue adding up to 20 plots in this format
