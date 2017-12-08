## Identificaton
identification is a simple web project which query ID-card information for flask framework.

## Library
    yum -y install python-devel python-pip
    yum -y install MySQL-python
    pip install --upgrade pip 
    pip install flask 
    pip install redis 
    pip install pycrypto 
    pip install flask-sqlalchemy 
    pip install pyjwt 
    pip install requests==2.18.1 
    pip install flask-cache
    pip install flask-babel

## Start
    cd identification
    python main.py

## Docker
    将Dockerfile移到identification的上层目录执行docker build