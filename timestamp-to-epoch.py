import time
import datetime
import csv

# Have to append year, month
# Can get rid of miliseconds
# example format: 18:58:39:00

#time.strptime(18:58:39:00, "%H:%M:%s")

with open("timestamps-to-unix.csv", "r") as timestamps_file:
	#with open("timestamps-to-unix-write.csv", "w") as timestamps_file_write:
			#for row in timestamps_file:
	timestamps = timestamps_file.read().split("\r")
				#out.write('07.05.2014' + row)

	#timestamps.strip(':00')


#for each line, do this: 
	#cut off the (':00') at the end
	#(-3:-1)
	#add ('07.05.2014 ') to the beginning
for timestamp in timestamps:
	#print timestamp[0:-4]

	date_time = '07.05.2014 {0}'.format(timestamp[0:8])
	pattern = '%d.%m.%Y %H:%M:%S'
	epoch = int(time.mktime(time.strptime(date_time, pattern)))
	print epoch

#(to do: get this to print back to a csv. currently it outputs in terminal).