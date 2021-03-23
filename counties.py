counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


for county in counties:
    print(county)


for i in range(len(counties)):
    print(counties[i])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

#print corresponding key value
counties_dict["Denver"]

#prints corresponding key values
for county in counties_dict:
    print(counties_dict[county])

#prints corresponding key values too
for county in counties_dict:
    print(counties_dict.get(county))

#prints both the key and its corresponding value
for county, voters in counties_dict.items():
    print(county, voters)

#prints each county and registered voter from counties dictionary in sentence structure
for county, voters in counties_dict.items():
    print(county + " county has", str(voters) + " registered voters.")


#get each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#using range() function to iterate over the list of dictionaries to print the counties in voting_data
for i in range(len(voting_data)):

      print(voting_data[i])

#getting the values from a list of dictionaries
    #to retrieve only the values from each dict in list of dict, use nested for loop

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieving number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#If we only want to print the county name from each dictionary:
for county_dict in voting_data:
    print(county_dict['county']
