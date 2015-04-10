'''This module is the center of this program with all the module imports
   and calling the methods inside each module. It starts by initializing
   the ssh conection and compare module and performs functions like sort
   and file creation.
'''

import os
import time
import compa
import ssh
import plotme
import gui


class analysis(object):
    '''This class performs the data separation part of the program.
       It accesses the 'ipv6logfile.txt' saved in the same working
       directory and filters out route destinations, route mask,
       route next-hop and as-path for that route. It then saves the
       filtered data in separate lists. It calls sort() method of
       this class to perform the sort function.
       Attributes: Securesh, plot
       Methods: constructor, sorting and sort
    '''
    def __init__(self):
        '''This special method acts as a constructor to this class.
           It gets called everytime an object of this class is created.
        '''
        self.Securesh=ssh.sshconnection('198.11.21.47',22,'root','gfer54efw')
        self.plot = plotme.plotme()

    def constructor(self):
        '''This user defined method acts as an constructor. It needs an
           explicit call. It provides empty lists to save the parameters
           after sorting.
        '''
        self.routedest = []
        self.routemask = []
        self.next_hop = []
        self.as_path = []
        self.data = ''

    def sorting(self):
        '''This method performs the sorting process.
           It filters route prefixes, route mask, route next-hop
           and as-path segment for each route and generates four files:
           rmask.txt, rdest, next_hop, and as-path.txt. Initial 7 lines 
           are skipped before process starts as they are unwanted data.
           I am only looking for route and route details.
        '''
        self.logfile = open('ipv6logfile.txt', 'ro')
        for i in range(7): 
            self.data = self.logfile.readline()    
        while True:
            if self.data.startswith('*'):#Looking for route prefix
                self.sort()
                self.data = self.logfile.readline()
                if self.data.startswith('*') is False:#Looking for Next-hop
                    self.sort()
                    self.data = self.logfile.readline()#Looking for AS-path
                    if self.data.startswith('*') is False:
                        self.sort()
                else:
                    break
            else:
                self.data = self.logfile.readline()
            if self.data == '':
                break
        self.file_write(self.routedest, 'route_dest.txt')
        self.file_write(self.routemask, 'route_mask.txt')
        self.file_write(self.as_path, 'as_path.txt')
        self.file_write(self.next_hop, 'next_hop.txt')


    def sort(self):
        '''This method performs sorting for a route entry and returns
           parameter specific values like route prefix, route mask,
           next-hop and as-path and saves it as separate files
           for each route entry.
        '''
        temp = ''
        temp2 = ''
        temp3 = ''
        temp4 = []
        flag = 0
        self.temp_list = self.data.split(' ')
        for index in self.temp_list:
            if flag == 1:
                if len(index) != 0:
                    flag = 0
            else:

                if len(index) != 0:
                    if '/' in index:
                        temp = index.split('/')
                        self.routedest.append(temp[0])                
                        temp=temp[1].split('\n')[0]
                        self.routemask.append(temp[:2])
                    elif ':' in index:
                        self.next_hop.append(index)
                        flag = 1
                    elif index != '0':
                        if index.find('*>') == -1:
                            if index.startswith('i') is False:
                                temp2 = temp2 + ' '+ index
                            elif index.startswith('?') is False:
                                temp2 = temp2 + ' ' + index
            if temp2 != '':
                temp3 = temp2.split('I')
                temp4.append(temp3[0])
                p = temp4[-1].find(' 30071')
                if index.find('i') != -1 or index.find('?') != -1 or index.find('e') != -1:
                    temp4 = temp4[-1][p:].split('?')
                    temp4 = temp4[0].split('i')
                    temp4 = temp4[0].split('e')
                    self.as_path.append(temp4[0])   

            if self.data == '':
                break
            

    def file_write(self, list_var,var):
        '''This method takes two arguments: a list and a string.
           It saves the entire list in a file with the provided
           string as the name of the file.
        '''
        file_create = open(var, 'w')
        for index in list_var:
            if index.find('\n') != -1:
                file_create.write(index)
            else:
                file_create.write(index+'\n')
        file_create.close()

    def data_merger(self):
        self.latest = dict()
        for index,val in enumerate(self.routedest):
            self.latest[val] = [self.routemask[index]]
            self.latest[val].append(self.as_path[index])
        return self.latest


    def __str__(self):
        '''This special method is called everytime a print or a str()
           uses the object of this class as its arguments.
        '''
        return str(self.routedest, self.routemask, self.next_hop, self.as_path)


def main():
    print '$'*60
    print '\t\tLive IPv6 BGP Route Monitoring'
    print '$'*60
    obj = analysis()
    obj.comp = compa.compare_module()
    count = 0
    while True:
        count += 1
        print 'Iteration #'+str(count)
        obj.constructor()
        obj.Securesh.ssh_connection_open()
        obj.sorting()
        obj.dict1 = obj.data_merger()
        obj.comp.compare_me(obj.dict1)
        print 'time to sleep for 30s'
        #time.sleep (5)
        print '*'*20
        
        if count == 15:
            break

    obj.plot.prep_data(obj.comp.Total_flaps)
    gui.gui_main(obj.plot.max_add_list, obj.comp.Aspath_change)


if __name__ == '__main__':
    main()
