import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
from pyspark import SparkFiles
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.classification import RandomForestClassifier,DecisionTreeClassifier,GBTClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.classification import MultilayerPerceptronClassifier
#Create spark session, connect to master and worker nodes
spark = SparkSession.builder.master('spark://<hostip>:7077').appName('training_model').getOrCreate()
