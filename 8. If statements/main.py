x = 19;
y = 10;

if x > y:
	print("X IS VERY BIG");

	if x >= 20:
		print("X is 20 or more");
	elif x < 20: #else if
		print("x is still small");
else:
	print("x is very small");
print("This is not part of the if statement");

y = 0 if (x > y) else 1 # one-liner if statement

print(y)

print("Hello World") if (y > x) else print("Goodbye World")