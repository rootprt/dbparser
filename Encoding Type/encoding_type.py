import chardet

filepath = input("Enter File Path: ")

with open(filepath, "rb") as rawdata:
    result = chardet.detect(rawdata.read())

encoding = result['encoding']
print("\n", f"Encoding: {encoding}", "\n")