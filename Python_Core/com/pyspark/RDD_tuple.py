# Import
from pyspark.sql import SparkSession

# Create spark session
spark = SparkSession \
    .builder \
    .appName("mypysparkapp") \
    .getOrCreate()

# Create PySpark RDD from Tuple
data = [("Java", 20000),("Python", 10000),("Scala", 30000)]
rdd = spark.sparkContext.parallelize(data)

print(rdd.collect())