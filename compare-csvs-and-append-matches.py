# I found this by Googling. This is taken exactly from the following (corrected code) on Stack Overflow: 
# http://stackoverflow.com/questions/17635247/comparing-and-appending-csv-files-in-python
# I had to change 'rB' to 'rU' to make it understand universal newline signals. or something. 

# But it worked! Here's what I needed to happen: 
    # I had one file with all the seconds in the hour-long debate. 
    # I had another file with the seconds when a transcript section started. (It's split into sentences, 
        # more or less). 
    # I needed Python to look through the file with transcript sentences, take each second it started, 
        # and match it (and append it!) to the file with ALL seconds. 

    # The result is the new outFile, which essentially has ALL seconds, but at each transcript second
    # time, it ALSO has the transcript quote. 

    # Saved me going through >200 lines of a CSV file and doing ctrl F and copy/pasting a transcript
    # line into another file. 

# WOOOOOO. I am so happy. 

# That being said, I couldn't tell you for the life of me why the masterlist part works. Just does.

import csv

f1 = file('all-epoch-seconds.csv', 'rU')
f2 = file('epoch-and-transcript.csv', 'rU')
f3 = file('outFile2.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = [row for row in c2]
for hosts_row in c1:
    found = False
    for master_row in masterlist:
        results_row = hosts_row
        if hosts_row and master_row:
            if hosts_row[0] == master_row[0]:
                results_row.append(master_row[1])
                found = True
                break

    #if not found:
       # results_row.append(master_row[1])

    if any(hosts_row):
        c3.writerow(results_row)