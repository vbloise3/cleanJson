from pyspark import SparkContext
from operator import add

sc = SparkContext()
data = sc.parallelize(list("Hello Spark EMR World"))
counts = data.map(lambda x: (x, 1)).reduceByKey(add).sortBy(lambda x: x[1], ascending=False).coalesce(1).saveAsTextFile('s3://go-lambda-bucket/Spark_Output')
sc.stop()
