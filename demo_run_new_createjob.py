from datetime import datetime
from autojenkins import Jenkins
import re

import os,sys
sys.path.extend(os.path.dirname(os.path.realpath(__file__)))
#http://www.cnblogs.com/huangcong/archive/2011/08/29/2158268.html


date_regexp = re.compile("(\d+-\d+-\d+)")

jobHash = {}





if __name__ == '__main__':
    j = Jenkins('http://135.251.224.94:8080/')
    jobs = j.all_jobs()
    print(jobs)

    for job, color in jobs:
        if color in ['red', 'blue', 'yellow']:
            full_info = j.job_info(job)
            last_build = j.last_build_info(job)
            when = datetime.fromtimestamp(last_build['timestamp'] / 1000)
        else:
            when = '(unknown)'
        print("{0!s:<19} {1:<6} {2}".format(when, color, job))

    #print "Build!"
    #j.build("CodeWarrior_Build_Test")
    #print "Waiting"
    #j.wait_for_build("CodeWarrior_Build_Test")
    #print "Result!"
    #j.last_build_info("CodeWarrior_Build_Test")
    #print "Create another"
    test = "YangSen"
    #j.create(test, "config.xml")
    #j.build(test)
    #j.wait_for_build(test)
    #j.last_build_info(test)
    """
    {'building': False, 
     'changeSet': {'items': [], 'kind': None}, 
     'builtOn': '135.251.224.97', 
     'description': None, 
     'artifacts': [], 
     'timestamp': 1406097476259L, 
     'number': 1, 
     'actions': [{'causes': [{'userName': 'anonymous', 'userId': None, 'shortDescription': 'Started by user anonymous'}]}], 
     'id': '2014-07-23_14-37-56', 
     'keepLog': False, 
     'url': 'http://135.251.224.94:8080/job/YangSen/1/', 
     'culprits': [], 
     'result': 'SUCCESS', 
     'executor': None, 
     'duration': 7020, 
     'fullDisplayName': 
     'YangSen #1', 
     'estimatedDuration': 7020}
    """
    print j.last_result(test)

    print "----------------------------------------------------------"

    k = Jenkins('http://172.24.186.185/')
    print k.last_result("LR_L1_PRACH_MT_FG4_L1A")



