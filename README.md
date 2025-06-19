📈 Walmart Sales Forecaster
This is an end-to-end data science project that forecasts weekly sales for a Walmart store using time series analysis and presents the results in an interactive web application.

🚀 Live Demo & Screenshot

[**➡️ View the Live Application Here**](https://walmart-time-series-sales-forecast-martinezreices.streamlit.app/)

📖 Project Overview
The primary goal of this project is to predict future weekly sales based on historical data. It demonstrates a complete machine learning workflow, including:

Data Ingestion & Cleaning: Loading and merging multiple data sources (train.csv, stores.csv, features.csv).

Exploratory Data Analysis (EDA): Analyzing the data to uncover trends, seasonality, and correlations.

Time Series Modeling: Using Meta's Prophet library to build a robust forecasting model that automatically detects yearly and weekly seasonal patterns.

Model Evaluation: Rigorously testing the model's performance using time series cross-validation to ensure its accuracy and reliability.

Interactive Visualization: Building a user-friendly web application with Streamlit to visualize the forecast and its underlying components.

Professional Code Structure: The project is refactored into a clean, modular structure, separating data logic, forecasting functions, and the user interface.

✨ Key Features
Interactive Forecasting: Users can select a forecast horizon (in weeks) and instantly generate a prediction.

Detailed Visualizations: The app displays the forecast with uncertainty intervals, allowing users to see the potential range of outcomes.

Model Interpretability: The "Forecast Components" plot breaks down the prediction into its core parts (overall trend, yearly seasonality, and weekly seasonality), making the model's logic easy to understand.

Clean, Modular Code: The application logic is separated into different source files for easier maintenance and scalability.

🛠️ Technologies Used
Language: Python

Data Manipulation: Pandas, NumPy

Forecasting Model: Prophet (by Meta)

Web Framework: Streamlit

Visualization: Plotly, Matplotlib, Seaborn

Model Persistence: Pickle

⚙️ How to Run Locally
To run this application on your own machine, please follow these steps:

Clone the Repository:

git clone https://[github.com/martinezreices/sales-forecast](https://github.com/martinezreices/sales-forecast)
cd your-repo-name

Create and Activate a Virtual Environment:

# Create the environment
python -m venv venv

# Activate it (on Mac/Linux)
source venv/bin/activate

# Or on Windows
.\venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Run the Streamlit App:

streamlit run app.py


