'''
    This program is to display traceroute via a world map.
'''
class Tracert(object):
    '''
       some text here
    '''
    def _init(self):
        self.destip = ''

    def tracert():
        '''
           Some Text here
        '''
        print('$'*60)

def main():
    print '$'*60
    print '\t\tLive IPv6 BGP Route Monitoring'
    print '$'*60
    obj = tracert()
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
