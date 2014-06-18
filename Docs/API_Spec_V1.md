API SPEC V1 (INCOMPLETE)
------------------------

### API REQUEST: Get donation types

GET /API/v1/DonationTypes/

Return Value: List of dictionaries of donation type details
Donation Dict Schema:
*  ID: Unique donation type ID, defined by backend
*  Title: Donation title/name string
* Subtypes: List of donation sub qualifier dicts, Null on on sub qualifiers
   - ID: Unique donaiton subtype ID, defined by backend
   - Title: Donation subtype title/name string

Example:
```json
[ { "ID": 1,
    "Title": "volunteering",
    "Subtypes": null }, 
  { "ID": 2,
    "Title": "Give Blood",
    "Subtypes": [ 
                { "ID": 101, "Title": "A" },
                { "ID": 102, "Title": "A+" },
		{ "ID": 103, "Title": "B+" },
		{ "ID": 104, "Title": "B-" },
		{ "ID": 105, "Title": "AB+" },
		{ "ID": 106, "Title": "AB-" },
		{ "ID": 107, "Title": "O+" },
		{ "ID": 108, "Title": "O-" },
		{ "ID": 109, "Title": "Unknown" },
             ]
  },
  { "ID": 3,
    "Title": "Donate Food",
    "Subtypes": null 
  },
  { "ID": 4, 
    "Title": "Donate Money",
    "Subtypes": null 
  },
  { "ID": 5, 
    "Title": "Donate Clothing",
    "Subtypes": [
                { "ID": 201, "Title": "Children's" },
                { "ID": 202, "Title": "Mens's" },
                { "ID": 203, "Title": "Women's" },
              ]
  },
  { "ID": 6, 
    "Title": "Donate Toys",
  }, 
]
```

### API REQUEST: Find nearby donors/recipients

- Donor Search: POST: /API/v1/Search/donors/
- Recipient Search: POST: /API/v1/Search/recipients/

POSTDATA:
```json
{
  "DonationID": 5,            # ID of the donation type
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
[ {
    "Name": "Salvation Army",              # Name of donor/recipient
    "DonationID": 5,                       # Donation ID for this response
    "Subtypes": [ 201, 202, 203 ],         # Subtypes offered/accepted
    "Address": "1234 Fake St\nDenver, CO", # (String)
    "Lat": 39.737567,                      # Latitude (Float)
    "Lon": -104.984718,                    # Longitude (Float)
    "Distance": 0,                         # Distance in miles (Int)
    "Details": {                           # Arbitrary key value paring for details like hours, notes, etc.
       "key1": "value1",
       "key2": "value2",
    },
  }
]
```

### API REQUEST: Authenticate User

- To Be Defined

### API REQUEST: Update/save Details

- To Be Defined
