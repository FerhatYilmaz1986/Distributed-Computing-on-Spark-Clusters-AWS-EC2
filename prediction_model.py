import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
import sys

#Create and connect to spark session, read data given in docker command
spark = SparkSession.builder.master('local[*]').appName('Predict_model').getOrCreate()
test_set =spark.read.csv(sys.argv[-1], header=True, inferSchema= True, sep=';')

