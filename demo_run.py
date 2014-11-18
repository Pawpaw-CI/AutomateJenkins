from datetime import datetime
from autojenkins import Jenkins
import re

#http://www.cnblogs.com/huangcong/archive/2011/08/29/2158268.html


date_regexp = re.compile("(\d+-\d+-\d+)")

jobHash = {}





if __name__ == '__main__':
    j = Jenkins('http://172.24.186.185:8081')
    jobs = j.all_jobs()
    #print(jobs)
    for myjob in jobs:
        print myjob

    for jobname, jobstatus in jobs:
        dateflag = date_regexp.search(jobname)
        if dateflag:
            datestamp = dateflag.groups()[0]
            #print "Jobname=%-90s Date=%-20s Status=%-10s" % ( jobname, datestamp, jobstatus )
            if jobHash.has_key(datestamp):
                jobHash[datestamp].append(jobname)
            else:
                jobHash[datestamp] = []
                jobHash[datestamp].append(jobname)

    for key in  sorted(jobHash.keys()):
        if cmp(key, "2014-11-08") == 1:
            continue
        print "Date=%-20s " % key
        for job in jobHash[key]:
            print "          %s" % job
            print j.job_url( job )
            j.delete( job )



    print "Size=",len(jobs)


    '''
    for job, color in jobs:
        if color in ['red', 'blue', 'yellow']:
            full_info = j.job_info(job)
            last_build = j.last_build_info(job)
            when = datetime.fromtimestamp(last_build['timestamp'] / 1000)
        else:
            when = '(unknown)'
        print("{0!s:<19} {1:<6} {2}".format(when, color, job))
    '''
