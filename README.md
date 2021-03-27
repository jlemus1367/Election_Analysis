# Election_Analysis

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


## Summary
