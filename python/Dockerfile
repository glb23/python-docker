FROM python:3.10-bullseye

RUN groupadd --gid 1000 appuser
RUN useradd -m -s /bin/bash -u 1000 -g 1000 \
    -G sudo,adm,sudo,plugdev,cdrom,www-data \
    appuser

# prepare folder for the venv
RUN mkdir -p /opt/venv
RUN chown -R appuser:appuser /opt/venv

USER appuser

# make a venv in /app/venv
RUN python3 -m venv /opt/venv

# use the venv
ENV PATH="/opt/venv/bin:$PATH"

# Download pip from pypa
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
# Install pip without interaction
RUN python3 /tmp/get-pip.py

# install requirements
# we have to use ./app because of our docker build context
# being set to the parent directory
COPY ./app/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
