import ConfigParser
import json
import kafka.producer
import numpy as np
import random
def configs():
  config = ConfigParser.RawConfigParser()
  config.read("tests.ini")
  configs = []
  for x in config._sections:
    elem = []
    #print(config._sections[x]['sections'])
    elem.append(config._sections[x]['sections'])
    elem.append(config._sections[x]['aprices'])
    elem.append(config._sections[x]['aperc'])
    elem.append(config._sections[x]['percentges_buing'])
    elem.append(config._sections[x]['urequests'])
    elem.append(config._sections[x]['days'])
    configs.append(elem)
  #print(str(configs))

  #print(str(config._sections["section1"]['sections']))
  #json.loads(config._sections["section1"]['sections'])
  parse_chunk(configs[0])
  return configs
  pass

def parse_chunk(config_section):
  parsed = []
  inner_section = json.loads(config_section[0])
  tmp = []
  for a in inner_section :
    tmp.append(inner_section[a])
  parsed.append(tmp)
  tmp = []
  inner_section = json.loads(config_section[1])
  print(str(inner_section))
  for a in inner_section :
    tmp.append(inner_section[a])
  parsed.append(tmp)
  tmp = []
  inner_section = json.loads(config_section[2])
  for a in inner_section :
    tmp.append(inner_section[a])
  parsed.append(tmp)
  tmp = []
  inner_section = json.loads(config_section[3])
  for a in inner_section :
    tmp.append(inner_section[a])
  parsed.append(tmp)
  parsed.append(long(config_section[4]))
  parsed.append(long(config_section[5]))
  return parsed


def send_request(name,what_req,price,time):
  pass

def generate_data(file_name='kafka.list', parsed = None ):
  #generate array
  for x in parsed:
    #generate_array for data generation
    arr = []
    for a in xrange(0,len(x[3])):
      tmp=int(x[3][a])
      arr += tmp * [a]
    random.shuffle(arr)
    #generate data
    for i in xrange(0, parsed[4]):
      posit = random.randint(0,99)
      what_request = np.random.binomial(1, int(x[2][posit])/100.0,1)
      #add time when done
      send_request(x[0][posit],what_request,x[1],0)



  pass

  #print(str(parsed))




def generate():
    sections = configs()
    #for x in

    #print(str(sections))





    pass



if __name__ == "__main__" :
    generate()
