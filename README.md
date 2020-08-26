## target
由于淘宝数据库月报太难根据标题查找，该项目通过 python 构建一个 web 服务，访问该服务可以直接查看所有的月报标题

## how to build
first install python and virtualenv.[pyenv、pipenv、virtualenv.md](pyenv、pipenv、virtualenv.md)  
then create a new environment to run this project, use :  
```
cd environment_path
virtualenv --python=/usr/bin/python3 ~/.local/environment_path/test-flask-env
cd environment_path/test-flask-env
source ./bin/activate
```

then:  
```
pip install Flask
pip install uwsgi
```

then:  
```
cd projects/test-flask
nohup uwsgi --ini uwsgi.ini &
```

note that `uwsgi.ini`.

last:  
```
deactivate
```
