
import csv
# In this script, I want to take each epoch second in epoch-and-transcript.csv
# And find its match within all-epoch-seconds-transcript.csv. 

# I want it to put the transcript row next to the epoch row in the all-seconds csv.
# (It can also copy/paste the whole epoch-and-transcript row into the all-epoch
# seconds row; I'll just have to delete one unnecessary column. But seems easier than
# trying to just pick one cell to insert.)

with open("epoch-and-transcript.csv") as epoch_transcript_file: 

	# I'm splitting this with open object on each line
	transcript_epoch = epoch_transcript_file.read().split("\r")

	#print transcript_epoch[18]
	# If I uncomment this, it'll print row 18 (timestamp and quote together bc they aren't
	# separeted yet.)

	# I'm separating each line into individual strings, at each comma
  	for index, quote in enumerate(transcript_epoch):
    		transcript_epoch[index] = quote.split(",")

    	# I got this part from Shannon's states_enumerate.py. I couldn't 
    	# figure out how to get *just* the seconds; turns out this is the way
    	# to do that (the part on the right hand side.)
		epoch_second = transcript_epoch[index][0]

		# if I want to get all the transcript lines, I would do 
		# transcript_lines = transcript_epoch[index][1]
		# because each transcript line is at place 1 in the list. (or something). 
		print epoch_second


with open("all-epoch-seconds-transcript.csv") as seconds_transcript_file:
	all_seconds = seconds_transcript_file.read().split("\r")

	print all_seconds

#for (epoch_second, all_seconds) in zip(epoch_transcript_file, seconds_transcript_file):
	#if epoch_second == all_seconds: 
#print epoch_second
		


# Ok, now I have the list of epoch seconds in the transcript saved as the 
# epoch_second variable. 

# What I need to do is open the next csv file, and do a loop that takes
# each epoch_
	#if == 