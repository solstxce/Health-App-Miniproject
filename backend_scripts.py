# # backend_scripts.py
# import plotly.graph_objs as go
# from datetime import datetime

# def visualize_weight(fig, data):
#     fig.update_layout(title="Weight Trend", xaxis_title="Date", yaxis_title="Weight (kg)")

#     dates, weights = zip(*[(d, w) for d, w, _, _, _, _, _ in data])
#     fig.add_trace(go.Scatter(x=dates, y=weights, mode="lines"))

# def visualize_height(fig, data):
#     fig.update_layout(title="Height Trend", xaxis_title="Date", yaxis_title="Height (cm)")

#     dates, heights = zip(*[(d, h) for d, _, h, _, _, _, _ in data])
#     fig.add_trace(go.Scatter(x=dates, y=heights, mode="lines"))

# def visualize_bp(fig, data):
#     fig.update_layout(title="Blood Pressure Trend", xaxis_title="Date", yaxis_title="Blood Pressure (mmHg)")

#     dates, systolic, diastolic = zip(*[(d, s, d) for d, _, _, s, d, _, _ in data])
#     fig.add_trace(go.Scatter(x=dates, y=systolic, mode="lines", name="Systolic"))
#     fig.add_trace(go.Scatter(x=dates, y=diastolic, mode="lines", name="Diastolic"))

# def visualize_cholesterol(fig, data):
#     fig.update_layout(title="Cholesterol Trend", xaxis_title="Date", yaxis_title="Cholesterol (mg/dL)")

#     dates, cholesterol = zip(*[(d, c) for d, _, _, _, _, c, _ in data])
#     fig.add_trace(go.Scatter(x=dates, y=cholesterol, mode="lines"))

# def visualize_sugar(fig, data):
#     fig.update_layout(title="Blood Sugar Trend", xaxis_title="Date", yaxis_title="Blood Sugar (mg/dL)")

#     dates, sugar = zip(*[(d, s) for d, _, _, _, _, _, s in data])
#     fig.add_trace(go.Scatter(x=dates, y=sugar, mode="lines"))
# backend_scripts.py
import plotly.graph_objs as go
from datetime import datetime

def visualize_weight(fig, data):
    fig.update_layout(title="Weight Trend", xaxis_title="Date", yaxis_title="Weight (kg)")

    dates, weights = zip(*[(d, w) for d, w, _, _, _, _, _ in data])
    fig.add_trace(go.Scatter(x=dates, y=weights, mode="lines"))

def visualize_height(fig, data):
    fig.update_layout(title="Height Trend", xaxis_title="Date", yaxis_title="Height (cm)")

    dates, heights = zip(*[(d, h) for d, _, h, _, _, _, _ in data])
    fig.add_trace(go.Scatter(x=dates, y=heights, mode="lines"))

def visualize_bp(fig, data):
    fig.update_layout(title="Blood Pressure Trend", xaxis_title="Date", yaxis_title="Blood Pressure (mmHg)")

    dates, systolic, diastolic = zip(*[(d, s, d) for d, _, _, s, d, _, _ in data])
    fig.add_trace(go.Scatter(x=dates, y=systolic, mode="lines", name="Systolic"))
    fig.add_trace(go.Scatter(x=dates, y=diastolic, mode="lines", name="Diastolic"))

def visualize_cholesterol(fig, data):
    fig.update_layout(title="Cholesterol Trend", xaxis_title="Date", yaxis_title="Cholesterol (mg/dL)")

    dates, cholesterol = zip(*[(d, c) for d, _, _, _, _, c, _ in data])
    fig.add_trace(go.Scatter(x=dates, y=cholesterol, mode="lines"))

def visualize_sugar(fig, data):
    fig.update_layout(title="Blood Sugar Trend", xaxis_title="Date", yaxis_title="Blood Sugar (mg/dL)")

    dates, sugar = zip(*[(d, s) for d, _, _, _, _, _, s in data])
    fig.add_trace(go.Scatter(x=dates, y=sugar, mode="lines"))