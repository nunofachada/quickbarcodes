# Summary

QuickBarcodes consists of two Python3 scripts which produce price 
tag barcodes using Latex as backend.

* [generator.py](generator.py) - Generates EAN numerical codes
* [barcodes.py](barcodes.py) - Generates price tag barcodes

# Usage

### Generator

    $ python3 generator.py

### Barcodes

    $ python3 barcodes.py source.csv

Replace `source.csv` with the barcodes/prices source file. Each line
in this file should correspond to a product, and must have the following 
sequence:

    ProductReference,ProductName,Price,Barcode

Example:

    PR_016102_28,A Product Name,49.90,5601303180333
    IN_016102B_30,Some Other Product Name,49.90,5601303180342
    SC_30_Unjaded,Unjaded Product,49.90,5601303180379
    GR_JCKT01,Great Jacket 1,49.90,5601303180351

# Custom configuration

Configuration can be changed directly in the source of the Python
code and the Latex templates.

# Dependencies

### Python

* math
* datetime
* stdnum
* csv
* sys
* subprocess
* collections

### Latex

* pst-barcode
* rotating
* textpos
* eurosym
* afterpage

# Licence

Simplified BSD License
