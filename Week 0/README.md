# Data Engineering Training Journey

This repository reflects my learning progress during data engineering training, where I moved step by step from basic concepts to building complete data workflows using PySpark and Databricks. Each phase focuses on practical understanding, hands-on implementation, and developing real-world data engineering skills.

# WEEK 0 – Foundation Phase

## Phase 0: Databricks Setup and Introduction

In this phase, I completed the Databricks Associate Data Engineering course. This helped me get familiar with the Databricks environment and understand how distributed data processing works in practice.

### Topics Covered:

Databricks workspace and notebook environment
Running basic Spark operations
Understanding clusters and execution context
Introduction to distributed computing

### Key Learnings:

I developed a basic understanding of how Databricks works and how Spark executes operations in a distributed environment. This phase built my confidence in working with big data tools.

### Outcome:

Gained foundational knowledge of Databricks and became comfortable executing basic Spark operations.

## Phase 1: SQL Operations (SELECT, FILTER, GROUP BY)

### Topics Covered:
SELECT queries for data retrieval
Filtering data using conditions
GROUP BY for aggregation and summarization

### Key Learnings:

I learned how to extract and filter data efficiently and how aggregation works to summarize datasets. This helped me understand how raw data is transformed into meaningful insights.

### Challenges Faced:

Initially, understanding how grouped results are formed was difficult. I also needed time to adjust from SQL syntax to PySpark DataFrame operations.

### Outcome:

Improved understanding of data querying and developed the ability to perform basic analytical operations using both SQL and PySpark.

## Phase 2: Joins and Aggregations in PySpark

### Topics Covered:
Inner, left, right, and full joins
Aggregation functions in PySpark
Converting SQL logic into PySpark DataFrame operations

### Key Learnings:

I learned how to combine multiple datasets using joins and how different join types affect results. I also improved my ability to translate SQL queries into PySpark code.

### Challenges Faced:

Join outputs were sometimes unexpected due to incorrect conditions or misunderstandings of join logic. Debugging required careful inspection of data.

### Outcome:

Strengthened my understanding of relational data processing and gained confidence in writing PySpark transformations.

## Phase 3 & 3A: PySpark Basics and Data Cleaning

### Topics Covered:

Basic PySpark DataFrame operations
SQL to PySpark syntax conversion
Data inspection using show() and printSchema()
Handling missing values and duplicate records
Data validation and filtering

### Key Learnings:
In this phase, I learned how to work with PySpark DataFrames and convert SQL logic into PySpark operations. Along with this, I understood the importance of data cleaning before analysis. I learned how to handle missing values, remove duplicates, and filter invalid data to ensure data quality.

I also realized that writing correct transformations is not enough; the data must be clean and consistent for accurate results.

### What I Did:

Used PySpark DataFrame operations for basic transformations
Converted SQL queries into PySpark syntax
Inspected datasets using show() and printSchema()
Identified null values, duplicates, and invalid age records
Removed rows with missing customer_id
Replaced missing name and city values with "Unknown"
Removed duplicate records
Filtered invalid age values
Verified dataset before and after cleaning
Counted customers in each city

### Challenges Faced:

Adjusting from SQL mindset to PySpark syntax
Understanding how transformations affect final output
Ensuring correct order of cleaning operations

### Outcome:

I developed a strong understanding of PySpark basics along with practical data cleaning skills. This phase helped me build confidence in preparing clean datasets for analysis and applying transformations correctly.

## Phase 4 & 4A: Complete Data Pipeline Implementation

### Topics Covered:
End-to-end ETL pipeline design
Data cleaning, joins, and aggregations
Data segmentation techniques
Reporting and final output generation
Bucketing techniques (Phase 4A)

### Key Learnings:

I understood how all ETL components work together to form a complete data pipeline. I also learned how to apply business logic for segmentation and grouping.

### Challenges Faced:

Inconsistent or missing data sometimes affected final outputs. Debugging multi-step pipelines required revisiting earlier transformations and ensuring correctness at each stage.

### Outcome:

Successfully developed a complete understanding of how production-level data pipelines are designed and executed.

### Overall Learning Summary

Through this training journey, I progressed from basic SQL concepts to building end-to-end data pipelines using PySpark and Databricks. Key improvements include:

Strong understanding of SQL and PySpark transformations
Experience with joins, aggregations, and ETL workflows
Ability to debug and fix data quality issues
Understanding of complete pipeline architecture
Improved analytical and problem-solving skills
