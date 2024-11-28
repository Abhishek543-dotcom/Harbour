from pyspark.sql import SparkSession

def run_job():
    spark = SparkSession.builder.appName("Job2").getOrCreate()
    df = spark.read.json("s3a://your-bucket/input.json")
    df.show()
