#!/usr/bin/env python
import uuid
from random import Random

class generateData(object):
    """#genrate the data"""

    def __init__(self):

        self.task_name = ''
        self.task_length = 3
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

        for i in range(0, self.task_length):
            task_dict = {'process_id' : '',\
                         'task_name' : '',\
                         'network_name' : '',\
                         'status_code' : '',\
                         'latency_time' : '',\
                         'concurrent_number' : '',\
            }
            task_dict['task_name'] = self.task_name
            task_dict['network_name'] = self.random_str()
            task_dict['concurrent_number'] = self.concurrent_number
            task_dict_list.append(task_dict)
        return task_dict_list

if __name__ == "__main__":
    object_network = generateData()
    object_network.setCreateNetworkTaskName()
    print object_network.generateNetworkTask()
