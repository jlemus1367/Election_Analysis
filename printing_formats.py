#F-strings
    ##easier than concatenation

    ##F-String begins with an f followed by a string contained within quotes
    
    ##curly braces are used to add variables or expressions to f-string

    ##F-string can perform calculations and format the value as string!

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#using f-strings with dictionaries
    ##will make our code easier to write and read

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    #without f-strings

for county, voters, in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    #with f-strings


#multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#format floats
    ##general format for number to formal in fstring
        ###f'{value:{width}.{precision}}
            ####width specifies number of character used to display value
            ####precision indicates number of decimal places --> e.g.  .2f=2 deciamal
            #### when formatting number, use comma to add thousands seperator after width
                ##### e.g. f'{value:{width},.{precision}}'

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
              
print(message_to_candidate)

#skill drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#skill drill 3.2.11 very end
voting_data = [{'county':'Arapahoe', 'registered_voters': 422829}, 
                    {'county':'Denver', 'registered_voters': 463353}, 
                    {'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

        
        
