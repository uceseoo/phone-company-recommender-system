# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load customer data
customers = pd.read_csv('customer_data.csv')

# Select relevant features for clustering
features = ['data_allowance', 'international_calling', 'mobile_hotspot']
X = customers[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use K-Means clustering to identify customer segments
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to the customer data
customers['cluster'] = clusters

# Use the cluster labels to make personalized recommendations
for customer_id, cluster in customers[['customer_id', 'cluster']].values:
  # Get the customer's current plan data
  current_plan = customers[customers['customer_id'] == customer_id][['data_allowance', 'international_calling', 'mobile_hotspot']].values[0]

  # Select other customers in the same cluster
  similar_customers = customers[customers['cluster'] == cluster]

  # Calculate the average plan data for the similar customers
  average_plan = similar_customers[['data_allowance', 'international_calling', 'mobile_hotspot']].mean().values

  # Calculate the difference between the customer's current plan and the average plan
  plan_difference = current_plan - average_plan

  # If the customer's plan is below the average for their cluster, recommend a new plan
  if np.all(plan_difference < 0):
    recommended_plan = average_plan + plan_difference
    print(f'Customer {customer_id} should consider switching to a plan with:')
    print(f'Data allowance: {recommended_plan[0]:.0f}')
    print(f'International calling: {recommended_plan[1]:.0f}')
    print(f'Mobile hotspot: {recommended_plan[2]:.0f}')
