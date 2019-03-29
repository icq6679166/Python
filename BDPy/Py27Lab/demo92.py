from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("hello").setMaster("local")
sc = SparkContext(conf=conf)
print(sc.getConf().getAll())
sc.stop()

spark = SparkSession.builder.appName("Spark").getOrCreate()
print(spark.sparkContext.getConf().getAll())
spark.sparkContext.stop()