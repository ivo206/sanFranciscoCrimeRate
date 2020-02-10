# sanFranciscoCrimeRate

# 1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
- Changing values on the SparkSession the throughput and latency would change and we could see that in tha variables: inputRowsPerSecond, which is the rate of data arriving and processedRowsPerSecond, which is the rate at which Spark is processing the data.

# 2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
I could get the best performances by setting the spark.sql.shuffle.partitions to be equal to the number of cores divided by the number of tasks to work with, spark.default.parallelism to be equal to the number of 3 times the number of cores. 
