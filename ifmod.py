#!/usr/bin/python2
import time 
import webbrowser
option='''
Press 1: To enter anything-split each word and search onn google
Press 2:same but find url
Press 3: same but find images answer
Press 4: current time and date
Press 5: open default browser
Press 6: all network IP
Press 7: enter domain name and find owner, email & contact
'''
print option
ch=raw_input()
#webbrowser.open("my name is Pihu")
if ch=='1':
	search_data=raw_input("enter data")
	final_data=search_data.strip()
	# above removing leadind and trailing space
	done_data=final_data.split()
	#spliting each word by space
	for i in done_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)
	

