from fabric.api import * 

env.hosts=['192.168.80.129','192.168.80.130']
env.user='l'
env.password='zhou5460'
env.roledefs={
	'server01':['192.168.80.129',],
	'server02':['192.168.80.130',],
}


def helloworld(who="world"):
	print "Hello {0}".format(who)

def helloworld1(you='world',me="ruiaplin"):
	print "Hello {0},i am {1}".format(you,me)
def runsomething(cmd='whoami'):
	result=run(cmd)
	result.failed
def localsomething(cmd="pwd"):	
	yy=local(cmd,capture=True)
	print(yy)
	print(yy.succeeded)
def getsomefile(remotepath='/etc/passwd',localpath='./getsomething'):
	get(remote_path=remotepath,local_path=localpath)

@roles('server01','server02')
def putsomefile(localpath='/etc/passwd',remotepath='./putsomething',mode=0644):
	put_check=put(local_path=localpath,remote_path=remotepath,mode=mode)
	print(put_check.succeeded)

