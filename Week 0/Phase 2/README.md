## Phase 2 – Data Cleaning and Advanced Transformations

### What I Learned:

In this phase, 
I focused on performing data cleaning and advanced transformations using PySpark. 
I learned how to handle missing data and prepare the dataset for analysis. 
I also practiced aggregation and join operations, which helped me understand real-world data processing.

### I practiced:

Cleaning data by removing null values using dropna() 
Converting the amount column to integer using cast() for accurate calculations 
Using groupBy() and agg() to perform aggregations 
Calculating total spend and average values for customers 
Sorting data using orderBy() Using limit() to get top results like highest spending customers 
Applying joins to combine customer and order datasets Identifying customers with no orders Filtering customers who placed more than one order

### SQL to PySpark Mapping:

SELECT → select()

WHERE → filter()

GROUP BY → groupBy()

ORDER BY → orderBy()

LIMIT → limit()

JOIN → join()

CAST → cast()

NULL handling → dropna(), fillna()

This helped me understand how SQL logic is implemented in PySpark.

### What I Implemented:

Cleaned dataset by removing null values using dropna() 
Converted amount column to integer using cast() 
Performed aggregations using groupBy() and agg() 
Calculated total spend and average spend per customer 
Sorted data using orderBy() Used limit() to get top spending customers 
Joined customer and order datasets Found customers with no orders Filtered customers with multiple orders

### Challenges Faced:

Difficulty in handling missing values and deciding whether to drop or keep them Understanding join logic between multiple datasets 
Writing aggregation logic using groupBy() and agg() 
Handling data type conversion using cast() 
Filtering grouped results correctly

### Final Outcome:

By the end of this phase, I became comfortable with data cleaning and transformation in PySpark. I understood how real-world datasets are processed using aggregations, joins, and filtering. This gave me strong confidence in working with structured data.

### Summary:

Successfully learned data cleaning, transformations, joins, and aggregations in PySpark. This phase helped me build a strong foundation for advanced data engineering concepts.
