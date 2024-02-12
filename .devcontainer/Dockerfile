ARG VARIANT="debian-11"
FROM mcr.microsoft.com/devcontainers/base:${VARIANT}

LABEL dev.containers.features="common"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3-pip gdb gdbserver tmux file
RUN pip3 install --upgrade pip && pip3 install pwntools
RUN bash -c "$(curl -fsSL https://gef.blah.cat/sh)" -s -y
RUN cp /root/.gdbinit /home/vscode/.gdbinit && chown vscode:vscode /home/vscode/.gdbinit
RUN cp /root/.gef-2024.01.py /home/vscode/.gef-2024.01.py && chown vscode:vscode /home/vscode/.gef-2024.01.py
