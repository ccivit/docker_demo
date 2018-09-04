#docker build -t test .

#docker run -t -v /Users/ccivit/DataProjects/docker_demo/3_script_w_tensorflow-cpu/src:/keras/src -v /Users/ccivit/DataProjects/docker_demo/3_script_w_tensorflow-cpu/data:/keras/data test

## FROM python:3
## Changed from "FROM python:3" to "FROM python:3.5" since there are no Tensorflow distros supporting the python 3 version that was being downloaded, which was 3.7. Tensorflow does support 3.5 as of this text.


FROM python:3.5

ADD . /keras

WORKDIR /keras

VOLUME ["/keras/data", "/keras/src"]

RUN pip install -U pip
RUN pip install -U tensorflow


CMD [ "python", "src/main.py" ]