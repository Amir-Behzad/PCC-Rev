''''
 More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.
'''

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