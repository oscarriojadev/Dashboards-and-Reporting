# streamlit_sales_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    data = pd.read_csv(file_path)
    return data

def plot_sales_trend(data, date_column, sales_column):
    """
    Plot the sales trend over time.

    Parameters:
    data (pd.DataFrame): Input data.
    date_column (str): Name of the date column.
    sales_column (str): Name of the sales column.
    """
    st.subheader('Sales Trend')
    fig, ax = plt.subplots()
    data.plot(x=date_column, y=sales_column, ax=ax)
    st.pyplot(fig)

def plot_sales_by_category(data, category_column, sales_column):
    """
    Plot the sales by category.

    Parameters:
    data (pd.DataFrame): Input data.
    category_column (str): Name of the category column.
    sales_column (str): Name of the sales column.
    """
    st.subheader('Sales by Category')
    fig = px.bar(data, x=category_column, y=sales_column, title='Sales by Category')
    st.plotly_chart(fig)

def plot_sales_distribution(data, sales_column):
    """
    Plot the distribution of sales.

    Parameters:
    data (pd.DataFrame): Input data.
    sales_column (str): Name of the sales column.
    """
    st.subheader('Sales Distribution')
    fig, ax = plt.subplots()
    sns.histplot(data[sales_column], ax=ax, kde=True)
    st.pyplot(fig)

def plot_top_products(data, product_column, sales_column, top_n=10):
    """
    Plot the top products by sales.

    Parameters:
    data (pd.DataFrame): Input data.
    product_column (str): Name of the product column.
    sales_column (str): Name of the sales column.
    top_n (int): Number of top products to display.
    """
    st.subheader('Top Products by Sales')
    top_products = data.groupby(product_column)[sales_column].sum().nlargest(top_n).reset_index()
    fig = px.bar(top_products, x=product_column, y=sales_column, title=f'Top {top_n} Products by Sales')
    st.plotly_chart(fig)

def main():
    st.title('Sales Dashboard')

    # Load data
    file_path = 'path_to_your_data.csv'
    data = load_data(file_path)

    # Sidebar for user input
    st.sidebar.header('User Input')
    date_column = st.sidebar.selectbox('Date Column', data.columns)
    sales_column = st.sidebar.selectbox('Sales Column', data.columns)
    category_column = st.sidebar.selectbox('Category Column', data.columns)
    product_column = st.sidebar.selectbox('Product Column', data.columns)

    # Plot sales trend
    plot_sales_trend(data, date_column, sales_column)

    # Plot sales by category
    plot_sales_by_category(data, category_column, sales_column)

    # Plot sales distribution
    plot_sales_distribution(data, sales_column)

    # Plot top products
    plot_top_products(data, product_column, sales_column)

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()
