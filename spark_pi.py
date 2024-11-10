# from pyspark.sql import SparkSession
#
# # Create a Spark session
# spark = SparkSession.builder \
#     .appName("CalculatePi") \
#     .master("local[*]") \
#     .getOrCreate()
#
# # Read the CSV file into a DataFrame
# df = spark.read.format('csv') \
#     .option('header', 'true') \
#     .option('inferSchema', 'true') \
#     .load('/opt/spark/work-dir/Match.csv')
#
# # Show the DataFrame content
# df.show()
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

def get_absolute_path(path, filename):
    current_dir = os.path.dirname(__file__)
    relative_path = "{}{}".format(path,filename)
    absolute_path = os.path.join(current_dir,relative_path)
    return absolute_path;

def main(spark):
    path = "/opt/spark/work-dir/Data/"
    filename = "shipment.json"
    absolute_path = get_absolute_path(path, filename)
    df = spark.read.format('json').option('multiline',True).load(absolute_path)
    df.show(5,16)
#    df.printSchema()
    df = df.withColumn("Supplier_name", col("supplier.name"))\
           .withColumn("Supplier_city", col("supplier.city"))\
           .withColumn("Supplier_state", col("supplier.state"))\
           .withColumn("Supplier_country", col("supplier.country"))\
           .drop("supplier")\
           .withColumn("Customer_name", col("customer.name"))\
           .withColumn("Customer_city", col("customer.city"))\
           .withColumn("Customer_state", col("customer.state"))\
           .withColumn("Customer_country", col("customer.country"))\
           .drop("customer")\
           .withColumn("items", explode(col("books")))
    df.show(5,False)
    df.printSchema()
    
    df =  df.withColumn("qty", col("items.qty"))\
            .withColumn("title", col("items.title"))\
            .drop("items")\
            .drop("books")
    df.show(5,15,False)


if __name__ == '__main__':
    spark = SparkSession.builder.appName("Display of shipment") \
        .master("local[*]").getOrCreate()
    # Comment this line to see full log
    spark.sparkContext.setLogLevel('error')
    main(spark)
    spark.stop()




