import logging

def openConfig(defaultDict, file):

        # Whether the config file has to be restored from defaults
        restore = False

        # Dictonary to return
        configs = defaultDict
        imports = {}
       
        # Read config file for key/value pairs
        try:
            logging.info("Loading config file...")
            f = open(file,'r')
            lines = f.read().splitlines()
            f.close()
            for setting in lines:
                s = setting.split('=',1)

                if len(s) > 1:
                    imports[s[0]] = s[1]
                else:
                     imports[s[0]] = ""

            # Combine lists
            configs.update(imports)
            
        except Exception as e:
            logging.error('Failed to read ini file: ' + str(e))
            restore = True
        
        # Re-create config if neccessary
        if restore == True:
            logging.info("Re-generating config file with defaults")
            writeConf(configs, file)
        
        # Return configuration dictonary
        return configs

def writeConf(defs, file):
    try:
        logging.info('Writing to config file...')

        f = open(file,'w')

        for key in defs:
              f.write(key + '=' + str(defs[key]) + '\n')
        
        f.close()
    except Exception as e:
        logging.error('Failed to regenerate config file! Error: ' + str(e))

