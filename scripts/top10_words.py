import re
import sys
from pyspark.sql import SparkSession
from pyspark import StorageLevel

STOP = {"and", "or", "that", "the", "a", "an", "is", "are", "have"}

def tokenize(line):
    return [w for w in re.findall(r"[A-Za-z0-9']+", line.lower()) if w]

def main(input_path, persist_level):
    spark = SparkSession.builder.appName("Top10Words").getOrCreate()
    sc = spark.sparkContext

    rdd = sc.textFile(input_path)

    # set persistence level
    if persist_level == "MEMORY_ONLY":
        rdd.persist(StorageLevel.MEMORY_ONLY)
    elif persist_level == "DISK_ONLY":
        rdd.persist(StorageLevel.DISK_ONLY)

    words = rdd.flatMap(tokenize).filter(lambda w: w not in STOP)
    counts = words.map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)
    top10 = counts.takeOrdered(10, key=lambda x: -x[1])

    print("\nTop 10 Most Frequent Words:")
    for w, c in top10:
        print(f"{w}\t{c}")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: spark-submit top10_words.py <input_path> <MEMORY_ONLY|DISK_ONLY>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])