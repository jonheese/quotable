#!/bin/bash
#set -x
CONF_FILE="/etc/default/quotable"
[ ! -f "$CONF_FILE" ] && echo "Create file $CONF_FILE with (at least) the \$EXEC variable defined (eg. /usr/bin/python /usr/local/bin/flask run --host-127.0.0.1 --port=5000)." && exit 1

. $CONF_FILE

[ -z "$EXEC" ] && echo "Create file $CONF_FILE with (at least) the \$EXEC variable defined (eg. /usr/bin/python /usr/local/bin/flask run --host-127.0.0.1 --port=5000)." && exit 1

LOG_FILE=${LOG_FILE:-/var/log/quotable.log}
export FLASK_APP=${FLASK_APP:-/usr/local/quotable/quotable.py}

date >> $LOG_FILE
$EXEC >> $LOG_FILE 2>&1
