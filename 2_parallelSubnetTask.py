#!/usr/bin/env python
import httplib2
from multiprocessing import Lock, Process, Queue, current_process
from generateData import generateData 
from dataHandle import dataHandle
import json
import time
import random


def worker(work_queue, done_queue):
    try:
        for task_item in iter(work_queue.get,'STOP'):
            #print_task(task_item)
             
            task_dict = {'process_id' : '',\
                         'task_name' : '',\
                         'subnet_name' : '',\
                         'status_code' : 0,\
                         'latency_time' : '',\
                         'concurrent_number' : '',\
                         'auth_token' : '',\
                         'network_id' : ''
            }
            result_dict = createSubnet(task_item['auth_token'], task_item['network_id'])
            #print result_dict
            task_dict['process_id'] = current_process().name
            task_dict['task_name'] =  task_item['task_name']
            #task_dict['network_name'] =  task_item['network_name']
            task_dict['status_code'] = result_dict['status_code']
            task_dict['latency_time'] = result_dict['latency_time'] 
            #task_dict[''] =  
            #print "2222222222222222"
            #print task_dict.value()
            done_queue.put(task_dict)
            #done_queue.put("%s - %s got %s." % (current_process().name, task_item['task_name'], task_item['network_name'] ))
    except Exception, e:
        done_queue.put("%s failed on %s with: %s" % (current_process().name, task_item['task_name'], e.message))
    return True

def print_task(task_dict):
    print "the task name is %s" % (task_dict['task_name'])


def createNetwork(auth_token, network_name):
    """
    """
    try:
        result_dict = {'function_name':'generate_token',\
                     'latency_time':'',\
                     'is_ok': False,\
                    'status_code':''
                  }
        print auth_token
        h = httplib2.Http()
        body_dict = {"network":{"name":"","admin_state_up":"false"}}
        body_dict['network']['name'] = network_name
        body_str = json.dumps(body_dict)
        #print body_str
        #print type(body_str)
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
        result_dict['latency_time'] = str(end_time - start_time)
        result_dict['status_code'] = resp.status
        #print ((endtime - starttime).microseconds)
        #print resp
        #print content
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


def createSubnet(auth_token, network_id):
    """
    """
    try:
        result_dict = {'function_name':'generate_token',\
                     'latency_time':'',\
                     'is_ok': False,\
                    'status_code':''
                  }
        print auth_token
        h = httplib2.Http()
        request_body = {"subnet":{"network_id":"",\
                    "ip_version":4,\
                    "cidr":"",\
                    "allocation_pools":[]
                    }}
        request_body['subnet']['network_id'] = network_id
        ip2 = random.randint(2, 253)
        ip3 = random.randint(2, 253)
        #ip2 = 0
        #ip3 = 8
        cidr_str = "10.%s.%s.0/24" % (str(ip2), str(ip3))
        request_body['subnet']['cidr'] = cidr_str 
        allocation_pools_list = []
        allocation_pools = {'start':'',\
                            'end':''
                            }
        allocation_pools['start'] = "10.%s.%s.10" % (str(ip2),str(ip3)) 
        allocation_pools['end'] =  "10.%s.%s.150" % (str(ip2),str(ip3))
        allocation_pools_list.append(allocation_pools)
        request_body['subnet']['allocation_pools'] = allocation_pools_list
        body_str = json.dumps(request_body)
        #print request_body
        #print type(request_body)
        #print body_str
        headers = {'Content-Type':'application/json',\
                   'Accept':'application/json',\
                   'X-Auth-Token':''}
        headers['X-Auth-Token'] = auth_token
	    #starttime = datetime.datetime.now()
	    #start_time = time.clock()
        cidr_str = "10.%s.%s.0/24" % (str(ip2), str(ip3))
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
        #print request_body
        #print type(request_body)
        print body_str
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
        result_dict['latency_time'] = str(end_time - start_time)
        result_dict['status_code'] = int(resp.status)
        #print ((endtime - starttime).microseconds)
        #print resp
        #print content
        result_dict['is_ok'] = True
        #print "****************"
        #print result_dict
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


def main():
    
    network_list = [] 
    start_maint = time.time()
    workers = 10
    #workers = 1
    work_queue = Queue()
    done_queue = Queue()
    task_name_str = ''
    processes = []

    object_data = dataHandle() 
    object_network = generateData()
    object_network.setCreateSubnetTaskName()
    task_list = object_network.generateSubnetTask(1,1)
    if not task_list:
        print "fail create task list"
    else: 
        for task_item in task_list:
            work_queue.put(task_item)
    
        for w in xrange(workers):
            p = Process(target=worker, args=(work_queue, done_queue))
            p.start()
            processes.append(p)
            work_queue.put('STOP')
    
        for p in processes:
            p.join()
    
        done_queue.put('STOP')
         
        with open("perfromqaSubnet.log", 'a+') as f:
            for task_dict in iter(done_queue.get, 'STOP'):
                #print "=============="
                print task_dict
                #print type(task_dict[''])
                if( int(task_dict['status_code']) == 200 or int(task_dict['status_code']) == 201 ):

                    network_list.append(task_dict)
                    information =  "%s %s %s %s OK %s\r\n" % (task_dict['process_id'],\
                    task_dict['task_name'],\
                    task_dict['subnet_name'],\
                    task_dict['status_code'],\
                    task_dict['latency_time']) 
                else:
                    information =  "%s %s %s %s Bad %s\r\n" % (task_dict['process_id'],\
                    task_dict['task_name'],\
                    task_dict['network_id'],\
                    task_dict['status_code'],\
                    task_dict['latency_time']) 
                f.write(information) 
                task_name_str =  task_dict['task_name'] 
    end_maint = time.time()
    with open("perfromqaSubnet.log", 'a+') as f:
        information = 'the task %s spend %s seconds\r\n'  % (task_name_str,(end_maint - start_maint))
        f.write(information) 
            #print information

    object_data.dataSave(network_list)
if __name__ == "__main__":
    main()
