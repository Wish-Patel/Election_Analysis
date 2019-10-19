import csv
import os

#load file
file_to_load = os.path.join("Resources", "election_results.csv")

# output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options =[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open file and read
with open(file_to_load) as election_data:
	
	#read/analyze data
	file_reader = csv.reader(election_data)

	#reading headers
	headers = next(file_reader)

	#reading data
	for row in file_reader:
		total_votes +=1
		candidate_name = row[2]
		if candidate_name not in candidate_options:
			#creatinga  list of candidates in the election
			candidate_options.append(candidate_name)

			#initializing cadidate's vote count
			candidate_votes[candidate_name] = 0

		#counting cadidate's votes
		candidate_votes[candidate_name] +=1

	#determine voting percentages
	for candidate in candidate_votes:
		#determine votes for a candidate
		votes = candidate_votes[candidate]

		#calculate percentage
		vote_percentage = int(votes)/int(total_votes)*100

		#print voting counts and percentages for all candidates
		print (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

		#determining the winning contender
		if (votes > winning_count) and (vote_percentage > winning_percentage):
			winning_count = votes
			winning_percentage = vote_percentage
			# set winning candidate name
			winning_candidate = candidate
	
	winning_candidate_summary = (
		f"-------------------------\n"
		f"Winner: {winning_candidate}\n"
		f"Winning Vote Count: {winning_count:,}\n"
		f"Winning Percentage: {winning_percentage:.1f}%\n"
		f"-------------------------\n")
	print(winning_candidate_summary)



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