FROM python:3.12

ARG UNAME=user
ARG UID=1000
ARG GID=1000

# Server part
WORKDIR /src

# Install dependencies
RUN python3 -m pip install --upgrade Pillow

# Add user
RUN groupadd -g $GID $UNAME && \
    useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

USER $UNAME

# Copy project files
COPY src src
COPY assets assets
COPY lib lib

# Launch script
CMD python src/main.py
