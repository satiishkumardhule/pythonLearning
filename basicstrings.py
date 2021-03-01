import string


print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

test_string1="The quick brown fox jumps over lazy dog on the 1st of December"
test_string2="Supercalifragiristic"
test_string3="90210"

result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)

print(test_string1.isalnum())
print(test_string2.isalpha())

print(all([c.isalnum() for c in test_string1]))
print(test_string3.isnumeric())