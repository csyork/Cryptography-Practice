import codecs

# Prompt user to enter a hex value
hexValue = input("Enter a hex value: ")

#Convert hex to base64 and print value
base64Value = codecs.encode(codecs.decode(hexValue, "hex"), 'base64').decode()
print(base64Value)
