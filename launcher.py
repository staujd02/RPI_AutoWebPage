#!/usr/bin/env python

import Tkinter
import logging
import interface

# Log File
LOG_FILE = "webdisplay.log"

# Set Logging Info
logging.basicConfig(filename=LOG_FILE,level=logging.INFO)

# Load GUI
root = Tkinter.Tk()
root.wm_title('Web Display')
app = interface.WebInterface(root)
root.mainloop()
