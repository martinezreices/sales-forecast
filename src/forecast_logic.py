import pickle
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.graph_objects as go

def load_model():
    """Loads the pre-trained Prophet model from the .pkl file."""
    try:
        with open('src/prophet_model_store1.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        print("Model file not found. Please run the training notebook to create it.")
        return None

def generate_forecast_plots(model, forecast, history_df):
    model.history = history_df
    
    # Generate main forecast plot
    fig1 = plot_plotly(model, forecast)
    fig1.update_layout(
        title_text="Weekly Sales Forecast",
        xaxis_title="Date",
        yaxis_title="Weekly Sales"
    )
    
    # Generate components plot
    fig2 = plot_components_plotly(model, forecast)
    
    return fig1, fig2

