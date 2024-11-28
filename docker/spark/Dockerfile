# Use the official Bitnami Spark image as the base
FROM bitnami/spark:latest

# Expose the necessary ports
EXPOSE 7077 8080

# Optionally, you can include additional setup steps here if necessary

# Define the command to run Spark
CMD [ "/opt/bitnami/spark/bin/spark-class", "org.apache.spark.deploy.master.Master" ]
