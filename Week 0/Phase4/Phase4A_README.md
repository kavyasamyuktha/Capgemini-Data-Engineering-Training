# phase 4a - PySpark Bucketing & Segmentation

##  Dataset

**sales.csv**
Contains transaction-level data including `total_amount` representing customer spending.


##  Key Concepts Covered

* Data segmentation (bucketing)
* Business-rule based classification
* Data-driven segmentation
* Window functions for ranking
* Aggregation and grouping

---

##  Methods Implemented

### 1️ Bucketizer (MLlib)

* Uses predefined numeric ranges (*splits*) to divide data into buckets
* Outputs numerical bucket labels (e.g., 0, 1, 2)
* Commonly used in machine learning pipelines

---

### 2️ Window-based Ranking

* Uses `percent_rank()` function
* Assigns values between **0 and 1** based on relative position
* Helps understand customer ranking within the dataset

---

### 3️ Conditional Segmentation (Business Logic)

* Rule-based categorization using conditions

  * **Gold** → total_spend > 10000
  * **Silver** → 5000 ≤ total_spend ≤ 10000
  * **Bronze** → total_spend < 5000
* Easy to interpret and widely used in business scenarios

---

### 4️ Grouping Analysis

* Groups customers by segment
* Counts number of customers in each category
* Helps in understanding distribution across segments

---

### 5️ Quantile-based Segmentation

* Divides data into equal-sized groups based on distribution
* More balanced compared to fixed thresholds
* Adapts dynamically to changing data

---

### 6️ Comparison of Methods

This project compares multiple segmentation techniques:

* Conditional (rule-based)
* Quantile (data-driven)
* Bucketizer (ML approach)
* Ranking (relative positioning)

---

##  Output Insights

* Different segmentation techniques produce different categorizations
* Quantile-based segmentation ensures balanced group sizes
* Business-rule segmentation reflects domain-specific thresholds
* Ranking provides a relative view of customer standing

---

##  Key Learnings

* **Conditional logic** is ideal for implementing business rules
* **Quantile segmentation** adapts better to changing data distributions
* **Bucketizer** is useful for scalable ML workflows
* **Window functions** help in advanced analytics and ranking

---
