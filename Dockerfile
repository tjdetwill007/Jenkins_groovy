FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask boto3 mysql.connector 
EXPOSE 80
CMD ["flask","run","--host=0.0.0.0","--port=80"]
