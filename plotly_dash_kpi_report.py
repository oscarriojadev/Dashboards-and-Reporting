# plotly_dash_kpi_report.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

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

def create_kpi_card(title, value):
    """
    Create a KPI card.

    Parameters:
    title (str): Title of the KPI.
    value (str): Value of the KPI.

    Returns:
    dash_html_components.Div: KPI card.
    """
    return html.Div(
        children=[
            html.H3(title),
            html.P(value)
        ],
        style={
            'border': '1px solid #ddd',
            'borderRadius': '5px',
            'padding': '10px',
            'margin': '10px',
            'textAlign': 'center'
        }
    )

def create_bar_chart(data, x_column, y_column, title):
    """
    Create a bar chart.

    Parameters:
    data (pd.DataFrame): Input data.
    x_column (str): Name of the x-axis column.
    y_column (str): Name of the y-axis column.
    title (str): Title of the chart.

    Returns:
    dash_core_components.Graph: Bar chart.
    """
    fig = px.bar(data, x=x_column, y=y_column, title=title)
    return dcc.Graph(figure=fig)

def create_line_chart(data, x_column, y_column, title):
    """
    Create a line chart.

    Parameters:
    data (pd.DataFrame): Input data.
    x_column (str): Name of the x-axis column.
    y_column (str): Name of the y-axis column.
    title (str): Title of the chart.

    Returns:
    dash_core_components.Graph: Line chart.
    """
    fig = px.line(data, x=x_column, y=y_column, title=title)
    return dcc.Graph(figure=fig)

def create_pie_chart(data, names_column, values_column, title):
    """
    Create a pie chart.

    Parameters:
    data (pd.DataFrame): Input data.
    names_column (str): Name of the names column.
    values_column (str): Name of the values column.
    title (str): Title of the chart.

    Returns:
    dash_core_components.Graph: Pie chart.
    """
    fig = px.pie(data, names=names_column, values=values_column, title=title)
    return dcc.Graph(figure=fig)

def main():
    # Load data
    file_path = 'path_to_your_data.csv'
    data = load_data(file_path)

    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define the layout of the Dash app
    app.layout = html.Div(
        children=[
            html.H1('KPI Report'),
            html.Div(
                children=[
                    create_kpi_card('Total Sales', f'${data["Sales"].sum():,}'),
                    create_kpi_card('Average Sales', f'${data["Sales"].mean():,}'),
                    create_kpi_card('Max Sales', f'${data["Sales"].max():,}'),
                    create_kpi_card('Min Sales', f'${data["Sales"].min():,}')
                ],
                style={'display': 'flex', 'flexWrap': 'wrap'}
            ),
            create_bar_chart(data, 'Category', 'Sales', 'Sales by Category'),
            create_line_chart(data, 'Date', 'Sales', 'Sales Trend'),
            create_pie_chart(data, 'Category', 'Sales', 'Sales Distribution')
        ]
    )

    # Run the Dash app
    if __name__ == '__main__':
        app.run_server(debug=True)

if __name__ == '__main__':
    main()
