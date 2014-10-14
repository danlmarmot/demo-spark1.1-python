__author__ = 'dmckean'

'''
    Run this with either python readme_word_count.py, or ./readme_word_count.py
'''

import os, sys
from pprint import pprint

SPARK_HOME = os.path.join(os.environ["HOME"], "bin/spark/current/")
sys.path.append(os.path.join(SPARK_HOME, "python"))
sys.path.append(os.path.join(SPARK_HOME, "python/lib/py4j-0.8.2.1-src.zip"))
from pyspark import SparkContext

sc = SparkContext("local", "Read Me")
read_me_data = sc.textFile(os.path.join(SPARK_HOME, "README.md")).cache()

counts = read_me_data.flatMap(lambda line: line.split(" "))\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda a, b: a + b)

word_counts = counts.collect()

pprint(word_counts)