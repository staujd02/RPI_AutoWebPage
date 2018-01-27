import subprocess
import logging
import time
import webbrowser
import psutil as util

# CONSTANT
MAX_ITER = 20
BROWSER_CLASS = "chromium-browser"
BROWSER_PROCESS = "chromium-browser"

def openWeb(url):

    logging.info("Launching default web browser...")

    # Open Browser
    try:
        webbrowser.open(url,0,True)
    except e as Exception:
        logging.error("Failed to launch browser: " + str(e))
        return
    

    # Fetch the number of instances matching chrome
    pid = fetchPIDcount()

    # Check if browser pid count was found
    if pid == -1:
        logging.error("Failed to establish web browser was launched")
        return

    # Check how many windows the browser has open
    b_count = -1
    attempts = 0
    gate = False

    # Let an error pass 10 times
    while attempts < 10 and gate == False:
        try:
            out = subprocess.check_output(["xdotool","search","--class",BROWSER_CLASS])
            b_count = len(out.splitlines())
            gate = True
            
        except:
            print "passing"
            attempts = attempts + 1

    # Kill execution if a browser number failed
    if gate == False:
        logging.error("Failed to establish a window count!")
        return
    else:
        # Give the browser a chance to wake up
        time.sleep(1)
        
    # Fullscreen window
    try:
        # Issue a raise, focus, and key F11 to last browser window
        logging.info("Launching browser number: " + str(b_count))
        subprocess.call(["xdotool","search","--class",BROWSER_CLASS,"windowraise","%" + str(b_count),"windowfocus","%" + str(b_count),"key","--window","key","--window","%" + str(b_count),"F11"])
        #subprocess.call(["xdotool","search","--class",BROWSER_CLASS,"windowraise","%4","windowfocus","%4","key","--window","key","--window","%4","F11"])

        # Move the mouse to bottom right corner
        subprocess.call(["xdotool","mousemove","10000","10000"])
    except e as Exception:
        logging.error("Browser interaction failed: " + str(e))
        

# Search running processes for a running chrome browser
def fetchPIDcount():

    # Func vars
    i = 0
    count = 0
    gate = False

    # Attempt to find process under MAX iterations
    while i < MAX_ITER:

        # Reset count
        count = 0
        
        # Check for running process
        for proc in util.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['name'])
            except util.NoSuchProcess:
                pass
            else:
                if BROWSER_PROCESS == pinfo['name']:
                    count = count + 1
                    if proc.status() == 'running':
                        gate = True
                    
        # Check the gate
        if gate:
            return count
        
        # No process was found; wait and then try again
        i = i + 1
        time.sleep(0.25)

    # END WHILE

    # No process was found, and iterations count was reached
    return -1
