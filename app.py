# app.py

import streamlit as st
from src.load_training_data import load_training_data
from src.forecast_logic import load_model, generate_forecast_plots

# --- Page Configuration ---
st.set_page_config(
    page_title="Sales Forecaster",
    page_icon="📈",
    layout="wide"
)

# --- Load Data and Model ---
history_df = load_training_data()
model = load_model()

# --- App Interface ---
st.title("📈 Walmart Sales Forecaster")
st.write("This app uses a pre-trained Prophet model to forecast weekly sales for Store 1.")
st.write("The model was trained on historical data from 2010 to 2012.")

# --- Sidebar ---
st.sidebar.header("Forecasting Options")
periods_input = st.sidebar.number_input(
    'Select forecast period (in weeks):',
    min_value=1, max_value=104, value=52
)

# --- Main Logic ---
# Check if data and model loaded successfully before proceeding
if history_df is not None and model is not None:
    if st.button("Generate Forecast"):
        with st.spinner("Generating forecast..."):
            # Create future dataframe and make predictions
            future = model.make_future_dataframe(periods=periods_input, freq='W')
            forecast = model.predict(future)
        
        st.success("Forecast generated successfully!")

        # Generate plots using our dedicated function
        fig1, fig2 = generate_forecast_plots(model, forecast, history_df)

        # Display plots
        st.header("Forecast Results for Store 1")
        st.write("This chart shows the historical sales (black dots), the model's forecast (blue line), and the uncertainty interval (light blue shade).")
        st.plotly_chart(fig1)

        st.header("Forecast Components")
        st.write("This shows the underlying patterns the model found in the data: the overall trend, and the yearly and weekly seasonalities.")
        st.plotly_chart(fig2)
        
        st.header("Forecast Data")
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods_input))
else:
    st.error("There was an error loading the data or the model. Please check the terminal for details.")

