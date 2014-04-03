#!/usr/bin/env python3

import math
import datetime
import stdnum.ean

# country + company + prod. id
# However I use country (560=PT) + 6 date digits + 3 prod. id digits
barcode_base = "560" + datetime.date.today().strftime("%y%m%d")

# list of 1000 barcodes
barcodes = []

# generate 1000 barcodes
for j in range(0, 999):

	# current barcode
	barcode = barcode_base + "%03d" % j            

	# determine check digit
	check_digit = stdnum.ean.calc_check_digit(barcode)

	# append barcode to list
	barcodes.append(barcode + check_digit)

# save to file
with open('barcodes.txt', mode='wt', encoding='utf-8') as barfile:
	barfile.write('\n'.join(barcodes))

