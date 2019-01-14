
#!/bin/bash

export PGCLIENTENCODING="UTF8"
DBLIST="$@"
echo ${DBLIST}
if [ -z "${DBLIST}" ]; then
  DBLIST="lab_erp"
fi
#backup directory
BACKUP=/home/peterdinh/Downloads/Project/data
ARCHNAME=`date +%Y%m%d-%H`

YEARMONTH=`date +%y%m`
TODAY=`date +%d`

mkdir -p ${BACKUP}/${YEARMONTH}/${TODAY}
for DBNAME in ${DBLIST} ; do
    BACKFILE=${DBNAME}.${ARCHNAME}.sql
    if [ -f ${BACKUP}/${YEARMONTH}/${TODAY}/${BACKFILE} ]; then
        continue
    fi
    pg_dump -U peterdinh  ${DBNAME} \
    > ${BACKUP}/${YEARMONTH}/${TODAY}/${BACKFILE}
done
