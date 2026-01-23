# -- Practical Membership Control --

# List Contains Admin
admins=["basmala","sara","ahmed","mohamed","doha","dina"]
name=input("Hello,enter your name to check if you are admin or not\n").strip().lower()

# If Name is In Admin
if name in admins:
    print("You Are Admin!")

    option=input("you need to update(u) or delete(d) your name:").strip().lower()
    # Update Option
    if option=="update" or option=="u":
        newname=input("enter new name:").strip().lower() 
        admins[admins.index(name)]=newname
        print("name updated")
     # Delete Option
    elif option=="delete"or option=="d":
        admins.remove(name)
        print("name deleted")
# Wrong Option
else:
    print("wrong,you are not admin")
    added=input("you need to added to admins yes(y)or no(n):").strip().lower()
    if added=="yes" or added=="y":
        admins.append(name)
        print("you are added")
    else:
        print("you are not added")