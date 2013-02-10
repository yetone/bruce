bruce
=====

demo: http://blog.yetone.net  

INSTALL
-------

```
git clone https://github.com/yetone/bruce.git bruce
cd bruce
cp config.py.sample config.py
virtualenv bruce_env
source bruce_env/bin/activate
pip install -r requirements.txt

```

Configurate
-------
Use your favorite editor edit the `config.py` file  

**note** Make sure `_DBNAME` in `config.py` exist in your mysql database.


RUN
-------
```
python app.py              # default
python app.py --port=8888  # run app on custom port
```

other
-------
If your want to use nginx as a reverse proxy, Read [Tornado Documentation](http://www.tornadoweb.org/documentation/overview.html?highlight=nginx#running-tornado-in-production)
