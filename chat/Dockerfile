FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files in your service's directory
# Modify these instructions to do that
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY models.py models.py
COPY websocket_manager.py websocket_manager.py
COPY config.py config.py
COPY mongodb.py mongodb.py
COPY request_forms.py request_forms.py
COPY utils.py utils.py
COPY test test
COPY authenticator.py authenticator.py
# Copy all of the subdirectories in your service's directory
# Modify these instructions to do that
COPY queries queries
COPY routers routers
COPY api api
COPY controllers controllers


# If you're using a relational database with migrations,
# uncomment the following line
# COPY migrations migrations

RUN python -m pip install -r requirements.txt
# CMD uvicorn main:app --host 0.0.0.0 --port $PORT
CMD uvicorn main:app --host 0.0.0.0

# If you're using a relational database and want migrations
# to be run automatically, delete the previous CMD line and
# uncomment this CMD line
# CMD python -m migrations up && uvicorn main:app --host 0.0.0.0
