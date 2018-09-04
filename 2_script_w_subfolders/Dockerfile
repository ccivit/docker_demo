FROM python:3

ADD . /keras

WORKDIR /keras

VOLUME ["/keras/data", "/keras/src"]

RUN pip install numpy

#ADD src/numpy_script.py /keras/src

#docker run -t -v /Users/ccivit/DataProjects/docker_demo/2_script_w_subfolders/src:/keras/src -v /Users/ccivit/DataProjects/docker_demo/2_script_w_subfolders/data:/keras/data test

#docker run -t -v src:/keras/src -v data:/keras/data test

CMD [ "python", "src/main.py" ]