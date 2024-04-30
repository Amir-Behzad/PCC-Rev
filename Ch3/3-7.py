"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
Print a message to each of the two people still on your list, letting them know they’re still invited.
Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""


guests_list = [
    'Seneca',
    'Marcus Aurelius',
    'Zeno',
    'Emerson',
    'David Goggins'
    ]

print()

print("Guests' list:")
for guest in guests_list:
    print(f"{guest} is invited to the pary.")

print("\nSince we've got a bigger table, we're gonna have more stoics at the party!\n")

guests_list.insert(0, 'Chrysippus')
guests_list.insert(3, 'Epictetus')
guests_list.insert(3, 'Cicero')

print("Guests' list:")
for guest in guests_list:
    print(f"{guest} is ivited to the party.")
    
print("\nThe table has not arrived!\n")

cancled_guests = []

while len(guests_list) > 2:
    popped_guest = guests_list.pop()
    cancled_guests.append(popped_guest)
    print(f"Sorry {popped_guest}, there invitation has been cancled.")

print(f"\nCancled Guests:", cancled_guests, '\n')

for guest in guests_list:
    print(f"See you at the party tomorrow dear {guest}!")

print()