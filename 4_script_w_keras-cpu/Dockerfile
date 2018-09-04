#docker build -t keras_docker .

#docker run -v /Users/ccivit/DataProjects/docker_demo/4_script_w_keras-cpu/src:/keras/src -v /Users/ccivit/DataProjects/docker_demo/4_script_w_keras-cpu/data:/keras/data keras_docker


FROM python:3.5

ADD . /keras

WORKDIR /keras

VOLUME ["/keras/data", "/keras/src"]

RUN pip install -U pip
RUN pip install -U tensorflow
RUN pip install keras

CMD [ "python", "src/main.py" ]