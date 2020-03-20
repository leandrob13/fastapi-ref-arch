FROM python:3.8
RUN useradd -ms /bin/bash appuser
ADD . home/appuser/app
WORKDIR /home/appuser/app

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PATH $PATH:/root/.local/bin

RUN pip3 install --upgrade pip && \
pip3 install certifi && \
pip3 install pipenv --no-cache-dir --user && \
pipenv --python 3.8 && \
pipenv install --system --deploy && \
chown -R appuser:appuser /home/appuser/app

EXPOSE 8081
USER appuser
ENTRYPOINT python -m src.http.main