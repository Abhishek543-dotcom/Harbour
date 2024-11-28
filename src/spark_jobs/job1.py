from pyspark.sql import SparkSession

def run_job():
    spark = SparkSession.builder.appName("Job1").getOrCreate()
    df = spark.read.csv("s3a://your-bucket/input.csv")
    df.show()
