FROM python:3.8

# create and set the working directory
RUN mkdir src
WORKDIR /src

RUN pip install jupyter

EXPOSE 8888

CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --port=8888

