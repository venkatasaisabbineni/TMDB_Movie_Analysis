from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def process_data():
    spark = SparkSession.builder.appName("MovieDataProcessing").getOrCreate()
    movies_df = spark.read.json("data/movies.json")
    movies_results_df = movies_df.select(explode(movies_df.results).alias("movie"))
    vote_avg_df = movies_results_df.select(col("movie.vote_average"))
    avg_ratings = vote_avg_df.agg(avg("vote_average").alias("avg_rating"))
    avg_ratings.show()

if __name__ == "__main__":
    process_data()
