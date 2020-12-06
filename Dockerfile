FROM amazoncorretto:8
COPY . .
RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
