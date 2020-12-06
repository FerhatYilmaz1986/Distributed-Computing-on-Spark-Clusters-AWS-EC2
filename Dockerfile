FROM amazoncorretto:8
COPY . .
RUN yum -y update
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum list python3*
RUN yum -y install python3 python3-dev python3-pip python3-virtualenv
