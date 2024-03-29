import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
all_data = pd.read_csv("all_data.csv")

# Exploratory Data Analysis (EDA)
def eda_all_data():
    """
    Perform Exploratory Data Analysis (EDA) on the combined dataset (all_data.csv).
    """

    # Display the first few rows of the dataset
    st.subheader("Exploratory Data Analysis for all_data")
    st.write("The first few rows of the dataset:")
    st.write(all_data.head())
    
    # Descriptive statistics
    st.write("Descriptive statistics of the dataset:")
    st.write(all_data.describe())
    
    # Distribution of Count per Month
    st.write("Distribution of bike rentals per month:")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Month', y='Count', data=all_data, estimator=sum, ci=None, palette='muted', ax=ax)
    ax.set_title('Distribusi Jumlah Peminjaman Sepeda pada Setiap Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Jumlah Peminjaman Sepeda')
    st.pyplot(fig)

    # Correlation matrix
    st.write("Correlation matrix between numerical features:")
    corr = all_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

# Streamlit Dashboard
def main():
    """
    Streamlit dashboard to display the results of EDA.
    """

    st.title("Exploratory Data Analysis Dashboard")

    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to:", ["Exploratory Data Analysis"])

    # Display EDA for all_data
    if selection == "Exploratory Data Analysis":
        eda_all_data()

if main == "_main_":
    main()
