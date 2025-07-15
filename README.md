# Traffic_Management_and_Prediction
This is a simple Streamlit-based web application for predicting traffic volume and visualizing traffic trends using synthetic data. It utilizes basic machine learning (Linear Regression) to forecast hourly traffic based on time, day of the week, and weather conditions.

📊 Features
Interactive dashboard built with Streamlit

Visualizes average traffic volume by hour

Predicts traffic volume using a trained machine learning model

User inputs for hour, day of the week, and weather conditions

Easy-to-run app with minimal dependencies

🧠 Tech Stack
Python

Streamlit

Pandas

Scikit-learn

Matplotlib

📁 Dataset
The synthetic dataset (traffic_data.csv) includes:

timestamp: Date and time of traffic measurement

hour: Hour of the day (0–23)

day_of_week: Day of the week (0=Monday, 6=Sunday)

weather: Simulated weather condition (0=Clear, 1=Rain, 2=Fog)

traffic_volume: Number of vehicles per hour

Note: This dataset is randomly generated for demonstration purposes and does not represent real-world traffic data.

🚀 How to Run
Clone the repository:

bash
Copy
Edit
cd traffic-prediction-app
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run traffic_app.py
View in browser:
Navigate to http://localhost:8501 in your browser.

Output:

<img width="474" height="808" alt="image" src="https://github.com/user-attachments/assets/662d1b8c-5c8a-45d8-a9b9-e47d0033c3ce" />






Weather: Rain
