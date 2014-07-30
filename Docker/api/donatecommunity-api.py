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

import dbBindings
import argparse
import sys

# Globals to pass into flask classes
DB_BINDING = None

class dummyDonationTypes(restful.Resource):
    def get(self):
        global DB_BINDING
        return DB_BINDING.get_donation_types()

class dummySearch(restful.Resource):
   def post(self, search_type):
       global DB_BINDING

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
           # TODO: SEARCH NOT IMPLEMENTED
           # NEED KEYS/GEO DATA
           return DB_BINDING.get_recipients()
       elif search_type == 'donors':
           return DB_BINDING.get_donors()
       else:
           print "ERROR: Unknown search criteria %s" %search_type
           abort(404)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Populate a test MongoDB', 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--dbhost", action='store', type=str, default='127.0.0.1', help='MongoDB Host')
    parser.add_argument("--dbport", action='store', type=int, default=27017, help='MongoDB Port')
    parser.add_argument("--database", action='store', type=str, required=True, help='Database to populate')

    args = parser.parse_args()

    return args


def main():
    global DB_BINDING

    args = parse_arguments()
    
    app = Flask(__name__)
    api = restful.Api(app)

    DB_BINDING = dbBindings.DonateCommunityDB(args.dbhost, args.dbport, args.database)
    
    api.add_resource(dummyDonationTypes, '/API/v1/DonationTypes/')
    api.add_resource(dummySearch, '/API/v1/Search/<string:search_type>/')

    # DEBUG/DEV/TODO: Running in debug mode
    app.run(debug=True)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
