debate-reactions
================

This is a repo of what I'm using to parse and display data from React Labs.

This is probably not useful to anyone as is, but I'm putting it up here because I wrote my first python scripts that are for my own project and I am super excited about that, and because I'm learning python with a lot of awesome women in Shannon Turner's #hearmecode class. So if anyone also learning python with Shannon wants to talk about unix epoch time or cleaning up/merging csv files, let's do it! 

At the Post, we partnered with React Labs for a Maryland governor's race debate, and asked readers to tap their reactions into their smartphones while the debate was going on. 

See here: How to use your smartphone as a real-time reaction tool for Md. governor’s race debate

http://www.washingtonpost.com/blogs/ask-the-post/wp/2014/05/06/how-to-use-your-smartphone-as-a-real-time-reaction-tool-for-md-governors-race-debate/

They could choose the candidate who was speaking, and then choose a reaction: Truth, Fact-check!, I support and I oppose. 

I've been interested in what React Labs is doing because they're trying to make real-time reactions more parsable and valuable. Instead of unstructured article comments or tweets, we have data at the end showing what statements specifically people reacted to, and how. (Did they support that sentence? Did a ton just ask for a fact-check on that claim?)

There was live charting of all the participants, and afterwards a json was exported. To parse and display the data, I had to write a few python files and get everything clean and matched up in a csv. 

*TLDR*: I got data from readers reacting to a political debate. It was essentially a ginormous json file of over 10,000 individual reactions. I turned that into a ginormous Python dictionary to manipulate it. I also had to match those timestamped reactions to a timestamped transcript. Then I used Tableau Public to display my cleaned and compiled data. 

Went from this raw json file: 
https://raw.githubusercontent.com/scarothers/debate-reactions/master/20140507-debate.json

to this graphic that charts reactions over the course of the debate, by candidate and reaction type:
http://public.tableausoftware.com/views/May7-joined-tables/Fulldebate?:showVizHome=no#1

And this one where I pulled out the statements that readers most wanted to be fact-checked for each candidate: 

http://public.tableausoftware.com/profile/scarothers#!/vizhome/May7-joined-tables/Dashboard2

*What else I'd like to do*: I basically took a very internet-friendly jSON feed and turned it into a static file I could manipulate in Talbeau (which is a very user-friendly charting program). It would also make a lot of sense to keep it in jSON and display a graphic with JavaScript, but I'm not that far along in JavaScript. One step at a time, ya'll, that's all you can really do. 

/// 

Here's my to-do list and the python/csv files I made to accomplish them: 

- I have a lot of .json files that I need to turn into .csv files
	
	*done:* all-responses.csv. I had to clean it from json to csv and then add columns for target (candidate) and reaction button. 

- I have to get a csv-style list of every unix second from the beginning of the debate to the end

	*done:* count-in-unix-epoch.py, copy/pasted into all-epoch-seconds-transcript.csv

- I have to change all the date/time marks in the transcript to unix epoch seconds

	*done:* timestamp-to-epoch.py took the timestamps in timestamps-to-unix.csv and created their equivalients in epoch seconds. Then, I copy/pasted the epoch seconds into my workbook. 

- I have to match every timestamped reaction to the (again, unix second) time it occurred during the debate

	*done:* with compare-csvs-and-append-matches.py, which put data into outFile.py
