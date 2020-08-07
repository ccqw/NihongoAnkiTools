FROM python:3.7

RUN apt-get install autoconf automake libtool
RUN export START_DIR=${PWD}
RUN pip install pipenv
COPY ./Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip uninstall -y pipenv

RUN cd $START_DIR

COPY get-vocab-sentences/* /
CMD ["python", "./get-sentences.py"]
