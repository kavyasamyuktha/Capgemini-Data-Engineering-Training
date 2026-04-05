Process Workflow

1. Data Loading

Loaded CSV files using PySpark
Used the header option to read column names

2. Data Cleaning

Removed null values using dropna()
Converted the total_amount column to integer type for accurate calculations

3. Data Processing & Analysis
I worked on solving different types of queries, such as:

Daily Sales
Calculated total sales for each day
City-wise Revenue
Joined sales and customer datasets
Computed revenue for each city
Repeat Customers
Identified customers who made more than two purchases
Highest Spending Customer per City
Calculated total spending for each customer
Identified the top-spending customer in each city
Final Reporting Table
Created a summary table including:
Customer ID, Name, City, Total Spend, and Order Count
Key Learnings

Through this phase, I learned:

How to work with PySpark DataFrames effectively
Performing joins and aggregations
Handling real-world data cleaning scenarios
Writing efficient data transformations