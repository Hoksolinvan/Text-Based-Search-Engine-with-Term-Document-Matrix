#!/usr/bin/env python3

import sys


def main():
	# Calls the workhorse of this program, the "freqcounter" function
	# Modular programming :)
	return freqcounter()



def freqcounter():
	#Creating a dictionary
	wordcount={}
	#reads line by line from stdin
	for line in sys.stdin:
		#Separates each word from the line and then gets read of any leading or trailing space
		x=line.strip().split(" ")
		for p in x:
			#if p does not exist create a new key-value pair
			if p not in wordcount and p is not "\n" and p is not None and p is not " ":
				wordcount[p]=1
			else:
			#if it already exists just increment the key-value pair value by +1
				wordcount[p]+=1


	#sorts the value of the set
	secondwordcount=sorted(wordcount.keys())
	finalwordcount={}

	for i in secondwordcount:
		finalwordcount[i]=wordcount[i]

	#new dictionary after being sorted by the sorter function
	printer(finalwordcount)


#this function will print the output of the keys and its values onto stdout
def printer(final):
	
	for p in final:
		#handles the case for when '' exists in a dictionary!
		if p !='':
			print(p,final[p])




if __name__=="__main__":
	main()
