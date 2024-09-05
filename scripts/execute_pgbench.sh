#! /bin/sh

set -eou pipefail 

SERVER_DNS=pg-pvc-at.postgres.com
SERVER_PORT=9002 #NLB port - route to 6432 on primary and replica
DURATION=60
POOLER=pgcat
TYPE=select
RESULT_DIR=${HOME}/${POOLER}-${TYPE}-`date "+%F-%H%M%S"`

mkdir -p ${RESULT_DIR}
rm -rf ${RESULT_DIR}/*

for i in 10 50 100 250 500;
do
  echo "Running with clients=$i"

  f=${RESULT_DIR}/${POOLER}_${i}.out
  > ${f}

  PGPASSWORD=pgbench /usr/pgsql-16/bin/pgbench -S -c ${i} -j 2 -l -T ${DURATION} -P 5 -h ${SERVER_DNS} -p ${SERVER_PORT} -U pgbench pgbench  2>&1 | tee ${f}

done
