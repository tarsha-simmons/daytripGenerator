# Day Trip Generator

#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate lists.

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I dont like
#(10 points): As a user, I want to be able to confirm that my day trip is 'complete' once I like all of the random selections. 
#(10 points): As a user, I want to display my completed trip in the console.
#(5 points): As a developer, I want all of my functions to have a Single Responsibility, remember each function should do one THING!
import random

destination = ['Barbados', 'California', 'New York', 'Cabos', 'Miami']
restaraunt = ['Chic Fil A', 'Taco Bell', 'Chipotle', 'McDonalds', 'Dominos']
transportation = ['Plane', 'Train', 'Boat', 'Car', 'Walk']
entertainment = ['Painting', 'Swimming', 'Broadway', 'Dancing', 'Sightsee']

print('Hi! Welcome to Quarantined day trip destinations! Where we plan your trip for you')

print(f'Good News!, Today, {random.choice(destination)} was selected for you!')

answer = input('Does this destination work for you? Please select [y/n]:')
while answer == 'n':
 random_destination = random.choice(destination)
print(f'We are so Sorry that location doesnt work, let us try again, how does {random.choice(destination)} Please select [y/n]:')
answer = input('Does this selection work for you? Please select [y/n]:')
if answer == 'y':
  print('Perfect! Let us select a restaurant for the day!')

random_restaurant = random.choice(restaraunt)
print(f'Would you like to dine at {random.choice(restaraunt)}? Please select [y/n]:')
while answer == 'n':
 print(f'We can find a better dining choice for your day trip, what about {random.choice(restaraunt)}, If this restaurant is okay please select [y/n]:')
if answer =='y':
 print('Awesome, Hope you enjoy! Lets find adequate transportation for the day')

random_transportation = random.choice(transportation)
print(f'Today, it would appear that {random.choice(transportation)} has been chosen for the day, does that work for you? Please select [y/n:]')
while answer == 'n':
 print(f'How about {random.choice(transportation)} for your day in the city, Please select [y/n]:')
 if answer =='y':
    print(f'Wonderful! The most exciting part is finding entertainment for the day!')

random_entertainment = random.choice(entertainment)
print(f'For entertainment {random.choice(entertainment)} was found,if that is satisfactory please select [y/n]:')
while answer == 'n':
 print(f'No worries, Let us try again, how about {random.choice(entertainment)}, please select [y/n]:')
if answer == 'y':
    print(f'We are so glad we could assist you with your day trip Needs!')