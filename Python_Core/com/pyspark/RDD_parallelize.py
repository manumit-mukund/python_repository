# Import
from pyspark.sql import SparkSession

# Create spark session
spark = SparkSession \
    .builder \
    .appName("myapp") \
    .getOrCreate()

# Create PySpark RDD from Parallelize
rdd = spark.sparkContext.parallelize([1,2,3,4,5,6])

print(rdd.collect())