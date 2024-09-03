FROM python:3.10.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV WORKDIR /code
RUN mkdir $WORKDIR
ADD . $WORKDIR
WORKDIR $WORKDIR
RUN apt-get update && apt-get install locales nginx locales-all python3-dev vim swig libxml2-dev libxslt-dev ffmpeg libsm6 libxext6 -y
RUN locale-gen pt_BR.UTF-8
RUN dpkg-reconfigure --frontend=noninteractive locales
ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
RUN update-locale LANG=pt_BR.UTF-8
RUN chmod +x entrypoint.sh
RUN python3 -m venv /opt/.venv
RUN /opt/.venv/bin/pip install --upgrade pip
RUN /opt/.venv/bin/pip install --upgrade setuptools
RUN /opt/.venv/bin/pip install wheel
RUN /opt/.venv/bin/pip install -r requirements.txt

CMD ["/code/entrypoint.sh"]