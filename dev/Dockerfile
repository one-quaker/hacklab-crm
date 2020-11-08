FROM onepycoder/python:3.8.1-v2

ENV TZ=Europe/Kiev
ARG DEV_DIR=dev
ENV VEN_DIR=/vendor
ENV GECKODRIVER_BIN=$VEN_DIR/geckodriver

USER root
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list \
    && apt update -y \
    && apt -y install postgresql-client-12 libpq-dev postgresql-server-dev-all \
    && apt update -y && apt upgrade -y && apt install -y git firefox \
    && apt autoremove -y && apt clean && rm -rfv /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir $VEN_DIR
WORKDIR $VEN_DIR
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz \
    && tar -xvzf geckodriver* && chmod +x geckodriver

USER $USER
WORKDIR $APP_DIR
COPY ./src/requirements.txt $APP_DIR
RUN $ENV_PIP_BIN install -U pip --no-cache-dir && $ENV_PIP_BIN install -r requirements.txt --no-cache-dir

# add entrypoint script
USER root
COPY $DEV_DIR/entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
USER $USER

ENTRYPOINT ["/bin/zsh", "/entrypoint.sh"]
