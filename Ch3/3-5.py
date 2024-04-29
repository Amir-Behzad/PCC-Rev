"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list.
"""

guests_list = [
    'Seneca',
    'Marcus Aurelius',
    'Xeno',
    'Emerson',
    'David Goggins'
    ]

cancled_guests = []

print()

for guest in guests_list:
    print(f"{guest} is invited to the pary.")


cancled_guests.append(guests_list.pop(-2))
guests_list.append('Ryan Holiday')

print()

for guest in cancled_guests:
    print(f"{guest} would not come to the party.")

print()

for guest in guests_list:
    print(f"{guest} would come to the party.")

print()