from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("CSV Data Processing").getOrCreate()

# Read the CSV file and create a Spark DataFrame
df = spark.read.format("csv").option("header", "true").load("/path/to/csv/file")

# Filter the DataFrame based on a condition
filtered_df = df.filter(df["age"] > 30)

# Perform aggregation on the filtered data
aggregated_df = filtered_df.groupBy("occupation").agg({"salary": "mean", "age": "max"})

# Write the result to a new CSV file
aggregated_df.write.format("csv").option("header", "true").save("/path/to/output/csv/file")

# Stop the Spark session
spark.stop()
