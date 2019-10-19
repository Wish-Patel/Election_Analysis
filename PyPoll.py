import csv
import os

#load file
file_to_load = os.path.join("Resources", "election_results.csv")

# output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open file and read
with open(file_to_load) as election_data:
	
	#read/analyze data
	file_reader = csv.reader(election_data)

	#print rows
	headers = next(file_reader)
	print(headers)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
     txt_file.write(
		 f"Countries in the Election\n"
		 f"-------------------------------------------------------\n"
		 f"Arapahoe\nDenver\nJefferson"
		 )

# Close the file
txt_file.close()
#create an array of all the candidates
#iterate through the file to get total votes for each candidate
#get total votes cast for the election

#close the file
election_data.close()