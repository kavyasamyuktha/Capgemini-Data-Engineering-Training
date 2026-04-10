Phase 2 – Data Cleaning & Advanced Transformations in PySpark
What I Learned

In this phase, I focused on performing data cleaning and advanced transformations using PySpark. I learned how to handle missing data and prepare datasets for meaningful analysis. I also practiced aggregation and join operations, which helped me understand real-world data processing workflows.

I gained hands-on understanding of how raw data is transformed into clean, structured, and analysis-ready data using PySpark DataFrames.

SQL to PySpark Mapping
WHERE → filter()
GROUP BY → groupBy()
ORDER BY → orderBy()
LIMIT → limit()
JOIN → join()
CAST → cast()
NULL handling → dropna() / fillna()
What I Implemented
Cleaned data by removing null values using dropna()
Converted the amount column to integer using cast() for accurate calculations
Performed aggregations using groupBy() and agg()
Calculated total spend and average spend per customer
Sorted results using orderBy()
Extracted top results using limit() (e.g., highest spending customers)
Applied joins to combine customer and order datasets
Identified customers with no orders
Filtered customers who placed more than one order
Challenges Faced
Handling missing values and deciding when to drop or retain them
Understanding correct usage of joins (especially inner vs left joins)
Writing aggregation logic using groupBy().agg() instead of SQL-style queries
Managing data type conversions using cast()
Filtering grouped results (like customers with multiple orders)
Final Outcome

By the end of this phase, I became comfortable with data cleaning and transformation techniques in PySpark. I understood how real-world datasets are prepared for analysis using aggregations, joins, and filtering operations. This strengthened my ability to work with structured data and build more complex data pipelines.

Summary

Successfully learned how to clean, transform, and analyze data using PySpark. This phase improved my understanding of joins, aggregations, and data preprocessing, giving me a strong foundation for advanced data engineering tasks.
