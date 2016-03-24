#!/bin/bash
if [ "$1" = "" ]; then
  echo "You must specify a user"
  exit
fi

LAST_WEEK=`date --date="1 week ago" +"%Y-%m-%d"`
NUM_COMMITS=`svn log -r {$LAST_WEEK}:HEAD svn://svn | grep "| $1 |" | wc -l`
OUTPUT="User $1 has $NUM_COMMITS commit(s) in the past week."

echo $OUTPUT
if [ "$NUM_COMMITS" != "0" ]; then
  exit
fi

mail -s "SVN Commit Report for $1" trolen@windrock.com <<EOF
$OUTPUT
EOF
