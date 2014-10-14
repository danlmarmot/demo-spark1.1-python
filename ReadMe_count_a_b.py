#!/usr/bin/env python
# Run this with either python readme_count_a_b.py, or ./readme_count_a_b.py

import sys, os

SPARK_HOME = os.path.join(os.environ["HOME"], "bin/spark/current/")
sys.path.append(os.path.join(SPARK_HOME, "python"))
sys.path.append(os.path.join(SPARK_HOME, "python/lib/py4j-0.8.2.1-src.zip"))

#Uncomment to examine Python paths
# from pprint import pprint as pp
# print "Paths are:"
# pp(sys.path)

from pyspark import SparkContext

read_me = os.path.join(SPARK_HOME, "README.md")
sc = SparkContext("local", "Read Me")
read_me_data = sc.textFile(read_me).cache()

numAs = read_me_data.filter(lambda s: 'a' in s).count()
numBs = read_me_data.filter(lambda s: 'b' in s).count()

print "Lines with a: %i, lines with b: %i" % (numAs, numBs)

# A couple of assertions to make sure things are correct
assert(numAs is 83)
assert(numBs is 38)