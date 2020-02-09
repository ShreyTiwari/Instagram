""" Importing the one library that we need """
import instaloader

""" Get the instance """
L = instaloader.Instaloader()

print("\n----------------------- Welcome -----------------------\n")

""" Load session """
username = input("Enter your user handle (not your name): ")
password = input("Enter your password: ")
L.login(username, password)       

""" Obtain profile metadata """
profile = instaloader.Profile.from_username(L.context, username)

""" Print the list of followees (people who you are following) """
print("\n\n----------------------- Followees -----------------------")

x = []
for followee in profile.get_followees():
    print(followee.username)
    x.append(followee.username)
print(len(x))

""" Print the list of followers (people who are following you) """
print("\n\n----------------------- Followers -----------------------")
y = []
for follower in profile.get_followers():
    print(follower.username)
    y.append(follower.username)
print(len(y))

""" The important part is the difference (followingAccounts - Followers), i.e who you are following but are not following you """
for i in y:
    if(i in x):
        x.remove(i)

print("\nThe people you need to stop following are...")
for i in x:
    print(i)