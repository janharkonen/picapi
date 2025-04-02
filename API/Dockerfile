FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
VOLUME /app
RUN echo "alias log='cat /app/log.txt'" > ~/.bashrc
EXPOSE 5000
CMD ["bash", "-c", "python -u API/picapi.py > /app/log.txt 2>&1"]
#go to this directory (where this dockerfile is)
#docker build -t picapi-flask-image .
#docker run --name picapi-flask -v $(pwd)/:/app/ picapi-flask-image