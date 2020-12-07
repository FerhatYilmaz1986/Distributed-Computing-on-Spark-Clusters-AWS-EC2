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

#Read data into dataframes
training_set = spark.read.csv("/home/ec2-user/TrainingDataset.csv", header=True, inferSchema= True, sep=';')
validation_set = spark.read.csv("/home/ec2-user/ValidationDataset.csv", header=True, inferSchema= True, sep=';')

#Create feature vectors for training and test sets
assembler = VectorAssembler(inputCols=[training_set.columns[0],
 training_set.columns[1],
 training_set.columns[2],
 training_set.columns[3],
 training_set.columns[4],
 training_set.columns[5],
 training_set.columns[6],
 training_set.columns[7],
 training_set.columns[8],
 training_set.columns[9],
 training_set.columns[10]],outputCol = 'features')
training_assembled = assembler.transform(training_set)
train = training_assembled.select(training_assembled.columns[-1], training_assembled.columns[-2])

assembler = VectorAssembler(inputCols=[validation_set.columns[0],
 validation_set.columns[1],
 validation_set.columns[2],
 validation_set.columns[3],
 validation_set.columns[4],
 validation_set.columns[5],
 validation_set.columns[6],
 validation_set.columns[7],
 validation_set.columns[8],
 validation_set.columns[9],
 validation_set.columns[10]],outputCol = 'features')
validation_assembled = assembler.transform(validation_set)
validation = validation_assembled.select(validation_assembled.columns[-1], validation_assembled.columns[-2])

#Build and fit classification model
rf = RandomForestClassifier(labelCol=train.columns[-1],featuresCol='features',numTrees=50,maxDepth=15)
rf_model = rf.fit(train)
