#!/usr/bin/python -tt
# Copyright 2013 Tom Noonan II (TJNII)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import Flask,abort,request
from flask.ext import restful

import sys

class dummyDonationTypes(restful.Resource):
    def get(self):
        return [ { "ID": 1,
                   "Title": "volunteering",
                   "Subtypes": None }, 
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
                   "Subtypes": None 
               },
                 { "ID": 4, 
                   "Title": "Donate Money",
                   "Subtypes": None 
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
                   "Subtypes": None 
               }, 
             ]

class dummySearch(restful.Resource):
   def post(self, search_type):
       arguments = request.json

       if type(arguments) is not dict:
           print "ERROR: POST data not a dict"
           abort(400)
       
       # Verify required keys are present
       for key in [ "Distance", "curLat", "curLon"]:
           if not arguments.has_key(key):
               print "ERROR: Missing argument %s" % key
               abort(400)
               
        # Optional arguments
       for key in [ "Subtypes", "DonationID" ]:
           if not arguments.has_key(key):
               arguments[key] = None
               
       # Generate a dummy response
       if search_type == 'recipients':
           return [
                    {
                        "Name": "Dummy Donation Place 1",
                        "DonationID": arguments['DonationID'],
                        "Subtypes": arguments['Subtypes'],
                        "Address": "1234 Fake St\nDenver, CO",
                        "Lat": 39.737567,
                        "Lon": -104.984718,
                        "Distance": 0,
                        "Details": {
                            "key1": "value1",
                            "key2": "value2",
                        },  
                    },
                    {
                        "Name": "Dummy Donation Place 2",
                        "DonationID": arguments['DonationID'],
                        "Subtypes": arguments['Subtypes'],
                        "Address": "5678 Fake St\nDenver, CO",
                        "Lat": 39.737567,
                        "Lon": -104.984718,
                        "Distance": 0,
                        "Details": {
                            "key1": "value1",
                            "key2": "value2",
                        },  
                    },
           ]
       elif search_type == 'donors':
           return [
                    {
                        "Name": "Generous Person 1",
                        "DonationID": arguments['DonationID'],
                        "Subtypes": arguments['Subtypes'],
                        "Address": "5432 Fake St\nDenver, CO",
                        "Lat": 39.737567,
                        "Lon": -104.984718,
                        "Distance": 0,
                        "Details": {
                            "email": "someone@somedomain.com",
                            "twitter": "@someone",
                        },  
                    },
                    {
                        "Name": "Generous Person 2",
                        "DonationID": arguments['DonationID'],
                        "Subtypes": arguments['Subtypes'],
                        "Address": None,
                        "Lat": 39.737567,
                        "Lon": -104.984718,
                        "Distance": 0,
                        "Details": {
                            "email": "someoneelse@somedomain.com",
                            "phone": "(303) 555-1234",
                        },  
                    },
           ]
       else:
           print "ERROR: Unknown search criteria %s" %search_type
           abort(404)


def main():
    app = Flask(__name__)
    api = restful.Api(app)
    
    api.add_resource(dummyDonationTypes, '/API/v1/DonationTypes/')
    api.add_resource(dummySearch, '/API/v1/Search/<string:search_type>/')

    # DEBUG/DEV/TODO: Running in debug mode
    app.run(debug=True)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
