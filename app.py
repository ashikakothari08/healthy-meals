import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean dataset
df = pd.read_csv("healthy_meals_plan_cleaned.csv")
df.columns = df.columns.str.strip()

# Sidebar Filters
st.sidebar.title("Filters")
selected_diet = st.sidebar.multiselect("Select Diet Type", options=df['diet type'].unique(), default=df['diet type'].unique())
filtered_df = df[df['diet type'].isin(selected_diet)]

# Title
st.title("🍽️ Healthy Meal Plan Dashboard")
st.markdown("This dashboard helps stakeholders and directors analyze the nutritional aspects and trends in healthy meal planning.")

# Tabs for better layout
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Nutrients", "Preparation", "Diet Type Analysis"])

with tab1:
    st.subheader("1. Healthy vs Non-Healthy Meals")
    st.markdown("A pie chart showing proportion of healthy vs non-healthy meals.")
    fig1 = px.pie(df, names='is_healthy', title='Meal Health Distribution')
    st.plotly_chart(fig1)

    st.subheader("2. Diet Type Count")
    st.markdown("Distribution of meals by different diet types.")
    fig2 = px.histogram(filtered_df, x='diet type', color='is_healthy', barmode='group')
    st.plotly_chart(fig2)

    st.subheader("3. Ingredient Count Table")
    st.markdown("Average number of ingredients by healthiness.")
    st.dataframe(df.groupby('is_healthy')['num_ingredients'].mean().reset_index())

with tab2:
    st.subheader("4. Calories Distribution")
    st.markdown("Boxplot of calories for healthy vs non-healthy meals.")
    fig3 = px.box(df, x='is_healthy', y='calories', color='is_healthy')
    st.plotly_chart(fig3)

    st.subheader("5. Protein vs Calories")
    st.markdown("Are high-protein meals also high-calorie?")
    fig4 = px.scatter(df, x='protein', y='calories', color='is_healthy')
    st.plotly_chart(fig4)

    st.subheader("6. Nutrient Correlation")
    st.markdown("Correlation heatmap of calories, protein, fat, carbs.")
    corr = df[['calories', 'protein', 'fat', 'carbs']].corr()
    fig5, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig5)

    st.subheader("7. Macronutrient Histogram")
    st.markdown("Nutrient distribution across all meals.")
    st.bar_chart(df[['protein', 'fat', 'carbs']].mean())

with tab3:
    st.subheader("8. Prep Time vs Calories")
    st.markdown("Do high-calorie meals take longer to prepare?")
    fig6 = px.scatter(df, x='prep_time', y='calories', color='is_healthy')
    st.plotly_chart(fig6)

    st.subheader("9. Prep Time Distribution")
    st.markdown("Histogram of preparation time.")
    fig7 = px.histogram(df, x='prep_time', nbins=20, color='is_healthy')
    st.plotly_chart(fig7)

    st.subheader("10. Average Prep Time by Diet Type")
    st.markdown("How prep time varies by diet type.")
    st.bar_chart(df.groupby('diet type')['prep_time'].mean())

    st.subheader("11. Calories per Minute of Prep")
    df['cal_per_min'] = df['calories'] / df['prep_time'].replace(0, 1)
    st.line_chart(df[['cal_per_min']])

with tab4:
    st.subheader("12. Vegan Meals Analysis")
    st.markdown("Calories of meals marked as vegan.")
    st.dataframe(df[df['vegan'] == 1][['diet type', 'calories']].head(10))

    st.subheader("13. Healthy Meal Count by Diet Type")
    healthy_counts = df[df['is_healthy'] == 1]['diet type'].value_counts()
    fig8 = px.bar(x=healthy_counts.index, y=healthy_counts.values, labels={'x': 'Diet Type', 'y': 'Healthy Meal Count'})
    st.plotly_chart(fig8)

    st.subheader("14. Carbs vs Fat")
    st.markdown("Relationship between carbs and fat.")
    fig9 = px.scatter(df, x='carbs', y='fat', color='is_healthy')
    st.plotly_chart(fig9)

    st.subheader("15. Data Table: Filtered Meals")
    st.markdown("Explore the filtered meals below.")
    st.dataframe(filtered_df.head(20))

# Final notes
st.markdown("---")
st.markdown("✅ **Tip**: Use sidebar filters to analyze trends for specific diet types.")
