"""
    archive.py
    Archives old directories into a predefined dir within current dir
"""
# imports
import os, datetime, shutil
# Func Defs
def overcopy(from_path, to_path):
    """
        copies dir trees forcefully
    """
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
# Parms
dir_path = '/home/sambuddha/Dungeon/Code/python/github/dirwatch/trgt/'
expir_days = 120
archive_dir = 'ARCHIVE'
# Timestamp
currtime = datetime.datetime.now()
# Main block START
# Scan through subdirs
entryItr = os.scandir(dir_path)
for iEntry in entryItr:
    print('DIR: ' + iEntry.name)
    if iEntry.name != archive_dir:
        modtime = datetime.datetime.fromtimestamp(iEntry.stat().st_atime)
        dirAge = currtime - modtime
        # Check if older than expiration
        if dirAge.days > expir_days:
            try:
                # Copy directory and contents into archive_dir
                overcopy(iEntry.path, os.path.join(dir_path, archive_dir, iEntry.name))
                shutil.rmtree(iEntry.path)
            except Exception as ex:
                print('ERROR backing up dir \'{}\': {}'.format(iEntry.name, str(ex)))
        # print('Dir "{}" last modified on {}; {} days old.'.format(iEntry.name, modtime.strftime('%d-%b-%Y %H:%M:%S'), dirAge.days))
# Main block END
