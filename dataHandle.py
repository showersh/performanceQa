#!/usr/bin/env python

class dataHandle(object):

    def __init__(self):

        self.max = 0.0
        self.min = 0.0
        self.avg = 0.0
        self.task_name = ""

    def dataSave(self, task_list):
        
        latency_list = []
        for task in task_list:
            latency_list.append(float(task['latency_time']))
            self.task_name = task['task_name']
        self.max = max(latency_list)
        self.min = min(latency_list)
        self.avg = sum(latency_list)/len(latency_list)
        filename = "./result/%s_result" % (self.task_name)
        with open(filename, 'a+') as f:
            information = "%s %s %s\r\n" % (self.max, self.min, self.avg)
            f.write(information)
        
        filename = "./result/%s_source" % (self.task_name)
        with open(filename, 'a+') as f:
            for latency in latency_list:
                information = "%s\r\n" % (latency)
                f.write(information)
