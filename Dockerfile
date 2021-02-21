FROM fedora:33
RUN dnf install -y python3-pytelegrambotapi
COPY . /opt/detoxebot/
WORKDIR /opt/detoxebot
ENTRYPOINT ["python3", "/opt/detoxebot/main.py"]
