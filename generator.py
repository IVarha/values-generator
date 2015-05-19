import ConfigParser
import json
import numpy as np
def configs():
    config = ConfigParser.RawConfigParser()
    config.read("tests.ini")
    for x in config._sections:
      print(str(x))

    print(str(config._sections["section1"]['sections']))
    json.loads(config._sections["section1"]['sections'])

    return config
    pass

def generate():
    print(str(configs()))





    pass



if __name__ == "__main__" :
    generate()
