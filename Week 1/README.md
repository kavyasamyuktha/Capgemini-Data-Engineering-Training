# WEEK 1 

## Phase 5: Data Analysis using PySpark

### Objective:
The main objective of this phase was to perform data analysis using PySpark on given datasets. The goal was to understand the data, analyze it, and generate meaningful outputs. This phase also focused on strengthening skills in data transformation, joins, aggregations, and window functions, which are essential for real-world data engineering tasks.

### Topics Covered:

Data loading using Spark
Joins across multiple datasets
Aggregations using groupBy()
Window functions (rank(), dense_rank())
Data transformation and column creation
Segmentation techniques

### Implementation:

Loaded multiple datasets using Spark
Joined tables: orders, customers, and order_items

### Calculated:
Total customer spend
Daily sales
Product-level sales
Applied window functions:
rank()
dense_rank()
Performed aggregations using:
groupBy()
sum()
count()
Transformed data:
Converted timestamp to date
Created new columns (customer segments: Gold, Silver, Bronze)
Generated final dataset containing:
customer_id, city, total_spend, segment, order_count

### Key Learnings:

Understanding joins in PySpark
Usage of window functions for ranking
Performing aggregations on large datasets
Handling date transformations
Importance of data cleaning before analysis
Difference between rank() and dense_rank()

### Challenges Faced:

Syntax errors in joins and functions
Understanding window function behavior
Applying correct business logic for segmentation
Managing multiple datasets together
Understanding partitioning in Spark

### Outcome:

Identified top 3 customers per city
Analyzed daily sales trends
Found best-performing products
Performed customer segmentation (Gold, Silver, Bronze)

## Day 2: Joins and GROUP BY in SQL

### What I Learned:
In this phase, I focused on SQL joins and GROUP BY operations. I learned how to combine multiple tables and summarize data using aggregation functions. This helped me understand how real-world data analysis is performed.

### Topics Covered:

Inner, Left, Right, and Full Outer Joins
GROUP BY with aggregation functions
Filtering grouped data using HAVING
Combining joins with aggregations

### What I Implemented:

Joined customer and order tables using different join types
Retrieved matched records using inner join
Found customers without orders using left join
Identified unmatched records using right join
Used full outer join for complete dataset comparison
Calculated total spend per customer using SUM()
Calculated average order value
Grouped data by customer_id and city
Filtered results using HAVING conditions
Found top customers using ORDER BY and LIMIT

### Challenges Faced:

Understanding differences between join types
Handling NULL values after joins
Using GROUP BY correctly with aggregates
Applying HAVING conditions
Combining joins and aggregations effectively

### Outcome:
Developed strong understanding of SQL joins and aggregation techniques, improving ability to analyze relational data.

## Day 3: CASE WHEN and Window Functions in SQL

### What I Learned:
This phase focused on conditional logic and advanced analytics using SQL. I learned how to use CASE WHEN statements and window functions to perform complex analysis without collapsing rows.

### Topics Covered:

CASE WHEN statements
Window functions with OVER()
ROW_NUMBER(), RANK(), DENSE_RANK()
PARTITION BY and ORDER BY
Running totals and cumulative calculations

### What I Implemented:

Categorized customers using CASE WHEN
Classified customers based on spending
Applied ROW_NUMBER() for unique ranking
Used RANK() and DENSE_RANK() for comparisons
Calculated running totals using window functions
Partitioned data by customer and city
Identified top records per group
Combined CASE WHEN with window functions

### Challenges Faced:

Understanding differences between ranking functions
Writing correct PARTITION BY logic
Applying multiple CASE conditions
Avoiding confusion between GROUP BY and window functions
Working with cumulative calculations

### Outcome:
Gained strong understanding of advanced SQL analytics, including ranking, segmentation, and running totals.

## Day 4: NULL Functions and String, Date, and Numeric Functions in SQL

### What I Learned:
In this phase, I focused on handling missing values and applying different types of SQL functions. I learned how NULL values affect query results and how to handle them properly using built-in functions. I also practiced string, date, and numeric functions to transform and analyze data effectively.

### Topics Covered:

NULL handling functions (IFNULL, COALESCE, NULLIF)
String functions (UPPER, LOWER, TRIM, LENGTH, SUBSTRING)
Pattern matching using LIKE
Date functions (CURRENT_DATE, DATE_ADD, DATEDIFF, EXTRACT)
Numeric functions (ROUND, CEIL, FLOOR)

### What I Practiced:

Replacing NULL values using IFNULL and COALESCE
Comparing values using NULLIF
Converting text to uppercase and lowercase
Removing extra spaces using TRIM
Extracting parts of strings using SUBSTRING
Filtering data using LIKE patterns (e.g., starts with, ends with)
Performing date calculations (adding days, finding differences)
Extracting year and month from date columns
Rounding and formatting numeric values

### What I Implemented:

Handled missing salary or values using NULL functions
Cleaned string columns by trimming and formatting text
Filtered records based on string patterns
Performed date-based analysis using date functions
Calculated differences between dates
Rounded numeric values for better readability
Applied multiple functions together in queries

### Challenges Faced:

Understanding behavior of NULL values in conditions
Choosing between IFNULL and COALESCE
Writing correct string patterns using LIKE
Applying multiple functions in a single query
Handling date formats correctly

### Outcome:
Developed a strong understanding of handling NULL values and applying string, date, and numeric functions. This improved my ability to clean, transform, and analyze data effectively using SQL.

## Day 5: PySpark Practice 

### What I Learned:
In this session, I focused on practicing core PySpark DataFrame operations using real datasets. I learned how SQL-like logic is implemented using PySpark transformations and actions.

### Topics Covered:

DataFrame creation and manipulation
Selecting, filtering, and transforming data
Joins and aggregations in PySpark
Column operations and type casting

### What I Practiced:

Creating DataFrames using SparkSession
Selecting columns using select()
Filtering data using filter()
Adding columns using withColumn()
Casting data types using cast()
Renaming columns using withColumnRenamed() and alias()
Splitting columns using split()
Adding constant values using lit()
Dropping columns
Performing joins
Using groupBy() with aggregations
Sorting using orderBy()
Using limit()

### What I Implemented:

Displayed datasets using show()
Filtered records based on conditions
Selected required columns
Converted data types
Added new columns (e.g., country)
Renamed columns for readability
Split full name into first and last name
Joined multiple DataFrames
Performed aggregations
Sorted and retrieved top records

### Challenges Faced:

Understanding difference between select() and withColumn()
Handling data type conversions
Using split function correctly
Writing join conditions
Managing multiple transformations

### Outcome:
Became comfortable with PySpark DataFrame operations and gained confidence in performing real-world data transformations.
