
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#largest county turnout
largest_county = ""
largest_county_count = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

#county options and value 
counties = [] #list
county_votes = {} #key and values (dictionary has been defined)

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) #readcsv file
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # Get the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing counties, add the county to list.
        if county_name not in counties:
            # Add the county name to the county list.
            counties.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
            # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="") #printing the election results in the terminal
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #print the county votes and results 
    print( f"County Votes:\n") #print the county votes as a header
    txt_file.write(f"County Votes:\n") #write to the textfile
    for county in county_votes:
        # Retrieve vote count and percentage.
        co_votes = county_votes[county]
        co_vote_percentage = float(co_votes) / float(total_votes) * 100
        county_results = (
            # f"County Votes:\n"
            f"{county}: {co_vote_percentage:.1f}% ({co_votes:,})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results) 
    #add txt file
    
     # Find county that got the most votes with .values and max 
    for county, votes in county_votes.items():
        if votes == max(county_votes.values()):
            largest_county = county #define the variable 
            largest_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n") #printing the largest county turnout
            #print the largest file to the terminal.
            print(largest_county_summary)
            # Save the largest county to the text file.
            txt_file.write(largest_county_summary)
            

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)