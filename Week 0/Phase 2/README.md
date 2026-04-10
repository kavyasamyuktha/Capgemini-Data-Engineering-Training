##Phase 2 – Data Cleaning and Advanced Transformations

###What I Learned

In this phase, I focused on performing data cleaning and advanced transformations using PySpark
Learned how to handle missing data and prepare datasets for analysis
Understood how real-world data is processed before analysis
Practiced aggregation and join operations in PySpark

###I Practiced

Cleaning data by removing null values using dropna()
Converting the amount column to integer using cast() for accurate calculations
Using groupBy() and agg() to perform aggregations
Calculating total spend and average values for customers
Sorting data using orderBy()
Using limit() to get top results like highest spending customers
Applying joins to combine customer and order datasets
Identifying customers with no orders
Filtering customers who placed more than one order

###SQL to PySpark Mapping

WHERE → filter()

GROUP BY → groupBy()

ORDER BY → orderBy()

LIMIT → limit()

JOIN → join()

CAST → cast()

NULL handling → dropna(), fillna()

###What I Implemented

Cleaned dataset by removing null values using dropna()
Converted amount column to integer using cast()
Performed aggregations using groupBy() and agg()
Calculated total spend and average spend per customer
Sorted data using orderBy()
Extracted top spending customers using limit()
Joined customer and order datasets
Found customers with no orders
Filtered customers with multiple orders

###Challenges Faced

Difficulty in handling missing values and deciding whether to drop or keep them
Understanding join logic between multiple datasets
Writing aggregation logic using groupBy() and agg() instead of SQL queries
Handling data type conversions using cast()
Filtering grouped results correctly

###Final Outcome

Gained strong understanding of data cleaning and transformation in PySpark
Understood how joins and aggregations work in real-world datasets
Improved confidence in handling structured data pipelines
Built a strong foundation for advanced PySpark topics

###Summary

Successfully learned data cleaning, transformations, joins, and aggregations in PySpark. 
This phase helped strengthen my understanding of real-world data processing and prepared me for advanced data engineering concepts like complex joins and window functions.
