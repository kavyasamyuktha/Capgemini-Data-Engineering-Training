# Phase 4

##  Key Concepts Learned and implemented

During this task, I strengthened my understanding of:

- Data loading using PySpark
- Data type casting (`cast`)
- Joining datasets using `join()`
- Aggregations using `groupBy()` and `sum()`
- Column transformations using `withColumn()`
- Conditional logic using `when()`
- Sorting and limiting results
- Building final reporting tables

---

##  What I Implemented

### 1. Daily Sales Analysis
- Calculated total revenue for each day
- Used `groupBy()` and aggregation functions

### 2. City-wise Revenue
- Joined sales and customer data
- Calculated revenue per city

### 3. Top 5 Customers
- Created full customer name using `concat_ws()`
- Calculated total spending
- Sorted and identified top 5 customers

### 4. Repeat Customers
- Counted number of orders per customer
- Filtered customers with more than one order

### 5. Customer Segmentation
- Categorized customers based on total spending:
  - Gold → Spend > 10000
  - Silver → Spend between 5000 and 10000
  - Bronze → Spend < 5000
- Used conditional logic with `when()`

### 6. Final Reporting Table
- Combined:
  - Customer details
  - Total spend
  - Order count
  - Segment
- Created a clean final dataset for reporting

---

##  Challenges Faced

- Handling data type conversion for numeric columns  
- Writing multiple joins correctly without confusion  
- Applying conditional logic for segmentation  
- Managing multiple transformations step-by-step  

---

##  Key Learnings

- Real-world data processing involves combining multiple datasets  
- PySpark transformations must be applied in a logical sequence  
- Aggregations and joins are core to data engineering tasks  
- Business insights can be derived from simple datasets with proper logic  

---

##  Outcome

By completing this task, I gained hands-on experience in:

- Performing end-to-end data analysis using PySpark  
- Generating business insights like revenue trends and customer segmentation  
- Writing cleaner and more structured PySpark code  

This task helped me move from basic operations to solving practical data problems.

---
