import logging
import webbrowser
import configIO
import Tkinter
import web_ini


class WebInterface:

    # File Constants
    CONFIG_FILE = "web.conf"

    # Global Configuration Dictonary
    config = {}

    def __init__(self, master):

        # Create Globals
        self.url = Tkinter.StringVar()
        self.auto = Tkinter.IntVar()
        self.window = master

        # Create GUI, and add master frame
        frame = Tkinter.Frame(master)
        frame.pack()

        # Load configurations
        config_default = {"autostart":"1","url":"https://earth.nullschool.net/"}
        self.config = configIO.openConfig(config_default, self.CONFIG_FILE)

        # Create Label
        Tkinter.Label(frame, text="URL:").grid(row=1, column=1)
        # Label Spacers
        Tkinter.Label(frame, text="").grid(row=0, column=0, rowspan=5, ipadx=10)
        Tkinter.Label(frame, text="").grid(row=0, column=5, rowspan=5, ipadx=10)
        Tkinter.Label(frame, text="").grid(row=3, column=1, columnspan=4, pady=5)
        Tkinter.Label(frame, text="").grid(row=5, column=2,padx=150)

        # Create Buttons
        Tkinter.Button(frame, text="Exit", command=self.close).grid(row=5, column=1)
        Tkinter.Button(frame, text="Save", command=self.save).grid(row=5, column=3, pady=10, padx=5)
        Tkinter.Button(frame, text="Launch", command=self.launch).grid(row=5, column=4, pady=10)

        # Create Textbox
        Tkinter.Entry(frame, textvariable=self.url).grid(row=1,columnspan=3,column=2,pady=10,sticky=Tkinter.W+Tkinter.E)

        # Create Checkbox
        Tkinter.Checkbutton(frame, text="Auto-Start", variable=self.auto).grid(row=2,columnspan=2,column=2,sticky=Tkinter.W)

        # Populate fields
        self.url.set(self.config["url"])
        self.auto.set(self.config["autostart"])
        
        # Check if autostart is enabled
        if self.config["autostart"] == "1":
            self.launch()

    def save(self):
        self.config["url"] = self.url.get()
        self.config["autostart"] = self.auto.get()
        configIO.writeConf(self.config, self.CONFIG_FILE)

    def close(self):
        exit()

    def launch(self):
        logging.info("Launching " + self.config["url"])
        self.save()
        web_ini.openWeb(self.config["url"])
        self.window.iconify()
