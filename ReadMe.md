# Spark 1.1 and Python demo scripts

Small demo of how to get standalone Python scripts working in Spark 1.1 through the regular Python interpreter,
rather than using bin/pyspark <filename.py>.

Useful for interactive debugging and avoids messing with PYTHONPATH.

These scripts are useful for checking out how Spark can be extended with Python scripts, and in particular I use this 
script inside of the PyCharm IDE debugger to shape the data that Spark returns.

Note that Spark is expected to be installed at ~/bin/spark/current