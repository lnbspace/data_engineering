# data_engineering

## Bingo Welcome to apache spark 

<img src="spark.png">

## little things you need to know 

<img src="sparksetup.png">

## creating a common docker image for spark packages 

```
docker run -it  --name spark_common  ubuntu bash
```

## installing and setup all pre-requisite software related to spark 

```
apt update
apt  install  default-jdk  git  scala -y 
 java -version ; javac -version ; scala -version ; git --version 
  apt install wget -y
  wget  https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
 tar xvzf  spark-3.1.2-bin-hadoop3.2.tgz 
  rm  spark-3.1.2-bin-hadoop3.2.tgz 
   mv  spark-3.1.2-bin-hadoop3.2/  /opt/spark 
   apt install vim -y
   apt install python3 -y
    apt install net-tools -y
    

```

### setting /root/.bashrc file 
### Note : in very last line  add this data 
```
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```
## creating docker image from a running or non running container 

```
 docker  commit  -m  "spark common image"   spark_common   spark:v1 
```
