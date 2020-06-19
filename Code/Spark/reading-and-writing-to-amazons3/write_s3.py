
from pyspark.sql import SparkSession

def write_file():
        """
        Example script to test writing to S3 Bucket
        """
        spark = SparkSession.builder.appName("write file to S3").getOrCreate()

        # Get your file path from s3
        input_path = "s3n://databasedev-sparkify/cities.csv"
        df = spark.read.load(input_path, format="csv")

        # investigate what columns you have
        col_list = df.columns
        print(col_list)
        agg_df = df.groupby("city_name").count()

        # Get your output path - should be different than your input path
        output_path = "s3n://databasedev-sparkify/city-names.csv"
        agg_df.write.mode("overwrite").parquet(output_path)

if __name__ == "__main__":
        write_file()