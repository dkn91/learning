'''This module is responsible for graphical representation of the change
   in as-path for each route. It plots a single origin AS and as-path
   conectivity for all the as-path a particular route has encountered.
   Additionally, it resolves the AS number from the CIDR website and
   displays the resolved AS name for each AS node in my graph. The
   module responsible for the resolve part for AS nos. or the reverse
   mapping from AS number to AS name is influenced from our homework
   #3 Ex14.6. I am using Networkx to plot graphs
'''

import cidras
import networkx as nx
import matplotlib.pyplot as plt
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

class plotme(object):
    '''This class computes the raw data provided from our main module
       and converts it to lists that would help me to plot them.
       Attributes: max_no_of_route_flaps_list, max_add_list, as_path_list
       Methods: prep_data(), as_path_prep_data() and as_path_plot()
    '''
    def prep_data(self, sme_dict):
        '''This method accepts dictionary as arguments and sorts top 10
           prefixes with maximum no. of routes. In case of less than 10
           prefixes available, it creates list for only those routes which
           have flapped.
        '''
        max_no_of_route_flaps_list = []
        self.max_add_list = []
        for i in range(len(sme_dict)):
            flap_temp = 0
            add_temp = ''
            for index in sme_dict:
                if sme_dict[index] >= flap_temp:
                    flap_temp = sme_dict[index]
                    add_temp = index
            if add_temp == '':
                break
            max_no_of_route_flaps_list.append(flap_temp)
            self.max_add_list.append(add_temp)
            del sme_dict[add_temp]        
        #print self.max_add_list
        #print max_no_of_route_flaps_list
        

    def as_path_prep_data(self, prefix, as_path_dict):
        '''Using the maximum prefixes from prep_data, this method fetches
           the as-path changes for that set of prefixes. This data is
           plotted using networkx and a gui module.
           Additionally it uses the 'cidras' module to resolve the AS name
           of the AS number and append them in the order of their
           occurring. In the end it calls the as_path_plot function and
           to plot the graph using networkx.
        '''
        mainlist = list()
        as_path_list = []
        print '\nGenerating your graph........Please wait'
        as_path_list.append(as_path_dict[prefix])

        for index,val in enumerate(as_path_list):
            for pointer,val2 in enumerate(val):
                if val2 == 0:
                    pass
                else:
                    temp = val2.split(' ')
                    temp2 = list()
                    for deepind in temp:
                        if deepind == '':
                            pass
                        else:
                            temp2.append(deepind)
                    temp3 = list()
                    for deeptemp in temp2:
                        temp3.append('AS#'+deeptemp+':'+cidras.fetch_zipage(deeptemp))
                    if temp3 != []:
                        
                        for smeind, smeval in enumerate(temp3):
                            if smeval == temp3[-1]:
                                temp3[-1] = 'OriginAS |'+temp3[-1]
                                break
                                
                            temp3[smeind] = smeval
                        mainlist.append(temp3)
        print 'AS Path history for '+prefix+' is as follows:\n'
        print '>>>'+temp3[-1]
        print '>>> "'+prefix+'" had total of '+str(len(mainlist))+' as-paths updates till now.'
        for index, path in enumerate(mainlist):
            print '\n>>>as-path#' + str(index)+': ', 
            for AS in path:
                print AS+'<--',
        
        self.as_path_plot(mainlist, prefix)
        
    def as_path_plot(self,as_path, prefix):
        '''This method accpets the list of as-path to plot for the
           selected prefix as per the GUI. It uses networkx module.
           The Nodes represent the AS and the edges represent the
           AS connectivity.
        '''
        G = nx.Graph()
        l= as_path

        for i,a in enumerate(l):
            #print a, type(a), len(a)
            G.add_node(a[-1])
            for i in xrange(len(a)):
                if i == len(a)-1:
                    break
                G.add_node(a[i])
                G.add_edge(a[i],a[i+1])

#        plt.title("draw_networkx")
        
 #       plt.savefig('abcd.png',dpi=500, facecolor='w', edgecolor='w',orientation='landscape', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.8)

        plt.title("AS Path for "+prefix)
        pos=nx.graphviz_layout(G,prog='dot')
        plt.figure(1,figsize=(10,8))
        #nx.draw_networkx(G,pos)
        nx.draw(G,pos,with_labels=True,arrows=True, font_size = 9,edge_color='r', node_color='b')
        plt.savefig(prefix+'_as_path.png',pad_inches = 0.8)
        
        plt.show()

'''dict1 = {'2001:67C:2710::': 0, '2001:1450::': 0, '2404:8000:72::': 0, '2600:2008::': 0, '2001:4848:209::': 0, '2620:101:402D::': 3, '2607:CC00:4::': 6, '2620:68::': 0, '2A00:5600::': 0, '2604:9E80::': 0, '2001:67C:18C::': 5, '2804:B44:E000::': 1, '2001:CD8::': 4, '2001:67C:11C4::': 2, '2404:138:40::': 0, '2001:502:4612::': 0, '2600:1014:B000::': 0, '2001:67C:2670::': 0, '2401:A000:124::': 0, '2001:1530::': 0, '2A00:1888::': 0, '2404:E400::': 0, '2407:7E00::': 0, '2001:67C:4C::': 10, '2607:FD50:6::': 0, '2001:DF0:46::': 0, '2801:0:60::': 0, '2400:4A00::': 0, '2604:1380::': 0, '2405:6400:2000::': 0, '2001:67C:2718::': 9, '2001:5B0:3D00::': 11, '2001:1458::': 0, '2A00:EC00::': 0, '2001:67C:2988::': 0, '2607:F2E0::': 0, '2600:200F::': 0, '2001:DF0:458::': 0, '2607:F568:4000::': 8, '2607:F4E0:200::': 12, '2400:3100::': 0, '2403:BA00:6FF::': 0}

dict2 = {'2001:67C:2710::': [' 30071 6939 12956 5610 25512 57823 '], '2001:1450::': [' 30071 3549 5602 '], '2404:8000:72::': [' 30071 17451 '], '2600:2008::': [' 30071 6453 33517 '], '2001:4848:209::': [' 30071 6939 31985 ', ' 30071 3356 31985 ', ' 30071 6939 31985 '], '2620:101:402D::': [' 30071 2914 16880 '], '2607:CC00:4::': [' 30071 6939 7385 13833 '], '2620:68::': [' 30071 3356 29906 '], '2A00:5600::': [' 30071 2914 31727 '], '2604:9E80::': [' 30071 6939 11260 30396 '], '2001:67C:18C::': [' 30071 6939 8641 47682 '], '2804:B44:E000::': [' 30071 16735 23456 ', ' 30071 104 23456 ' ], '2001:CD8::': [' 30071 6939 9264 4780 '], '2001:67C:11C4::': [' 30071 3257 34744 '], '2404:138:40::': [' 30071 6939 4637 9901 23655 38299 38299 38299 38299 '], '2001:502:4612::': [' 30071 12008 '], '2600:1014:B000::': [' 30071 1239 2828 6167 22394 22394 22394 22394 22394 '], '2001:67C:2670::': [' 30071 9009 39392 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 '], '2401:A000:124::': [' 30071 6939 17832 '], '2001:1530::': [' 30071 6667 2586 '], '2A00:1888::': [' 30071 2914 10021 50314 '], '2404:E400::': [' 30071 3549 18200 45345 '], '2407:7E00::': [' 30071 3491 56049 '], '2001:67C:4C::': [' 30071 1257 8437 3248 35609 '], '2607:FD50:6::': [' 30071 4436 40015 '], '2001:DF0:46::': [' 30071 4725 2907 24287 '], '2801:0:60::': [' 30071 3257 19169 27814 52274 '], '2400:4A00::': [' 30071 6453 38757 9341 '], '2604:1380::': [' 30071 6939 54825 '], '2405:6400:2000::': [' 30071 6453 23678 '], '2001:67C:2718::': [' 30071 3356 5400 25068 '], '2001:5B0:3D00::': [' 30071 1239 2828 6621 '], '2001:1458::': [' 30071 2914 8928 513 513 '], '2A00:EC00::': [' 30071 9002 16066 '], '2001:67C:2988::': [' 30071 6939 9121 58151 '], '2607:F2E0::': [' 30071 6939 36252 '], '2600:200F::': [' 30071 6939 33517 '], '2001:DF0:458::': [' 30071 6453 4755 18229 '], '2607:F568:4000::': [' 30071 6939 4323 11215 '], '2607:F4E0:200::': [' 30071 3356 4150 ', ' 30071 104 4150 '], '2400:3100::': [' 30071 4826 38456 45935 '], '2403:BA00:6FF::': [' 30071 6453 45147 24521 ']}

obj = plotme()
obj.prep_data(dict1)
obj.as_path_prep_data('2001:4848:209::',dict2)'''

'''([[' 30071 6453 39386 34426 ', ' 30071 6762 39386 34426 ', ' 30071 6453 39386 34426 ', 0, ' 30071 6453 39386 34426 '], [' 30071 3356 29119 58345 ', ' 30071 3257 29119 58345 ', ' 30071 3356 29119 58345 ', ' 30071 3257 29119 58345 ', ' 30071 3356 29119 58345 '], [' 30071 4436 33597 36236 55079 ', 0, ' 30071 4436 33597 36236 55079 '], [' 30071 6939 14572 ', 0, ' 30071 6939 14572 ']])'''
