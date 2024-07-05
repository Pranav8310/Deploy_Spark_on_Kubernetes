from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("CalculatePi") \
    .master("local[*]") \
    .getOrCreate()

# Read the CSV file into a DataFrame
df = spark.read.format('csv') \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .load('/opt/spark/work-dir/Match.csv')

# Show the DataFrame content
df.show()
