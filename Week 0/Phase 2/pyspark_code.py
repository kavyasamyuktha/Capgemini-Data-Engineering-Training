# starting spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count, desc 

spark = SparkSession.builder.appName("phase2 practice").getOrCreate()

# loading datasets from spark playground
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
orders = spark.read.option("header", "true").csv("/samples/orders.csv")

# just checking data
customers.show()
orders.show()
customers.printSchema()
orders.printSchema()

# cleaning step (removing null customer_id)
customers = customers.dropna(subset=["customer_id"])
orders = orders.dropna(subset=["customer_id"])

# converting order_amount to number (otherwise aggregations won't work properly)
orders = orders.withColumn("order_amount", orders["order_amount"].cast("double"))

# 1. total order amount for each customer
print("total order amount per customer")
total_df = orders.groupBy("customer_id").agg(sum("order_amount").alias("total_amount"))
total_df.show()

# 2. top 3 customers by spend
print("top 3 customers")
top3 = total_df.orderBy(desc("total_amount")).limit(3)
top3.show()

# 3. customers with no orders
print("customers with no orders")
no_orders = customers.join(orders, "customer_id", "left").filter(orders.customer_id.isNull())
no_orders.select("customer_id", "first_name").show()

# 4. city wise revenue
print("city wise revenue")
city_rev = customers.join(orders, "customer_id").groupBy("city").agg(sum("order_amount").alias("revenue"))
city_rev.show()

# 5. average order amount per customer
print("avg order per customer")
avg_df = orders.groupBy("customer_id").agg(avg("order_amount").alias("avg_amount"))
avg_df.show()

# 6. customers with more than one order
print("customers with multiple orders")
multi_orders = orders.groupBy("customer_id").agg(count("*").alias("order_count")).filter("order_count > 1")
multi_orders.show()

# 7. sorting customers by total spend
print("customers sorted by spend")
sorted_df = customers.join(orders, "customer_id").groupBy("customer_id").agg(sum("order_amount").alias("total_spend")).orderBy(desc("total_spend"))
sorted_df.show()

# stopping spark
spark.stop()