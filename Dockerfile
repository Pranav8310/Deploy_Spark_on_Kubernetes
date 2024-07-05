# Use a specific version of the Spark image
FROM apache/spark:latest
# Set the working directory
WORKDIR /opt/spark/work-dir

# Copy the Python script and CSV file into the working directory
COPY spark_pi.py /opt/spark/work-dir/
COPY Match.csv /opt/spark/work-dir/

# Set appropriate permissions for the copied files (if necessary)
# RUN chmod 644 /opt/spark/work-dir/spark_pi.py /opt/spark/work-dir/Match.csv
