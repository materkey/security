## Quick Start Guide
1. `virtualenv -p python3 env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `docker run --rm -it -p 8081:80 vulnerables/web-dvwa`

### RCE
`python rce/run.sh`

### SQL-INJECTION
1. `python sql_injection/run_vulnerable.py` and enter `"""2'); drop table Users; --"""`

