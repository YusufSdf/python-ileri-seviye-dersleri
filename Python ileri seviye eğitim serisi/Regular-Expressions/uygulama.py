import re

text = "BTK akademi İle Python kurs tarihleri 15-May-2025 15/May/2025 15.05.2025. Telefon numaralarmız +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr"

pattern = r"\d\d[-][a-zA-Z][a-zA-Z][a-zA-Z]-\d{4}"
pattern = r"\d{2}[-./][a-zA-Z]{3}[-./]\d{4}" # [] içine alınırsa aynı anda birden çok karakteri de karşılar

pattern = r"[a-zA-Z]{0,}@\w+[.]\w+"



matches = re.findall(pattern , text)

for i in matches:
    print(i)