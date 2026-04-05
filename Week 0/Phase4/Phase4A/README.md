# PySpark Data Segmentation & Bucketing (Phase 4A)

## Dataset

**sales.csv**
Contains transactional data with attributes like `customer_id`, `sale_date`, and `total_amount`.

---

## Objective

The aim of this project is to explore how raw numerical data can be transformed into structured categories using PySpark. This process, known as **bucketing or segmentation**, helps in simplifying analysis and deriving actionable insights from data.

---

## Problem Statement

Businesses often deal with continuous values (e.g., customer spending), which are difficult to analyze directly. By segmenting these values into categories, we can better understand patterns, customer behavior, and distribution.

---

##  Techniques Applied

###  1. Rule-Based Segmentation

Used conditional logic to classify customers into:

* **Gold**
* **Silver**
* **Bronze**

This method is straightforward and aligns well with business requirements.

---

###  2. Bucketization using MLlib

Applied **Bucketizer** to divide spending into predefined ranges:

* Efficient for large-scale data processing
* Commonly used in feature engineering for ML models

---

###  3. Quantile-Based Segmentation

Segmented customers based on data distribution:

* Divides data into equal-sized groups
* Adapts dynamically to dataset changes

---

### 🔹 4. Window-Based Ranking

Used `percent_rank()` to:

* Assign relative ranking to customers
* Understand positioning within the dataset

---

### 5. Aggregation & Analysis

Performed grouping operations to:

* Count customers per segment
* Analyze distribution trends across categories

---

## 📊 Key Observations

* Different segmentation techniques yield different results
* Fixed thresholds may create uneven distributions
* Quantile-based methods ensure balanced grouping
* Ranking provides deeper insight into relative performance

---

##  Key Takeaways

* Segmentation simplifies complex numerical data
* Choice of method depends on use case:

  * Business-driven → Conditional logic
  * Data-driven → Quantiles
  * ML pipelines → Bucketizer
* Window functions enhance analytical capabilities

---

##  Conclusion

This project highlights how PySpark can be used to implement various segmentation strategies efficiently. Understanding these techniques is essential for building scalable data pipelines and performing advanced analytics in real-world scenarios.

---
