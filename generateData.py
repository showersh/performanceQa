#!/usr/bin/env python
import uuid
import httplib2
import json
from random import Random

class generateData(object):
    """#genrate the data"""

    def __init__(self):

        self.task_name = ''
        self.task_length = 10
        self.concurrent_number = 1 

    def setCreateNetworkTaskName(self):
        self.task_name = "network_%s" % ( str(uuid.uuid1()))

    def random_str(self,randomlength=8):
        """ generate random arbitrary length string 
        """
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str+=chars[random.randint(0, length)]
        return str
    
    def generateNetworkTask(self, task_length=10, concurrent_number=1):
        """ genetate create Network task data
        """
        task_dict_list = []
        authen_token = ''
        result_dict = self.genetateToken()
        if result_dict['isOK'] :
            authen_token = result_dict['auth_token']
        else:
            print "fail generate authen tolen"
            return []

        for i in range(0, self.task_length):
            task_dict = {'process_id' : '',\
                         'task_name' : '',\
                         'network_name' : '',\
                         'status_code' : '',\
                         'latency_time' : '',\
                         'concurrent_number' : '',\
                         'auth_token' : '',\
            }
            task_dict['task_name'] = self.task_name
            task_dict['network_name'] = self.random_str()
            task_dict['concurrent_number'] = self.concurrent_number
            task_dict['auth_token'] = authen_token
            task_dict_list.append(task_dict)
        return task_dict_list

    def genetateToken(self):
        """login and   generate tolen 
        """
        try:
            result_dict = {'functionName':'generateToken',\
                         'delayTime':'',\
                           'auth_token': '',\
                       'isOK': False,\
                        'statusCode':''
                      }
            h = httplib2.Http()
            body = '{"auth":{"tenantName":"admin","passwordCredentials":{"username":"admin","password":"admin"}}}'
            resp, content = h.request("http://192.168.122.37:5000/v2.0/tokens","POST",body,headers={'Content-Type':'application/json'})
            #print type(content)
            if(int(resp.status) == 200):
            #print type(resp.status)
                return_valuse = json.loads(content)
                result_dict['auth_token'] = return_valuse['access']['token']['id']
                result_dict['isOK'] = True
        except Exception,e:
            print e
            result_dict['isOK'] = False
        finally:
            return result_dict
if __name__ == "__main__":
    object_network = generateData()
    object_network.setCreateNetworkTaskName()
    print object_network.generateNetworkTask()

