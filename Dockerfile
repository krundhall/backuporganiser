# funny small python
FROM python:3.12-slim

# set working dir
WORKDIR /app

# copy working dir
COPY . .

# install flask
RUN pip install --no-cache-dir flask

# expose port
EXPOSE 5000

CMD ["python", "main.py"]
