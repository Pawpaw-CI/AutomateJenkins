## Automate Jenkins Operations

```
Python scripts for automating jenkins operation: create/copy/delete/build jobs|folders, create/delete slave ...
```

## Reference
* http://pythonhosted.org/jenkinsapi/using_jenkinsapi.html
* http://pythonhosted.org/jenkinsapi/build.html
* https://github.com/pycontribs/jenkinsapi/blob/master/examples/how_to/query_a_build.py
* JenkinsAPI https://my.oschina.net/sanpeterguo/blog/197931

## Jenkins Plugin download
* http://updates.jenkins-ci.org/download/plugins/
* CloudBees Folders Plugin 5.3 - com.cloudbees.hudson.plugins.folder.Folder
* AnsiColor - https://wiki.jenkins-ci.org/display/JENKINS/AnsiColor+Plugin

## Slave Node Operation
* Config - http://XX.XX.XX.XX/computer/node1/config.xml 
* Delete - curl -X POST http://XX.XX.XX/computer/node1/doDelete\?json={}\&Submit=Yes
* 

## Slave Node Connected to Jenkins Master using JNLP (Java Web Start) in Docker Container
* https://github.com/carlossg/jenkins-slave-docker
* https://hub.docker.com/r/csanchez/jenkins-slave/
* https://hub.docker.com/r/jenkinsci/jnlp-slave/
```
wget http://XX.XX.XX.XX/jnlpJars/slave.jar
java -jar slave.jar -jnlpUrl -noReconnect  http://XX.XX.XX.XX/computer/node1/slave-agent.jnlp
```
  

## Dockerfile for Jenkins Setup
* https://github.com/larrycai/docker-images/blob/master/jenkins-demo1/Dockerfile
* https://github.com/blacklabelops/jenkins/blob/master/Dockerfile
* https://github.com/jenkinsci/docker
* http://www.open-open.com/lib/view/open1436922756240.html
* http://www.open-open.com/lib/view/open1415669219461.html


## curl automate jenkins
* https://my.oschina.net/sanpeterguo/blog/197931
* http://www.cnblogs.com/buaawp/p/5260996.html
```
*. delete a job
   curl -X POST http://localhost:8080/jenkins/job/jobfromcmd/doDelete

*. query job's status
   curl --silent ${JENKINS_SERVER}/job/JOB_NAME/lastBuild/api/json

*. get job's build number
   curl --silent ${JENKINS_SERVER}/job/JOB_NAME/lastBuild/buildNumber
   curl --silent ${JENKINS_SERVER}/job/JOB_NAME/lastStableBuild/buildNumber

*. create a job 
   curl -X POST http://localhost:8080/jenkins/createItem?name=jobfromcmd --user admin:admin --data-binary "@config.xml" -H "Content-Type: text/xml”
   curl --user ${UserName}:${PASSWORD} -o /dev/null --data disable JENKINS_URL/job/JOBNAME/disable
   curl --user ${UserName}:${PASSWORD} -o /dev/null --data disable JENKINS_URL/job/JOBNAME/enable

*. launch job build with parameter
   http://localhost:8080/jenkins/job/commandTest/buildWithParameters -d param1=value1&param2=value

```


## JAVA8/7/6 Download
* http://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html
* http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html
```
curl -s http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html | grep jdk | grep linux-x64.tar.gz | awk -F'"' '{print $(NF-1)}' | grep -v jre
```

* Add JAVA_HOME into PATH
```
export JAVA_HOME=/usr/java/jdk1.7.0_80
export CLASSPATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/jre/lib/rt.jar
source /etc/profile

```
