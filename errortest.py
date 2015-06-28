#try:
import time
error_file_name = 'Error File Report: ' + time.ctime() + '.txt'
error_file = open(error_file_name, 'a')
print 'running'
#except Exception, e:
#no method called append... :(
error_file.append('Program criical error at ' + time.ctime())
error_file.append('stuff')
error_file.append()