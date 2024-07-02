#!/usr/bin/env python3


import sys
import os
import math

def main():

	#Command line argument for index files
	path=sys.argv[1]
	
	usrinput=sys.stdin

	
	#Function for reading from the sorted documents and returns a list
	sorteddocs=traversedocs(path)

	#Function for reading from the sorted terms and returns a list
	sortedterms=traverseterms(path)

	#Reads from the matrix and returns as a dictionary
	sortedmatrix=traversematrix(path,sortedterms)

	#Reads from the query vector file and creates a dictionary of query vectors
	queryvector=vectormaker(usrinput,sortedterms)

	
	#Calculates the cos similarity values and returns the collection of those values to an array
	cosvalues=cossine(queryvector,sorteddocs,sortedmatrix)
	

	
	#Prints the cos-similarity values to stdout
	
	for j in range(0,len(cosvalues)):
		print(cosvalues[j][0],cosvalues[j][1])
		



	

def traversedocs(path):

	sorteddocs=[]
	
	#traverses from current path to sorted_documents.txt using os.walk
	for root,dirs,files in os.walk(path,topdown=True):
		#Scans each file
		for filename in files:
			if filename == "sorted_documents.txt":
				#Creates a path from current to the sorted_documents.txt
				with open(os.path.join(root,filename),"r") as file:
					#Reads line by line from the file
					for line in file:
						sorteddocs.append(line.strip())
	return sorteddocs


def traverseterms(path):
	
	sortedterms=[]

	#traverses from current path to sorted_terms.txt using os.walk
	for root,dirs,files in os.walk(path,topdown=True):
		#Scans each file
		for filename in files:
			if filename == "sorted_terms.txt":
				with open(os.path.join(root,filename),"r") as file:
					#Reads line by line and stores into a list
					for line in file:
		 				sortedterms.append(line.strip())
	return sortedterms



def traversematrix(path,sortedterms):

	sortedmatrix={}
	
	for root,dirs,files in os.walk(path,topdown=True):

		for filename in files:
			if filename == "td_matrix.txt":
				with open(os.path.join(root,filename),"r") as file:
					#because the first line includes the row and columns of the matrix document we have to loop through the document once to ensure that we skip it! Count keep tracks of the
					#line starting from index 0 
					#while i keeps track of the index of the list
					count=0
					i=0
					for line in file:
						if count != 0:
							lists=line.split()
							sortedmatrix[sortedterms[i]]=lists
							i=i+1
						count=count+1
	
	return sortedmatrix

					
def vectormaker(userinput,origin):
	
	#storing the vectors in dictionaries, therefore creating a dictionary of dictionary/vectors
	#The counter is used to give each of those dictionaries indexes so it would be easier to reference each query vector which is a dictionary on its own
	
	vector = {}
	
	#initialize the vector dictionary with the sortedwords list
	for words in origin:
		vector[words] = [0] * 1

	#reads line by line from userinput
	for line in userinput:

		word=line.strip().split(" ")

		if word[0] in vector:
			newlist=[]
			newlist.append(word[1])
			#updates the vector until there is no more lines to read
			vector.update({word[0]:newlist})


	return vector

def cossine(vector,sorted_docs,sorted_matrix):
	
	cos_values = []  # Initialize cos_values outside the loop
	finaldict = {}

	

	if vector is not None:  # Check if vector is properly initialized
		for doc_idx in range(len(sorted_docs)):
			numerator = 0
			sum_query = 0
			sum_doc = 0

			for term in sorted_matrix:
				if term in vector and term in sorted_matrix:  # Check if term exists in both dictionaries
					query_value = vector.get(term)

					if query_value is not None:  # Check if query_value is properly initialized

						# Calculate the dot product
						numerator += int(query_value[0]) * int(sorted_matrix[term][doc_idx])

						# Calculate the sum of squares for the query vector
					sum_query += int(query_value[0]) ** 2

                        			# Calculate the sum of squares for the document vector
					sum_doc += int(sorted_matrix[term][doc_idx]) ** 2

           			# Calculate the denominator
			denominator = math.sqrt(sum_query) * math.sqrt(sum_doc)

            			# Calculate the cosine similarity
            			# Avoid division by zero
			if denominator != 0:
				cos_value = round(numerator / denominator, 4)
				secondcosval = "{:.4f}".format(cos_value)
				cos_values.append([secondcosval, sorted_docs[doc_idx]])

        		# Sort the cosine values in descending order
		cos_values.sort(reverse=True)
		finaldict= cos_values

	return finaldict
		
		
			


if __name__ == "__main__":
	main()
