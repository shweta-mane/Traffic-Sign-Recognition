FROM python:3.6-slim
COPY ./predict.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./TrafficSignRecModel.h5 /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "predict.py"]