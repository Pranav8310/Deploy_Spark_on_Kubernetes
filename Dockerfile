
#use the specific version of spark image
FROM apache/spark:latest

#set the working directory
WORKDIR /opt/spark/work-dir

#Create a dir to store the data
RUN mkdir -p  /opt/spark/work-dir/Data


#COPY ~/Projects/Spark_on_k8s/Match.csv /opt/spark/work-dir/
#COPY ~/Projects/Spark_on_k8s/spark_pi.py /opt/spark/work-dir/

#COPY ./Match.csv /opt/spark/work-dir/
#COPY ./spark_pi.py /opt/spark/work-dir/


COPY ./shipment.json /opt/spark/work-dir/Data/ 
COPY ./spark_pi.py /opt/spark/work-dir/
