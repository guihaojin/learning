import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F


spark = SparkSession.builder.appName('test') \
                            .getOrCreate()

schema = StructType([ \
    StructField("SequenceNumber", StringType()), \
    StructField("ApproximateArrivalTimestamp", TimestampType()), \
    StructField("Data", StringType()), \
    StructField("PartitionKey", StringType()), \
    StructField("EncryptionType", StringType()), \
    StructField("ShardId", StringType())
])

df = spark.read.option('header', True) \
               .schema(schema) \
               .csv('proto-cloud_product_kinesis-source-Kinesis_Consumer_mm-sample-records.csv')
df.printSchema()
df.show()

df = df.withColumn('JsonData', F.unbase64('Data').cast('string'))
df.printSchema()
df.show()
