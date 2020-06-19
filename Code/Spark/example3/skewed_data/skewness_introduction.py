from pyspark.sql import SparkSession

def explore_dataframe():
	
	spark = SparkSession.builder.appName("Skewness Introduction").getOrCreate()

	#TODO get your file path from s3 for parking_violation.csv
	input_path = "s3n://databasedev-sparkify/parking_violation.csv"
	df = spark.read.format("csv").option("header", True).load(input_path)

	# investigate what columns you have
	col_list = df.columns
	print(col_list)

    # TODO groupby month and year to get count
	year_df = df.groupby("year")
    month_df = df.groupby("month")
    
    # TODO write file partition by year, and study the executor in the spark UI
    output_path = "s3n://databasedev-sparkify/city-names.csv"
    year_df.write.mode("overwrite").parquet(output_path)

    # TODO use repartition function
    year_df.repartition(3)

    spark.stop()


if __name__ == "__main__":
	explore_dataframe()