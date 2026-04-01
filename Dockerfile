FROM odoo:19.0

USER root

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install debugpy --break-system-packages && \
    rm -rf /var/lib/apt/lists/*

USER odoo