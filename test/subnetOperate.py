#!/usr/bin/env python
# coding=utf-8
import httplib2
import json
import time
import datetime
import uuid
from random import Random
import random


def genetateToken():
    """
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

def createNetwork(auth_token, network_name):
    """
    """
    try:
        result_dict = {'function_name':'generate_token',\
                     'letency_time':'',\
                     'is_ok': False,\
                    'status_code':''
                  }
        print auth_token
        h = httplib2.Http()
        body_dict = {"network":{"name":"","admin_state_up":"false"}}
        body_dict['network']['name'] = network_name
        body_str = json.dumps(body_dict)
        print body_str
        print type(body_str)
        headers = {'Content-Type':'application/json', 'X-Auth-Token':''} 
        headers['X-Auth-Token'] = auth_token
	#starttime = datetime.datetime.now()
	#start_time = time.clock()
	start_time = time.time()
	#long running

        resp, content = h.request("http://192.168.122.37:9696/v2.0/networks","POST",body_str,headers)
	#endtime = datetime.datetime.now()
	#end_time = time.clock()
	end_time = time.time()
	#print type(endtime - starttime)
	#result_dict['letency_time'] = str((end_time - start_time).mico)
	result_dict['letency_time'] = str(end_time - start_time)
        result_dict['status_code'] = resp.status
        #print ((endtime - starttime).microseconds)
        print resp
        print content
        result_dict['is_ok'] = True
        #if(int(resp.status) == 200):
        ##print type(resp.status)
        #    return_valuse = json.loads(content)
        #    result_dict['auth_token'] = return_valuse['access']['token']['id']
        #    result_dict['isOK'] = True
    except Exception,e:
        print e
    finally:
        return result_dict

def createSubnet(auth_token, network_id):
    """
    """
    try:
        result_dict = {'function_name':'generate_token',\
                     'letency_time':'',\
                     'is_ok': False,\
                    'status_code':''
                  }
        print auth_token
        h = httplib2.Http()
        request_body = {"subnet":{"network_id":"",\
                    "ip_version":4,\
                    "cidr":"",\
                    "allocation_pools":[],\
                    }}
        request_body['subnet']['network_id'] = network_id
        ip2 = random.randint(2, 253)
        ip3 = random.randint(2, 253)
        cidr_str = "10.%s.%s.0" % (str(ip2), str(ip3))
        request_body['cidr'] = cidr_str 
        allocation_pools_list = []
        allocation_pools = {'start':'',\
                            'end':''
                            }
        allocation_pools['start'] = "10.%s.%s.10" % (str(ip2),str(ip3)) 
        allocation_pools['end'] =  "10.%s.%s.240" % (str(ip2),str(ip3))
        allocation_pools_list.append(allocation_pools)
        request_body['allocation_pools'] = allocation_pools_list
        body_str = json.dumps(request_body)
        print request_body
        print type(request_body)
        headers = {'Content-Type':'application/json',\
                   'Accept':'application/json',\
                   'X-Auth-Token':''}
        headers['X-Auth-Token'] = auth_token
	    #starttime = datetime.datetime.now()
	    #start_time = time.clock()
        start_time = time.time()
	    #long running
        resp, content = h.request("http://192.168.122.37:9696/v2.0/subnets","POST",body_str,headers)
	    #endtime = datetime.datetime.now()
	    #end_time = time.clock()
        end_time = time.time()
	    #print type(endtime - starttime)
	    #result_dict['letency_time'] = str((end_time - start_time).mico)
        result_dict['letency_time'] = str(end_time - start_time)
        result_dict['status_code'] = resp.status
        #print ((endtime - starttime).microseconds)
        print resp
        print content
        result_dict['is_ok'] = True
        #if(int(resp.status) == 200):
        ##print type(resp.status)
        #    return_valuse = json.loads(content)
        #    result_dict['auth_token'] = return_valuse['access']['token']['id']
        #    result_dict['isOK'] = True
    except Exception,e:
        print e
        result_dict['is_ok'] = False
    finally:
        return result_dict

def createPort(auth_token, network_id):
    """
    """
    try:
        result_dict = {'function_name':'generate_token',\
                     'letency_time':'',\
                     'is_ok': False,\
                    'status_code':''
                  }
        print auth_token
        h = httplib2.Http()
        request_body = {"port":{"admin_state_up":True,"name":"", "network_id":""}}
        port_name = "port%s"  % ( str(uuid.uuid1())) 
        request_body['port']['name'] = port_name
        request_body['port']['network_id'] = network_id
        body_str = json.dumps(request_body)
        print body_str
        print type(body_str)
        headers = {'Content-Type':'application/json',\
                   'Accept':'application/json',\
                   'X-Auth-Token':''}
        headers['X-Auth-Token'] = auth_token
	    #starttime = datetime.datetime.now()
	    #start_time = time.clock()
        start_time = time.time()
	    #long running

        resp, content = h.request("http://192.168.122.37:9696/v2.0/ports","POST",body_str,headers)
	    #endtime = datetime.datetime.now()
	    #end_time = time.clock()
        end_time = time.time()
	    #print type(endtime - starttime)
	    #result_dict['letency_time'] = str((end_time - start_time).mico)
        result_dict['letency_time'] = str(end_time - start_time)
        result_dict['status_code'] = resp.status
        #print ((endtime - starttime).microseconds)
        print resp
        print content
        result_dict['is_ok'] = True
        #if(int(resp.status) == 200):
        ##print type(resp.status)
        #    return_valuse = json.loads(content)
        #    result_dict['auth_token'] = return_valuse['access']['token']['id']
        #    result_dict['isOK'] = True
    except Exception,e:
        print e
        result_dict['is_ok'] = False
    finally:
        return result_dict

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


if __name__== "__main__":
    print "the start time is %s " % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
    start_maint = time.time()
    result_dict = genetateToken()
    #print result_dict
    #print #createNetwork(result_dict['auth_token'],'test2')
    if result_dict['isOK'] :
        task_name = uuid.uuid1()
        for i in range(0,10):
            #time.sleep(1)
            network_name = random_str(8)
            result_dict2 = createNetwork(result_dict['auth_token'],network_name)
            with open("perfromqa.txt", 'a+') as f:
                if( int(result_dict2['status_code']) == 201 or int(result_dict2['status_code']) == 201 ):
                    information = '%s %s %s OK %s seconds\r\n' % (task_name,network_name, result_dict2['status_code'],result_dict2['letency_time'])
                    #print information
                else:
                   
                   information = '%s %s %s BAD %s seconds\r\n' % (task_name,network_name, result_dict2['status_code'],result_dict2['letency_time'])    
                   print information
                f.write(information)
        end_maint = time.time()
        with open("perfromqa.txt", 'a+') as f:
            information = 'the task %s spend %s seconds\r\n' % (task_name,(end_maint - start_maint))
            #print information
            f.write(information)

    print "the end time is %s " % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))

