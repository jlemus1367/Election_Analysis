# Election Analysis

## Project Overview
The Colorado Board of Elections has given us the task to determine the results of an election for a particular congressional district. They have provided us with a CSV file that contains all the votes cast for the congressional district in question. Using the file, we must substantiate the winner of the election and other data of interest that could help determine the future outcome of other elections. We will be using python and the CSV module to aid in our election audit. Considering that we are working with an entire congressional district's election data, we can expect a sizeable data set that is too large to be analyzed with excel or other spreadsheet applications. It is imperative that we convey the information to the board of elections promptly to ensure a smooth transition of power. Python and its extensive resources will provide us the processing power to generate the data we are seeking.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.54.3

## Results
* Total votes cast:
  * The total amount of votes cast for the congressional district was 369,711.
We got these results by looping through the election data CSV file and by initializing a vote count variable that would increment after each iteration. As the for loop iterated through each row, the vote count variable would increase by one with the following code:
```
total_votes = 0

for row in reader:
    total_votes += 1
```
* Votes per county:
  * Jefferson County had a turnout of 38,855 voters, which accounted for 10.5% of the total voter turnout for the congressional district we analyzed.
  * Jefferson County had a turnout of 306,055 voters, which accounted for 82.8% of the total voter turnout for the congressional district we analyzed.
  * Arapahoe County had a turnout of 38,855 voters, which accounted for 10.5% of the total voter turnout for the congressional district we analyzed.

* County with largest amount of votes:
  *  Denver county had the largest turnout for the particular district we analyzed, with 82.8% of the total turnout for the congressional district

* Number of votes and the percentage of the total votes for each candidate:
  * Candidate Charles Casper Stockham received 85,213 votes which amounted to 23.0% of the popular vote.
  * Candidate Diana DeGette received 272,892 votes which amounted to 73.8% of the popular vote.
  * Candidate Raymon Anthony Doane received 11,606 votes which amounted to 3.1% of the popular vote.

* Election winner:
  * Diana DeGette won the election with a vote count of 272,892 of the 369,711 votes cast. She won 73.8% of the total votes casted.

Votes per county and candidate were obtained by creating blank dictionaries that would hold the names as the key and their respective votes as the value:
```
county_votes = {}
candidate_votes = {}
```
Using the index where the county name and candidate name appeared in the row, we then created a variable to hold the names:
```
candidate_name = row[2]
county_name = row[1]
```
After that, we iterated through the CSV file and incrementally added to the value of each dictionary key using the following code:
```
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
 ```
We then calculated the percentages by using the a for loop to get the votes from each respective candidate/county and dividing those values by the total votes in the election. The following code shows how the percentages for each county was calculated:
```
# Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count.
        votes_county = county_votes[county_name]
        # Calculate the percentage of votes for the county.
        votes_county_percentage = float(votes_county) / float(total_votes) * 100
 ```
## Summary
The code's structure can be used as a template for any election in the future if the format of the future CSV files remains similar to the one we used in our analysis. For example, we used indexing to gather the data about candidates and counties to determine each distinct value. Indexing was imperative in determining the unique candidates and counties present in the vast dataset. By being cognizant of how the data organized in future CSV files containing election data, we can successfully apply indexing to extract the necessary information for future audits. Considering each row in the CSV file has a list structure, we determined that each item at index[2] was the candidate's name, which is the third item in the list. If we happen to have a CSV file where the candidate names are located in a different position in their row, we can adjust the indexing to reflect the changes. 

After obtaining the distinct candidates and counties, we used them as the keys for the dictionaries we created to track each unique candidate and county's votes. We can use the same method again in any future audits to iterate through the entire CSV file and incrementally adding to a counter variable that keeps tracks of votes by seeing if a particular name in a row matches the key in our dictionary. If it does, the key's value increases incrementally. We can essentially maintain the same script with only minimal alterations to expedite future election results.
