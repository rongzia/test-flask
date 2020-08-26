## how to build
first install python and virtualenv.  
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
