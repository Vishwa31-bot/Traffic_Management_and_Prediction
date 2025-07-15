
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("traffic_data.csv")
    return data

df = load_data()
st.title("Traffic Prediction and Management")

st.write("## Traffic Data Sample")
st.dataframe(df.head())

# Visualize traffic volume by hour
st.write("## Traffic Volume by Hour")
hourly_avg = df.groupby("hour")["traffic_volume"].mean()
fig, ax = plt.subplots()
hourly_avg.plot(kind="bar", ax=ax)
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Average Traffic Volume")
st.pyplot(fig)

# Prepare data for prediction
X = df[["hour", "day_of_week", "weather"]]
y = df["traffic_volume"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
st.write(f"## Model Performance")
st.write(f"Mean Absolute Error: {mae:.2f}")

# Predict traffic volume for user input
st.write("## Predict Traffic Volume")
hour = st.slider("Hour of Day", 0, 23, 12)
day = st.selectbox("Day of the Week", list(range(7)), format_func=lambda x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][x])
weather = st.selectbox("Weather", [0, 1, 2], format_func=lambda x: ['Clear', 'Rain', 'Fog'][x])

input_data = pd.DataFrame([[hour, day, weather]], columns=["hour", "day_of_week", "weather"])
prediction = model.predict(input_data)[0]
st.write(f"### Predicted Traffic Volume: {int(prediction)} vehicles/hour")
