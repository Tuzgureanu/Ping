from sql_lib import sql
from time import ctime,time
import Gnuplot, os

def plot_to_file(db, tb, field = 'Reachability', start = None, end = None):

    dbd = sql()
    data = dbd.get_data(db = db,tb = tb,start = start, end = end)

    type = {'Reachability': '(%)',
            'Jitter': '(ms)',
            'Avg_Rsp_time': '(ms)'}

    host = tb.replace('_','.')[3:]

    header = data[0]

    g = Gnuplot.Gnuplot()
    g.title("Host %s" %host)

    g.xlabel("Time")
    g.ylabel("%s %s" %(field.replace('_',' '), type[field]))
   
    time_list = [i[header['Time']] for i in data[1::]]
    xtic = int(max(time_list)-min(time_list))/4

    data_list = [i[header[field]] for i in data[1::]]
    rc = Gnuplot.Data(time_list, data_list, title = field.replace('_',' '), with_='lines')

    g("set grid")
    g("set xtic (%s, %s, %s, %s)" %(time_list[0], 
                                    time_list[len(time_list)/3],
                                    time_list[len(time_list)*2/3],
                                    time_list[-1]))
    
    if 'Reachability' == field:
        g('set ytic 0,10,105')
    elif field in ['Jitter','Avg_Rsp_time']:
        mx = max(data_list)*1.1
        g('set ytic 0,%d,%d' %(mx/5,mx))

    g("set terminal svg")
    g.plot(rc) # write SVG data directly to stdout ...

    name = host + '_' + ctime(time())

    cwd = os.getcwd()

    g.hardcopy (filename='%s/graphs/%s.png' %(cwd,name), terminal='png') # write last plot to another terminal

    del g
