"""
    archive.py
    Archives old directories into a predefined dir within current dir
"""
# imports
import os
import datetime
# Parms
dir_path = '/home/sambuddha/Dungeon/Code/python/dirwatch/trgt/'
expir_days = 30
archive_dir = 'ARCHIVE'
# Timestamp
currtime = datetime.datetime.now()
# Main block START
# Scan through subdirs
entryItr = os.scandir(dir_path)
for iEntry in entryItr:
    print('DIR: ' + iEntry.name)
    if iEntry.name != archive_dir:
        modtime = datetime.datetime.fromtimestamp(iEntry.stat().st_mtime)
        dirAge = currtime - modtime
        # Check if older than expiration
        if dirAge.days > expir_days:
            # Copy directory and contents into archive_dir
        print('Dir "{}" last modified on {}; {} days old.'.format(iEntry.name, modtime.strftime('%d-%b-%Y %H:%M:%S'), dirAge.days))
    else:
        print('archive')
# Main block END
