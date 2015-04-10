'''This module provides a simple GUI interface to the user to select
   a prefix and view the as-path change. It calls the as_path_prep_data()
   method and sends the selected prefix for further plotting process.
'''


import plotme
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw

class SimpleGUI:
    '''This class represents the GUI class that creates a window with two
       buttons: 'show from prefix list' and 'Exit'
       Attributes: interface, window
       Methods: __init__, execute_list
    '''
    def __init__(self, parent, add_list, aspath_dict):
        self.interface = Pmw.SelectionDialog(parent,
	        title = 'IPv6 Prefix List',
	        buttons = ('OK', 'Cancel'),
	        defaultbutton = 'OK',
	        scrolledlist_labelpos = 'n',
	        label_text = 'Please select a prefix and press Ok',
	        scrolledlist_items = add_list,
		    command = self.execute_list)
        self.interface.withdraw()
        self.interface.pack(fill = 'both', expand=1, padx=5, pady=5)
        self.interface.deactivate()
        self.aspath_dict = aspath_dict
        window = Tkinter.Button(parent, text = 'Select from Prefix-list',
	            command = self.interface.activate)
        window.pack(padx = 8, pady = 8)

    def execute_list(self, click):
        choice = self.interface.getcurselection()
        if click == 'Cancel':
            print 'You clicked on', click, '(no selection)'
        else:
            print 'you selected ' + choice[0]
            import plotme
            obj = plotme.plotme()
            obj.as_path_prep_data(choice[0], self.aspath_dict)
            
        self.interface.deactivate(click)


def gui_main(add_list, aspath_dict):
    '''This function acts as the driver to the SimpleGUI class.
       It creates the object of this class and is the end module
       of the entire program.
    '''
    title= 'Live BGP Monitoring - AS-Path Fluctuations'
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title(title)
    exitButton = Tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = SimpleGUI(root, add_list, aspath_dict)
    root.mainloop()
    print '<<<<<END>>>>>'
'''
print'>'*40+'Generating GUI Interface'+'<'*40
add_list = ('2607:F4E0:200::', '2001:5B0:3D00::', '2001:67C:4C::', '2001:67C:2718::', '2607:F568:4000::', '2607:CC00:4::', '2001:67C:18C::', '2001:CD8::', '2620:101:402D::', '2001:67C:11C4::', '2001:1450::')

aspath_dict = {'2001:67C:2710::': [' 30071 6939 12956 5610 25512 57823 '], '2001:1450::': [' 30071 3549 5602 5602 5602 5602',' 30071 3356 5602 ', ' 30071 3549 104 5602 '], '2404:8000:72::': [' 30071 17451 '], '2600:2008::': [' 30071 6453 33517 '], '2001:4848:209::': [' 30071 6939 31985 '], '2620:101:402D::': [' 30071 2914 16880 '], '2607:CC00:4::': [' 30071 6939 7385 13833 '], '2620:68::': [' 30071 3356 29906 '], '2A00:5600::': [' 30071 2914 31727 '], '2604:9E80::': [' 30071 6939 11260 30396 '], '2001:67C:18C::': [' 30071 6939 8641 47682 '], '2804:B44:E000::': [' 30071 16735 23456 ', ' 30071 104 23456 ' ], '2001:CD8::': [' 30071 6939 9264 4780 '], '2001:67C:11C4::': [' 30071 3257 34744 '], '2404:138:40::': [' 30071 6939 4637 9901 23655 38299 38299 38299 38299 '], '2001:502:4612::': [' 30071 12008 '], '2600:1014:B000::': [' 30071 1239 2828 6167 22394 22394 22394 22394 22394 '], '2001:67C:2670::': [' 30071 9009 39392 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 57706 '], '2401:A000:124::': [' 30071 6939 17832 '], '2001:1530::': [' 30071 6667 2586 '], '2A00:1888::': [' 30071 2914 10021 50314 '], '2404:E400::': [' 30071 3549 18200 45345 '], '2407:7E00::': [' 30071 3491 56049 '], '2001:67C:4C::': [' 30071 1257 8437 3248 35609 '], '2607:FD50:6::': [' 30071 4436 40015 '], '2001:DF0:46::': [' 30071 4725 2907 24287 '], '2801:0:60::': [' 30071 3257 19169 27814 52274 '], '2400:4A00::': [' 30071 6453 38757 9341 '], '2604:1380::': [' 30071 6939 54825 '], '2405:6400:2000::': [' 30071 6453 23678 '], '2001:67C:2718::': [' 30071 3356 5400 25068 '], '2001:5B0:3D00::': [' 30071 1239 2828 6621 '], '2001:1458::': [' 30071 2914 8928 513 513 '], '2A00:EC00::': [' 30071 9002 16066 '], '2001:67C:2988::': [' 30071 6939 9121 58151 '], '2607:F2E0::': [' 30071 6939 36252 '], '2600:200F::': [' 30071 6939 33517 '], '2001:DF0:458::': [' 30071 6453 4755 18229 '], '2607:F568:4000::': [' 30071 6939 4323 11215 '], '2607:F4E0:200::': [' 30071 3356 4150 ', ' 30071 104 4150 '], '2400:3100::': [' 30071 4826 38456 45935 '], '2403:BA00:6FF::': [' 30071 6453 45147 24521 ']}
gui_main(add_list, aspath_dict)'''
