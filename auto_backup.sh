#!/bin/bash

BACKUP_DIR = '/home/peterdinh/Downloads/Project'
if [ $DAY_OF_MONTH -eq 1 ];
then
	# Delete all expired monthly directories
	find $BACKUP_DIR -maxdepth 1 -name "*.sh" -exec rm -rf '{}' ';'
 
	perform_backups "-monthly"
 
	exit 0;
fi
