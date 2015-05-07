'''This module performs one of the most critical analysis of the program.
   It compares last fetched route with the latest one and focuses on
   mask changes, as-path changes and no. of times the route flap
   occurrences.
'''


class compare_module(object):
    '''This class represents the compare part of this program. It
       performs the most critical part of the program.
       It uses the recently fetched data and compares it with the last
       fetched log. Tracks changes for three specific route conditions
       which can cause the internet table to be unstable.
       Attributes: Last_table, Recent_table, Mask_change, Aspath_change
       and Total_flaps
       Methods: __init__(), compare_me()
    '''
    def __init__(self, Last_table=dict(), Recent_table=dict()):
        '''This special method is called everytime an object of this class
           is created.
        '''
        self.Last_table = Last_table
        self.Recent_table = Recent_table
        self.Mask_change = dict()
        self.Aspath_change = dict()
        self.Total_flaps = dict()
        self.ORIGINAS = 0

    def compare_me(self, Recent_table):
        '''This method tracks the changes in the IPv6 routing table by
           performing route by route comparison for each entry. It
           captures any changes and stores them in a dictionary file.
           It captures changes in mask (in case of more specific routes)
           and change in as-path segment field for each route.
           Additionally it tracks the total number of times a route
           was modified or deleted or added.
        '''
        self.Recent_table = Recent_table
        if self.Last_table == {}:
            print 'Last_table is empty'
            pass
        else:
            for key in self.Last_table:
                flag = 0
                if key in self.Recent_table.keys():
                    if self.Last_table[key][0] != self.Recent_table[key][0]:
                        if key in self.Mask_change:
                            self.Mask_change[key].append(self.Recent_table[key][0])
                        elif key not in self.Mask_change:
                            self.Mask_change[key] = list()
                            self.Mask_change[key].append(self.Recent_table[key][0])
                        if key in self.Total_flaps:
                            self.Total_flaps[key] += 1
                            flag = 1
                        elif key not in self.Total_flaps:
                            self.Total_flaps[key] = 0
                            flag = 1
                    if self.Last_table[key][1] != self.Recent_table[key][1]:
                        if key in self.Aspath_change:
                            self.Aspath_change[key].append(self.Recent_table[key][1])
                        elif key not in self.Aspath_change:
                            self.Aspath_change[key] = list()
                            self.Aspath_change[key].append(self.Recent_table[key][1])
                        if key in self.Total_flaps and flag == 0:
                            self.Total_flaps[key] += 1
                        elif key not in self.Total_flaps and flag == 0:
                            self.Total_flaps[key] = 0
                else:
                    if key in self.Mask_change:
                        self.Mask_change[key].append(0)
                    elif key not in self.Mask_change:
                        self.Mask_change[key] = [0]
                    if key in self.Aspath_change:
                        self.Aspath_change[key].append(0)
                    elif key not in self.Aspath_change:
                        self.Aspath_change[key] = [0]

                    if key in self.Total_flaps and flag == 0:
                        self.Total_flaps[key] += 1
                    elif key not in self.Total_flaps and flag == 0:
                        self.Total_flaps[key] = 0

        for key in self.Recent_table:
            if key not in self.Last_table:
                if key in self.Mask_change:
                    self.Mask_change[key].append(self.Recent_table[key][0])
                elif key not in self.Mask_change:
                    self.Mask_change[key] = list()
                    self.Mask_change[key].append(self.Recent_table[key][0])
                if key in self.Aspath_change:
                    self.Aspath_change[key].append(self.Recent_table[key][1])
                elif key not in self.Aspath_change:
                    self.Aspath_change[key] = list()
                    self.Aspath_change[key].append(self.Recent_table[key][1])
                if key in self.Total_flaps:
                    self.Total_flaps[key] += 1
                elif key not in self.Total_flaps:
                    self.Total_flaps[key] = 0

        self.Last_table = self.Recent_table
        for key in self.Total_flaps:
            if 0 in self.Mask_change[key]:
                fopen = open('Total_flaps.txt', 'w')
                fopen.write(str(self.Total_flaps))
                fopen.close()
        f1 = open('Mask_change.txt', 'w')
        f2 = open('Aspath_change.txt', 'w')
        f1.write(str(self.Mask_change))
        f2.write(str(self.Aspath_change))
        f1.close()
        f2.close()

