hasNumber = "177013"
hasString = "HelloWorld" # spaces may change the outcome
hasBoth = "H3ll0Wor1d"

print(hasNumber.isdigit()) # true since it is only numbers
print(hasString.isdigit()) # false, since it isn't just digets
print(hasBoth.isdigit()) # false, since it isn't just digets


print(hasNumber.isalpha()) # false since it is only numbers
print(hasString.isalpha()) # true, since it's just the alphabed (a space will cause it to be false)
print(hasBoth.isalpha()) # false, since it isn't just alphabetic