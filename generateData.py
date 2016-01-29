#!/usr/bin/env python
import uuid
import httplib2
import json
from random import Random

class generateData(object):
    """#genrate the task list  data """

    def __init__(self):

        self.task_name = ''
        self.current_task_name = ''
        self.task_length = 100
        self.auth_token = ""
        self.network_task_list = []
        self.subnet_task_list = []
        self.port_task_list = []
        self.concurrent_number = 1 

    def setCreateNetworkTaskName(self):
        self.task_name = "network_%s" % ( str(uuid.uuid1()))

    def setCreateSubnetTaskName(self):
        self.task_name = "subnet_%s" % ( str(uuid.uuid1()))

    def setCreatePortTaskName(self):
        self.task_name = "port_%s" % ( str(uuid.uuid1()))

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

    def generateSubnetTask(self, task_length=10, concurrent_number=1):
        """ genetate create subnet task data
        """
        task_dict_list = []
        authen_token = ''
        #self.task_length = task_length
        result_dict = self.genetateToken()
        if result_dict['isOK'] :
            authen_token = result_dict['auth_token']
            network_name = self.random_str()
            result_dict1 = self.generateNetworkId(authen_token, network_name)
            if result_dict1['is_ok'] :
                self.network_id = result_dict1['network_id']
            else:
                print "fail generate network_id"
                return []
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
                         'network_id' : '',\
            }
            task_dict['task_name'] = self.task_name
            task_dict['network_name'] = self.random_str()
            task_dict['network_id'] = self.network_id
            task_dict['concurrent_number'] = self.concurrent_number
            task_dict['auth_token'] = authen_token
            task_dict_list.append(task_dict)
        return task_dict_list

    def generatePortTask(self, task_length=10, concurrent_number=1):
        """ genetate create Port task data
        """
        task_dict_list = []
        authen_token = ''
        #self.task_length = task_length
        result_dict = self.genetateToken()
        if result_dict['isOK'] :
            authen_token = result_dict['auth_token']
            network_name = self.random_str()
            result_dict1 = self.generateNetworkId(authen_token, network_name)
            if result_dict1['is_ok'] :
                self.network_id = result_dict1['network_id']
            else:
                print "fail generate network_id"
                return []
        else:
            print "fail generate authen tolen"
            return []

        for i in range(0, self.task_length):
            task_dict = {'process_id' : '',\
                         'task_name' : '',\
                         'port_name' : '',\
                         'status_code' : '',\
                         'latency_time' : '',\
                         'concurrent_number' : '',\
                         'auth_token' : '',\
                         'network_id' : '',\
            }
            task_dict['task_name'] = self.task_name
            task_dict['port_name'] = self.random_str()
            task_dict['concurrent_number'] = self.concurrent_number
            task_dict['auth_token'] = authen_token
            task_dict['network_id'] = self.network_id
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

    def generateNetworkId(self, auth_token, network_name):
        """generate a new network id  
        """
        try:
            result_dict = {'function_name':'generateNetworkId',\
                           'network_id':'',\
                           'network_name':'',\
                           'is_ok': False,\
                           'status_code':''
                          }
            #print auth_token
            h = httplib2.Http()
            body_dict = {"network":{"name":"","admin_state_up":"false"}}
            body_dict['network']['name'] = network_name
            body_str = json.dumps(body_dict)
            #print body_str
            #print type(body_str)
            headers = {'Content-Type':'application/json', 'X-Auth-Token':''} 
            headers['X-Auth-Token'] = auth_token
            resp, content = h.request('http://192.168.122.37:9696/v2.0/networks','POST',body_str,headers)
            result_dict['status_code'] = resp.status
            #print resp
            #print type(resp)
            #print content
            #print type(content)
            result_dict['is_ok'] = True
            if(int(resp.status) == 200 or int(resp.status) == 201 ):
                #print type(resp.status)
                return_value = json.loads(content)
                #print return_value
                result_dict['network_id'] = return_value['network']['id']
                result_dict['network_name'] = network_name
                result_dict['is_ok'] = True

        except Exception,e:
            print "fail generate network id"
            print e
        finally:
            return result_dict

if __name__ == "__main__":
    #object_network = generateData()
    #object_network.setCreateNetworkTaskName()
    #print object_network.generateNetworkTask()
    #object_subnet = generateData()
    #object_subnet.setCreateSubnetTaskName()
    #print object_subnet.generateSubnetTask(1,1)
    object_port = generateData()
    object_port.setCreatePortTaskName()
    print object_port.generatePortTask(1,1)
    
