"""
    archive.py
    Archives old directories into a predefined dir within current dir
"""

# Parms
dir_path = '\\\\192.168.33.3\\testDirWatch'
expir_days = 30
archive_dir = 'ARCHIVE'

# imports
import os, datetime, shutil

# Func Defs
def overmove(from_path, to_path):
    """
        copies files and dir trees gracefully without overwriting previous files
    """
    # print('        In FUNC overcopy.')
    if os.path.exists(to_path):
        print('        Path exists: {}'.format(to_path))
        fpath, fname = os.path.split(to_path)
        # Append timestamp to target path
        tstamp = str(datetime.date.today())
        if os.path.isdir(from_path):
            to_path = os.path.join(fpath, '{}_{}'.format(fname, tstamp))
        else:
            fnames = fname.split('.')
            to_path = os.path.join(fpath, '{}_{}.{}'.format(fnames[0], tstamp, fnames[1]))
    try:
        if os.path.isdir(from_path):
            # Copy and del src dir
            shutil.copytree(from_path, to_path)
            shutil.rmtree(from_path)
        else:
            # Copy and del src file
            shutil.copy2(from_path, to_path)
            os.remove(from_path)
    except Exception as ex:
        print('        ERROR Copying File/Tree: \'{}\' to \'{}\': {}'.format(from_path, to_path, str(ex)))
        raise IOError('Tree Copy Error in func overcopy.')
    # print('        Copied tree to "{}". Exiting.'.format(to_path))

# Main block START
# Timestamp
currtime = datetime.datetime.now()
# Scan through subdirs
entryItr = os.scandir(dir_path)
for iEntry in entryItr:
    print('File/Dir: ' + iEntry.name)
    if iEntry.name != archive_dir:
        modtime = datetime.datetime.fromtimestamp(iEntry.stat().st_mtime)
        dirAge = currtime - modtime
        print('    Last modified on {}; {} days old.'.format(modtime.strftime('%d-%b-%Y %H:%M:%S'), dirAge.days))
        # Check if older than expiration
        # if dirAge.seconds > expir_days:
        if dirAge.days > expir_days:
            print('    Attempting archiving.')
            try:
                # Copy directory and contents into archive_dir
                overmove(iEntry.path, os.path.join(dir_path, archive_dir, iEntry.name))
                print('    Moved.')
            except Exception as ex:
                print('    ERROR moving entry \'{}\': {}'.format(iEntry.name, str(ex)))
# Main block END
