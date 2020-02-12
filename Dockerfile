"""
Docker is a tool used for the easy creation, deployment, and run of an application by using containers.
It allows developers to package up the application with all its dependencies, libraries, etc.
The advantage of containers is that this way, the application can be sent from a computer to another one,
and the developer can be sure that the app will run on other computer, where the settings might differ from
the settings of the computer on which the app was deployed and tested.
"""

FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv

RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install -i https://test.pypi.org/simple/ lambdata-doinalangille==0.1.2.1