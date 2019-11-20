# supreme-waddle-ocr

Simple python script that reads the text from an image

## Running the script

Run `ready.py` in your terminal or IDE and the script will read the text from the image in the root directory. 

On a successfull read of the image the output will look like this: 

```
{'text': u'Isporticos Transfer Corp.\n128 Bakeland Ave\nMiddlesex, New Jersey 88645\n\nTruck: ADLI\n\nCustewer: 8@1848/Alliance Disposal LLC\nCarrier: @81840/Alliance Disposal LLC\n\nComment:\nOrigin\n\nNEWE/New Brunswick\n\nCustomer Account Balance:\n\n \n\nLirense: XHFLIQ\nTruck Type: Roli-off\n\nMaterials & Services\n\n1@8% of 13C/T130\n\n-3, 528.69\n\n[\n\nGuantity Unit\n\nDeputy Weighwaster:\n\nTicket: 447129\nDate: 11/5/2013\nTime: 12216:14 - 12:27:31\n\nScale\nGross: 43860 1b In Seale i\nTare: 3714@ 1b Out Scale i\nNet: 6728 ib\n\nCarrier DEP: 38257\nTruck DEP: 684993\n\nTrailer DEP: 227281\n\nRate /init Amount\nTON $86. A5/Ton $291.62\nFees: $5. 81\n\nNJ Recycling Tax: $18. 88\nTotal Agount: $307.71\n\nBob'}
```

The text captured from the image will always be stored as a dictionary with a "text" key `{'text': ... }`. To change this output type please refer to the `pytesseract.py` > `image_to_string()` documentation. 

## Authors

- **Joseph Haddad** - _Initial Work_ 

## Acknowledgments

- Google
- Stack Overflow
