# Get data from user.
# Obtain initials, age, birth(year)
# Send info to a list and display entered information
# Then print all user information
# Check age of content 

def display(firstvar, lastvar, agevar, birthvar):
    
    print("Name:", firstvar, "Last Name", lastvar, "Age:", agevar, "Birth Year", birthvar)
    if(agevar < 18):
        print("You can't go put because it's too dangerous")
    else:
        print("You can go out to the street")


def savetolist(firstvar, lastvar, agevar, birthvar):
    userinfo = []
    singleuserinfo = [firstvar, lastvar, agevar, birthvar]
    userinfo.append(singleuserinfo)
    print(userinfo) 

        
if __name__ == "__main__":

    firstvar = str(input('First Name: '))
    lastvar = str(input('Last Name: '))
    agevar = int(input('Age: '))
    birthvar = int(input('Birth Year: '))

    display(firstvar, lastvar, agevar, birthvar)

    savetolist(firstvar, lastvar, agevar, birthvar)

