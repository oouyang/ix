FROM mcr.micronsoft.com/devcontainers/typescript-node:20

RUN apt-get update && apt-get install -y vim bash-completion && apt-get clean -y && rm -rf /var/lib/apt/lists/*

COPY library-scripts/*.sh /tmp/library-scripts/

RUN bash /tmp/library-scripts/install.sh

RUN rm -rf /tmp/library-scripts
