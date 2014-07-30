API SPEC V0 (INCOMPLETE)
------------------------

POST data should be Content-Type: application/json.  Other formats wil yeild a 400.

### API REQUEST: Get donation types

GET /API/v0/DonationTypes/

Return Value: List of dictionaries of donation type details
Donation Dict Schema:
*  ID: Unique donation type ID, defined by backend. (String)
*  Title: Donation title/name string
* Subtypes: List of donation sub qualifier dicts, Null on on sub qualifiers
   - ID: Unique donaiton subtype ID, defined by backend
   - Title: Donation subtype title/name string

Example:
```json
[ 
   {
      "ID": "53d848aafc34db000172eb05"
      "Title": "Donate Clothing",
      "Subtypes": [
         {   
            "Title": "Children's",
            "id": "53d848aafc34db000172eb05.0"
         },
         {   
            "Title": "Mens's",
            "id": "53d848aafc34db000172eb05.1"
         },
         {   
            "Title": "Women's",
            "id": "53d848aafc34db000172eb05.2"
         }
      ],
   },
   {   
      "Title": "Donate Toys",
      "ID": "53d848aafc34db000172eb06"
      "Subtypes": null,
   }
]
```

### API REQUEST: Find nearby donors/recipients

- Donor Search: POST: /API/v0/Search/donors/
- Recipient Search: POST: /API/v0/Search/recipients/

POSTDATA:
```json
{
  "DonationID": 5,            # ID of the donation type
                              # Can be omitted or Null if unset
                              # Unset DonationID matches all
  "Subtypes": [ 202, 203 ],   # A list of applicable subtypes
                              # Subtype can be omitted or Null if unset
                              # Unset subtype on donation ID with subtypes matches all 
  "Distance": 50,             # Distance radius in miles (Int)
  "curLat": 39.737567,        # Current Latitude (Float)
  "curLon": -104.984718,      # Current Longitude (Float)
}
```

Return Value: List of dictionaries of matches

Example:
```json
[
   {
      "Name": {
         "FullName": "Savers Business", # Full, complete name of donor/recipient
	 "ShortName": "Savers",         # Short name of donor/recipient, as they would like to be addressed
                                        # Intended fo salutations in the UI, like ("Hi, %s!" % data['Name']['ShortName'])
      },
      "Type": "Business",               # Type of this donor/recipient.

      "Address": {                      # Address hash
         "Line1": "1234 Some Street",
         "City":  "Littleton",
         "State": "Colorado",
         "Zipcode": 80120
      }, 

      "Distance": 0,   # Distance in miles (Int)  -1 for undefined (Missing GeoLoc Data)
      "geoLocation": { # Hash of geolocation data
         "Lat": 39.737567,   # Latitude (Float)
         "Lon": -104.984718, # Longitude (Float)
      },

      "ID": "53d848aafc34db000172eb22",         # Unique donation type ID, defined by backend. (String)
      "DonationID": "53d848aafc34db000172eb05", # Donation ID for this response
      "Subtypes": ["53d848aafc34db000172eb05.0", "53d848aafc34db000172eb05.1", "53d848aafc34db000172eb05.2"], # List of subtypes accepted

      "Email": null, 

      "Details": { # Arbitrary key value paring for details like hours, notes, etc.
         "key1": "value1",
         "key2": "value2",
      },
   }
]
```

### API REQUEST: Donor/Recipient types

- To Be Defined

### API REQUEST: Authenticate User

- To Be Defined

### API REQUEST: Update/save Details

- To Be Defined
