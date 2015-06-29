#errortest.py

"""
Short breakout of how to handle errors and preserve an 
output about the error in an external file. 
Host program is required to state output file and import 
traceback and time.
Time isn't really necessary but useful for timestamping errors 
you aren't handling right now. 
"""

def handle(output):
	e = traceback.format_exc()
	error_file = open(output, 'a')
	error_file.write('\n****NEW EXCEPTION THROWN****\n')

	print 'Printing error to ' + output
	#Timestamp	
	error_file.write('Program critical error at ' + time.ctime())
	error_file.write('\n\n')
	error_file.write(e)
	error_file.write('****END OF EXCEPTION****\n\n')


import traceback, time
error_file_name = 'TestErrs.log'

try: errorhere
except Exception:
	handle(error_file_name)


######Some commentary on error handling below #####



"""
The traceback object is pretty comprehensive if a bit hard to 
negotiate. See documentation for details: 
https://docs.python.org/2/library/traceback.html

****

Funny thing about opening the same file multiple times is that
whichever file is opened first will print all of it's content 
first. See below:
Python:
	>>> e_file = 'TestErrOut.txt'
	>>> out1 = open(e_file, 'a')
	>>> out2 = open(e_file, 'a')
	>>> out1.write('test1')
	>>> out2.write('test2')
	>>> out1.write('test1.1')
	>>> out3 = open(e_file, 'a')
	>>> out3.write('test3')
	>>> ^D
Bash:
	cat TestErrOut.txt
	test1test1.1test2test3
"""
