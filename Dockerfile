FROM python:3.7-slim
ADD Dockerfile /app/
ADD MyModel.py /app/
ADD connect_s3.py /app/
ADD requirements.txt /app/
ADD recipes-1.0.1-py3-none-any.whl /app/
ENV PYTHONPATH "/app:${PYTHONPATH}"
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install recipes-1.0.1-py3-none-any.whl
EXPOSE 5000

# Define environment variable
ENV MODEL_NAME MyModel
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

CMD python /usr/local/bin/seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE
