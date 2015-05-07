'''This module establishes a secure shell connection to the IPv6 internet
router (198.11.21.47). It fetches the IPv6 internet table and saves
the entire log in a file named "ipv6logfile.txt"
'''
import sys
import paramiko

class sshconnection(object):
    '''This class performs ssh activities. It establishes the ssh
       connection with 198.11.21.47 router that is directly connected
       to AS 30071 that is advertising all IPv6 BGP routes from the
       internet.
       Attributes: ip, port, username, password
       Methods: __init__, ssh_connection_open
    '''
    def __init__(self, ip="", port="", username="",password=""):
        '''This special method acts as a constructor. It assigns
           attributes with user passed variables.
        '''
        print "SSH connection state.....Ready"
        self.ip=ip
        self.port=port
        self.username=username
        self.password=password

    def ssh_connection_open(self):
        '''This method opens and ssh connection using paramiko package and
           user passed variables. 
           >>>  ssh_connect=paramiko.SSHClient()
           It executes 'show bgp ipv6 unicast'
           command and saves the stdout data in a text file with name
           ipv6logfile.txt
        '''
        print "Attempting an SSH connection"
        output=""
        ssh_connect=paramiko.SSHClient()
        ssh_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connect.connect(self.ip,self.port,self.username,self.password)
        print "SSH Connection.....Successful"
        stdin,stdout,stderr=ssh_connect.exec_command("sh bgp ipv6 unicast")
        print "Attempting an SSH connection Termination."
        logfile=open('ipv6logfile.txt','w')        
        for eachline in stdout:
            logfile.write(eachline)
        logfile.close()
        ssh_connect.close()
        print 'SSH connection Termination.....Successful'

def main():
    con1=sshconnection('username', 22, 'root', 'password')
    print con1.ip, con1.port
    con1.ssh_connection_open()

#main()
