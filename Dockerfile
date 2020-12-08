FROM amazoncorretto:8
COPY . .
RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum list python3*
RUN yum -y install python3 python3-dev python3-pip python3-virtualenv

RUN python -V
RUN python3 -V

ENV PYSPARK_DRIVER_PYTHON python3
ENV PYSPARK_PYTHON python3

RUN pip3 install --upgrade pip
RUN pip3 install numpy panda
RUN pip3 install pyspark
RUN python3 -c "import numpy as np"
