import re
text = "BTK akademi 123 12345 12345"

pattern = r"\d\d"
pattern = r"\d{3,4}"
pattern = r"[a-zA-z0-4]"


result = re.finditer(pattern, text)

for i in result:
    print(i.group())