price = [10,27,35,27,-35,0]

result = [vergi * 120 if vergi > 0 else False for vergi in price] # if ve else kullanımı
result = [vergi * 120 for vergi in price if vergi > 0] # sadece if varsa

print(result)