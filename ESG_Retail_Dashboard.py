import psycopg2
import pandas as pd
from sklearn.cluster import KMeans
from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest

# Connect to PostgreSQL database

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ESG_Retail_Dashboard",
    user="postgres",
    password="Manisha13",
)

# Load data from PostgreSQL
query = "SELECT * FROM energyconsumption"
data = pd.read_sql(query, conn)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=2)  # Set the number of clusters as needed
data['kmeans_cluster'] = kmeans.fit_predict(data[['retail_store_id', 'light_consumption']])
# Adjust the features accordingly
print(data)

# Perform Isolation Forest outlier detection
clf = IsolationForest(contamination=0.1)  # Adjust the contamination parameter as needed
data['outlier'] = clf.fit_predict(data[['retail_store_id', 'light_consumption']])  # Adjust the features accordingly


# Create a Flask API
app = Flask(__name__)

@app.route('/get_clustered_data', methods=['GET'])
def get_clustered_data():
    # Define API endpoint to retrieve clustered data
    filtered_data = data
    return filtered_data.to_json(orient='records')

@app.route('/get_outliers', methods=['GET'])
def get_outliers():
    # Define API endpoint to retrieve outliers
    outliers = data
    return outliers.to_json(orient='records')

if __name__ == "__main__":
    app.run(debug=True)
