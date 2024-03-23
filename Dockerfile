FROM python:3.12-alpine

# Server part
WORKDIR /src

# Install dependencies
RUN python3 -m pip install --upgrade Pillow

# Launch server
CMD python src/main.py
