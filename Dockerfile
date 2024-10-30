FROM python:3.12-slim
# 
ARG USERNAME=yc-dlan
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 
WORKDIR /usr/src/app

# 
RUN apt-get update

# OpenCV-Python
RUN apt-get install -y \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    pkg-config

# pip OpenCV
RUN pip install opencv-python

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | bash

# X11
RUN apt-get install -y \
    xvfb \
    x11-xkb-utils \
    x11-xserver-utils \
    xorg \
    xserver-xorg-dev \
    libgbm-dev \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libx11-dev

# XFCE
RUN apt-get install -y xfce4

# 复制GitKraken的安装包到容器中
COPY gitkraken-amd64.deb /usr/src/app/gitkraken-amd64.deb

# 安装GitKraken
RUN  apt-get install  /usr/src/app/gitkraken-amd64.deb  -fy

# 清理安装包
RUN rm /usr/src/app/gitkraken-amd64.deb

# 创建用户组和用户
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # 配置环境变量
    && echo "$USERNAME:'" | chpasswd \
    # 允许用户使用 sudo
    && usermod -aG sudo $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo 'source /opt/ros/humble/setup.bash' >> /home/$USERNAME/.bashrc \
    # 使新用户的 `.bashrc` 文件生效
    && chown $USERNAME:$USERNAME /home/$USERNAME/.bashrc
    
# 将当前目录下的应用文件复制到容器中
COPY . /usr/src/app

# 设置容器启动时执行的命令
CMD ["/bin/bash"]
