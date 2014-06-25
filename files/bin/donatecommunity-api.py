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

def main():
    app = Flask(__name__)
    api = restful.Api(app)
    
    api.add_resource(dummyDonationTypes, '/API/v1/DonationTypes/')

    # DEBUG/DEV/TODO: Running in debug mode
    app.run(debug=True)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
