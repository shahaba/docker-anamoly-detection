FROM python:3.9

COPY requirements.txt .

RUN pip install -r ./requirements.txt 

# create and set the working directory
WORKDIR /notebooks
VOLUME ["data", "notebooks"]

EXPOSE 8888

CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --port=8888

