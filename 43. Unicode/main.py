# https://www.online-toolz.com/tools/text-unicode-entities-convertor.php
# we can work with UTF-8 characters by using 'u'

# \u0020 translates into 0x0020 in UTF-8
print(u"Hello\u0020World") # Hello World

# Why use unicode? Helps you display characters from other languages:
chinese = u"\u4F60\u597D"
print(chinese)

japanese = u"\u3053\u3093\u306B\u3061\u306F"
print(japanese)