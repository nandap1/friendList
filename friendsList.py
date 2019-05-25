friend_2017 = ["Bob", "Jack", "Joe", "Jemmy"]
friend_2018 = ["Sheena", "Sean", "Lili"]
my_friends = friend_2017 + friend_2018
print(my_friends)
friend = input("Enter a name of the friend:")

if friend in friend_2017:
    print("Your friend is", friend, "in 2017!")
elif friend in friend_2018:
    print("Your friend is", friend, "in 2018!")
else:
    print("You have not met", friend)

newFriend = input("Enter a new friend:").strip()
year = input("Would you like to add to 2017 or 2018?")

if year ==  '2017':
    friend_2017.append(newFriend)
    print(friend_2017)
else:
    friend_2018.append(newFriend)
    print(friend_2018)
