import re

text = "BTK akademi python dersleri BTK"
pattern = "BTK"
match = re.search(pattern, text)

result = match

# print(result.span())
print(result.start())
print(result.end())

result = re.findall(pattern, text)
print(result)

