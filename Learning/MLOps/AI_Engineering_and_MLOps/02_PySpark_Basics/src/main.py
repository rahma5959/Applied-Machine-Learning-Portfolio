from pyspark.sql import SparkSession   

spark = SparkSession.builder \
    .appName("OnlineRetailAnalysis") \
    .getOrCreate()

print("Spark started successfully!")

df=spark.read.csv("../data/Online Retail.csv", header=True, inferSchema=True)

# df.printSchema()

#df.select("Description", "Quantity", "UnitPrice").show()

#df.filter(df.UnitPrice>10).show()

df=df.withColumn("TotalPrice", df.UnitPrice * df.Quantity)

df=df.select("Description", "Quantity", "UnitPrice", "TotalPrice").show()

#CountrySales=df.groupBy("Country").sum("TotalPrice")
#CountrySales.show()

CountrySales=df.groupBy("Country").agg(sum(Quantity).alis(TotalQuantity))


spark.stop()