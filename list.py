states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[1])
print(states_of_america[-1])
# for changing the stuff in a list
states_of_america[1]="pencilvania"
# for adding stuff
states_of_america.append("kancorp")
# adding multiple items together
states_of_america.extend(["mitansh","devang","kanani"])
print(len(states_of_america))
print(states_of_america)
# index error and nested lists

fruits=["strawberris","Nectarines", "Apples", "Grapes","Peaches", "Cherries", "Pears"]
veg=[ "Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits,veg]
print(dirty_dozen)
print(len(dirty_dozen))



