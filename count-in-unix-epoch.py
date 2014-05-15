

# start at 1399503537, which is 5/7/2014 6:58:57 PM GMT-4


# continue adding one second until we get to an hour and ten minutes later
# (the debate is one hour, plus some extra time for reax at the end)

# 70 minutes is 4200 seconds, so we're going to ask python to add 1 until 
# it gets to 1399503537 + 4200, which is 1399507737

# I can do a while loop:


unixsecond = 1399503519

while (unixsecond < 1399507737):
	print unixsecond
	unixsecond = unixsecond + 1

# we want to add until we get to 1399507737, so I can do a while loop. 


# it works! wooooo! I am hacky right now so I copy/pasted it into an excel doc
# but I'm sure I could have it create a .csv for me if I took the time.