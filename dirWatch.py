# v1: use of base file

# Modules
import os, time, glob, ctypes, datetime, json

# PARAMETERS
path_to_watch = "D:\\PRACTICE\\LAB_Python\\testDir"
msgbox_hdr = "COMMON_GRSE_FOLDER"
monitor_freq = 10
bFile = path_to_watch + "\\bdir"

while 1:
    # Baseline files
    try:
        before = json.load(open(bFile, 'r'))
    except (IOError, ValueError) as err:
        print(err)
        before = dict ([(f, None) for f in glob.glob (path_to_watch + "\\**", recursive=True)])
    
    # Get current time
    currtime = datetime.datetime.now()
    time.sleep (monitor_freq)
    after = dict ([(f, None) for f in glob.glob (path_to_watch + "\\**", recursive=True)])
    # Log file count to console
    print("[{}]: {:d} file(s).".format(currtime, len(after)))
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    # Populate message
    outMsg = ""
    if (added):
        outMsg = outMsg + "\nNEW FILE(s):\n" + "\n".join(added)
    if (removed):
        outMsg = outMsg + "\nDELETED FILE(s):\n" + "\n".join(removed)
    # Throw message for any change
    if (added or removed):
        ctypes.windll.user32.MessageBoxW(0, outMsg, msgbox_hdr, 0x1000)
        print("[{}]:\n {}".format(currtime, outMsg))
    else:
        print("[{}] No Change.".format(currtime))
    # Reset baseline for next iteration
    json.dump(after, open(bFile, 'w'))