#!/usr/bin/python
#coding:utf-8
#Author: Yang Sen


import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import optparse
import os, sys, time
import xml.dom.minidom
job_config_template    = os.path.join(os.path.dirname(os.path.realpath(__file__)), "jon_config_template.xml")



def get_plugin_details(server):
    for plugin in server.get_plugins().values():
        print "-"*10
        print "Short Name:%s" %(plugin.shortName)
        print "Long Name:%s" %(plugin.longName)
        print "Version:%s" %(plugin.version)
        print "URL:%s" %(plugin.url)
        print "Active:%s" %(plugin.active)
        print "Enabled:%s" %(plugin.enabled)


def create_folder():
    ###instsall plugins:　CloudBees Folders Plugin, https://wiki.jenkins-ci.org/display/JENKINS/CloudBees+Folders+Plugin
    #http://updates.jenkins-ci.org/latest/cloudbees-folder.hpi
    #
    pass


def create_job(jenkinshandle, jobname="mytest", jobxmlconfig="jon_config_template.xml"):
    xmlhandle=xml.dom.minidom.parse(job_config_template)
    commands = xmlhandle.documentElement.getElementsByTagName('command')
    #commands[0].childNodes[0].nodeValue = "uname -a;ifconfig;whoami;"
    custom_configxml_content = xmlhandle.toxml('UTF-8')

    #print(custom_configxml_content)
    job = jenkinshandle.create_job(jobname=jobname, xml=custom_configxml_content)
    my_job = jenkinshandle[jobname]
    print(my_job)
    # jenkinshandle.delete_job(jobname)

def install_plugin():
    #curl -X POST -H "Content-Type: multipart/form-data; boundary=---------------------------7e013a3050ad8" http://10.253.6.128:9999/pluginManager/uploadPlugin  -F "filename=@build-timestamp.hpi;type=application/x-zip-compressed"
    pass




if __name__ == '__main__':
    option_parser = optparse.OptionParser()
    option_parser.add_option('-v','--view',       dest="clearcaseview", default='', help="ClearCase Linux View")
    option_parser.add_option('-p','--project'  ,  dest="project"      , default='SoC'  , help="")
    option_parser.add_option('-f','--frametype',  dest="frameType"    , default='TDD'  , help="")
    option_parser.add_option('-c','--csls'      ,  dest="csls"        , default='senya', help="")
    options, args = option_parser.parse_args()
    
    #Jenkins(jenkins_url, username = 'foouser', password = 'foopassword')
    j = Jenkins('http://10.253.6.128:9999')
    print "============================="
    print j.version
    for k,v in j.get_jobs():
        print k,v
    for i in j.get_jobs():
        job_instance = j.get_job(i[0])
        #print dir(job_instance)
        print 'Job Name:%s' %(job_instance.name)
        print 'Job Description:%s' %(job_instance.get_description())
        print 'Is Job running:%s' %(job_instance.is_running())
        print 'Is Job enabled:%s' %(job_instance.is_enabled())

    print "============================="
    #print j.poll(tree='jobs[name,color,url]')
    print j.get_folders()

    create_job(jenkinshandle=j, jobname="senyang", jobxmlconfig="jon_config_template.xml")
    j.build_job(jobname="senyang")


    # time.sleep(10)
    #update config.xml
    xmlhandle=xml.dom.minidom.parse(job_config_template)
    commands = xmlhandle.documentElement.getElementsByTagName('command')
    commands[0].childNodes[0].nodeValue = "uname -a;df -h;"
    custom_configxml_content = xmlhandle.toxml('UTF-8')


    # j.create_job(jobname="senyang", xml=custom_configxml_content)
    # j.build_job(jobname="senyang")


    print j.get_job("senyang").get_last_build()


    #copy job

    for i in range(5):
        newjob = "longrun_%d" % i
        print j.copy_job("longrun", newjob)
        print j.build_job(newjob)



    #---------------------------------------------------------------------------
    # !!!!!! create slave node using JNLP (java web start) !!!!!!
    # slave connection command:
    #     >yum install -y wget curl screen; 
    #     >wget http://******:9999/jnlpJars/slave.jar ; 
    #     >screen java -jar slave.jar -noReconnect -jnlpUrl http://*****:9999/computer/${slave_node_name}/slave-agent.jnlp
    #---------------------------------------------------------------------------

    # print j.create_node(name="slave41", num_executors=2, node_description="docker container node", remote_fs='/var/lib/jenkins', labels="testing webui", exclusive=False)
    # print j.create_node(name="slave42", num_executors=2, node_description="docker container node", remote_fs='/var/lib/jenkins', labels="testing webui", exclusive=True)
    # print j.create_node(name="slave43", num_executors=2, node_description="docker container node", remote_fs='/var/lib/jenkins1', labels="testing webui", exclusive=False)
    # #print j.requester.post_xml_and_confirm_status(url="http://10.253.6.128:9999/job/foo_job2/config.xml", data=custom_configxml_content)

    time.sleep(3)
    #j.safe_restart()
    #print j.delete_node("slave41")

    # print j.create_folder("xxwfwgfg43g34455111111112211111")

    # k = Jenkins("http://10.253.6.128:9999/job/xxwfwgfg43g34455111111112211111/")
    # k.create_folder("xxxxx")

    # time.sleep(5)
    # print j.delete_folder("xxwfwgfg43g34455111111112211111")
    # print j.delete_folder("HAHAfolder1111111")
    # print j.delete_folder("HAHAfolder2222")
    # print j.delete_folder("folderdesc")
    # print j.delete_folder("HAHAfolder")

    #get_plugin_details(j)

    # try:
    #    j.create(options.clearcaseview, job_config_template)
    # except e:
    #    print e
    
