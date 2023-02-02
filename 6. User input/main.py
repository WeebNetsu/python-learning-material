from getpass import getpass # library inside python for CLI passwords input

print("Your name: ");
x = input(); #gets user input
print("Your name is " + x);

# you can put thext inside input() to enter text on the same line
x = int(input("Your age: ")); # int converts the input into an integer
print("You are " + str(x) + " years old"); # use str() to convert int to str

x = float(input("How much money do you have? : "));
print("You have " + str(x) + " amount of money");

# HERE WE USE getpass
username = input("Username: ")
password = getpass("Password: ")
print("Your password is", password)