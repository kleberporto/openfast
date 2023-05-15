FROM ubuntu:latest

RUN apt update -y
RUN apt install -y

RUN apt-get install wget -y


ENV CONDA_DIR /opt/conda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
RUN /bin/bash Anaconda3-2023.03-1-Linux-x86_64.sh -b -p /opt/conda

ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda create -n openfast_env -y \
    && conda install -c conda-forge openfast \
    && which python

RUN mkdir openfast/
COPY openfast/ openfast/
RUN chmod -R 777 openfast/

WORKDIR /openfast
CMD ["python3", "python_teste.py"]