# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.10

COPY . .

COPY ./python/requirements.txt requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip --default-timeout=100 install -r requirements.txt




# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python", "app.py"]
