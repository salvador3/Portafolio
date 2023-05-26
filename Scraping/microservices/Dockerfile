FROM python:3.9
RUN pip install --no-cache-dir gunicorn

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
    
ADD requirements.txt .
RUN pip install -r requirements.txt

# Copy local code to the container image.
WORKDIR /app
COPY /src .
ADD . .

ENV PORT 8081

EXPOSE 8081
CMD exec gunicorn --bind 0.0.0.0:8081 --workers 2 --threads 2 --timeout 0  main:app