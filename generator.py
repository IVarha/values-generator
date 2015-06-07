import ConfigParser
import json
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
  #parse_chunk(configs[0])
  return configs
  pass

def parse_chunk(config_section):
  parsed = []
  #sections
  inner_section = json.loads(config_section[0])
  tmp = []
  for a in inner_section :
    tmp+=inner_section[a]
  parsed.append(tmp)
  #aprices
  tmp = []
  inner_section = json.loads(config_section[1])
  #print(str(inner_section))
  for a in inner_section :
    tmp+=inner_section[a]
  parsed.append(tmp)
  tmp = []
  #apercs
  inner_section = json.loads(config_section[2])
  for a in inner_section :
    tmp+=inner_section[a]
  parsed.append(tmp)
  tmp = []
  #perc_bying
  inner_section = json.loads(config_section[3])
  for a in inner_section :
    tmp+=inner_section[a]
  parsed.append(tmp)
  #url_req
  parsed.append(long(config_section[4]))
  #days
  parsed.append(long(config_section[5]))
  return parsed


def generate_request(name,what_req,price,time):
  tmp = []
  tmp.append(name)
  if what_req == 1:
    tmp.append('buy')
  else :
    tmp.append('look')
  tmp.append(time)
  tmp.append(price)

  a = json.dumps(tmp)
  return a


  pass

def generate_time(requests,days):
  SECOUNDS = 86400
  num_chunks = days * SECOUNDS
  chunksize = requests // num_chunks
  tmp = (num_chunks - 1) * [chunksize]
  tmp += [requests % chunksize]
  return tmp


START_TIME = 0

def generate_data_chunk(ofile, parsed = None,start_time = 0):
  #generate array
  #print(parsed)
  #generate_array for data generation
  arr = []
  for a in xrange(0,len(parsed[3])):
    tmp=int(parsed[3][a])
    arr += tmp * [a]
  random.shuffle(arr)
  #generate data
  #print(arr)
  ## genetate_time
  time = generate_time(parsed[4],parsed[5])
  #print(time)
  for i in time:
    for j in xrange(0,i):
      posit = random.randint(0,99)
      #print(parsed[int(arr[posit])])
      what_request = np.random.binomial(1, parsed[3][arr[posit]]/100.0,1)
      #add time when done
      #print(parsed[0])
      data = generate_request(parsed[0][arr[posit]],what_request,parsed[1][arr[posit]], start_time + 1)
      ofile.write(data + '\n')
    start_time +=1
  pass

  #print(str(parsed))




def generate():
  sections = configs()
  parsed = []
  for x in sections :
    parsed.append(parse_chunk(x))

  f = open("myfile.txt",'w')
  time = 0
  for x in parsed:
    generate_data_chunk(f,x,time)
    #x[5] is  days
    time += 86400*x[5]
  #send_request("Iphone",1,512,0)
  #print(parsed)

  #print(str(sections))





    pass



if __name__ == "__main__" :
    generate()
