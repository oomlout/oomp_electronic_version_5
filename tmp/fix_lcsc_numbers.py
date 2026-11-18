f = open(r'working_oomp_populate_ic_extra.py')
c = f.read()
f.close()

# Fix XC6206P332MR LCSC number
c = c.replace('"part_number_lcsc": "C51489"', '"part_number_lcsc": "C5446"')
c = c.replace('"product_url": "https://www.lcsc.com/product-detail/C51489.html"', '"product_url": "https://www.lcsc.com/product-detail/C5446.html"')
c = c.replace('"datasheet_url": "https://www.lcsc.com/datasheet/C51489.pdf"', '"datasheet_url": "https://www.lcsc.com/datasheet/C5446.pdf"')
c = c.replace('"part_number_manufacturer": "XC6206P332MR"', '"part_number_manufacturer": "XC6206P332MR-G"')

# Fix XC6206P502MR LCSC number
c = c.replace('"part_number_lcsc": "C51490"', '"part_number_lcsc": "C16767"')
c = c.replace('"product_url": "https://www.lcsc.com/product-detail/C51490.html"', '"product_url": "https://www.lcsc.com/product-detail/C16767.html"')
c = c.replace('"datasheet_url": "https://www.lcsc.com/datasheet/C51490.pdf"', '"datasheet_url": "https://www.lcsc.com/datasheet/C16767.pdf"')

f = open(r'working_oomp_populate_ic_extra.py', 'w')
f.write(c)
f.close()
print('Fixed LCSC numbers')
