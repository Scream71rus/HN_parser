#!/bin/sh

PING=0

while [ $PING != 1 ] ; do
    PING=$(psql -d hn_parser -U admin -h db -c "select 'ping';" | grep -c 'ping')
    echo 'Await DB...'
    sleep 1s
done

if ! [ -f .is_install ] ; then
    mkdir log
    chmod +x server.py

    psql -h db -d hn_parser -U admin -f /home/application/hn_parser.sql

    touch .is_install
fi

python ./server.py
