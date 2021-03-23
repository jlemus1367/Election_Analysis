counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("what is the temperature outside? "))

if temperature > 80:
    print("turn on the AC")
else:
    print("open the window")

#what is the score?
score = int(input("what is your test score? "))

#determine grade
# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


x = 0
while x <= 5:
    print(x)
    x = x + 1

