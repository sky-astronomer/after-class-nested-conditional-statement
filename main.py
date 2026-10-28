print("Welcome to my holiday planner")
print("Select your holiday type")
print("beach")
print("Snowy")
t=input("Enter the holiday type you have selected: ").lower()
if t=="beach":
    print("We have various activities in the beach such as: ")
    print("swimmimg")
    print("Sand castle building")
    r=input("Enter the selected choice of activity: ").lower()
    if r=="swimming":
        print("Swimming is a relaxing and fun activity,go take a splash and enjoy yourself")
    if r=="sand castle building":
        print("Sand castle building is a good way to test your creativity skills! You have to think like an arist and build like an architect.")
if t=="snowy":
    print("We have various activities in the snow such as: ")
    print("snowball fights")
    print("sledging")
    s=input("Enter the selected choice of activity: ").lower()
    if s=="snowball fights":
        print("Snowball fights are fun as long as nobody gets hurt, so round your snow.And take a sgot towards your friend!")
        if s=="sledging":
            print("sledging is fun, going down the hill/mounain and riding on snow like skaating on ice. Once you star doing it, you will be addicted.")
