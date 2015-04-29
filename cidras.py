
''' This module accepts AS Number from user and returns
the Company name that bought the AS and total population of that city.'''
import string
import urllib

   
def fetch_zipage(as_no):
    '''This function fetches the entire webpage for the as number.
    It filters out data from the html coded page line by line.
    Filters out AS name details from the extracted data and displays them.'''
    #print 'in ras file'
    zip_url = urllib.urlopen('http://www.cidr-report.org/cgi-bin/as-report?as=' + as_no + '&view=2.0&v=6')
    flag = 0
    b = []
    for line in zip_url:
        temp = line.strip()
        #print temp
        if '<ul>' in temp:
            a = temp.find('<ul>')
            b = temp.find('</ul>')
            #print temp[a+4:b], 'inras'
            return temp[a+4:b]
            break
