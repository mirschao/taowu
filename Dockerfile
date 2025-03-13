# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器的工作目录
COPY . /app

# 安装系统依赖（如 MySQL 客户端）
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    apt-get clean

# 使用 pip 安装项目依赖
RUN pip install -r requirements.txt

# 暴露应用运行的端口
EXPOSE 3364

# 启动应用的命令（根据您的应用修改）
CMD ["python", "main.py"]
