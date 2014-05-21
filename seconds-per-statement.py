# Take as input epoch-and-transcript.csv, which lists epoch start time for each quote in the
# transcript. Do math for each line so you see the difference in seconds for each line, and 
# thus the total seconds per line. 

# Write to a new file that has as its columns: 
	# Epoch start time
	# Quote
	# Total time

# How will python do this math? 
	# Determine the epoch second for the line (quote-start-second)
	# Determine the epoch second for the next line (quote-end-second)
	# Do subtraction (quote-end-second minus quote-start-second) = total-quote-seconds


# (I might be double-counting seconds here somehow, but it's fine. I just need an approximate measure of 
# each chunk of text so I can determine how many reactions-per-second there were. If I need it to be more 
# exact, I can take quote-end-second and subtract 1 and then do the math.)

# Is there a method in python to get the next in a list? 

import csv

with open('epoch-and-transcript.csv', 'r') as epoch_and_transcript_data: 

	seconds = epoch_and_transcript_data.read().split("\n")

	print seconds[0:1]
    
