#!/bin/false
# dbBindings: Donate Community DB Bindings
# 2014 TJNII

from pymongo import MongoClient

class DonateCommunityDB(object):
    def __init__(self, dbhost, dbport, dbname):
        self.db = MongoClient(dbhost, dbport)[dbname]

        self.mandatory_fields = {
            "Name": None,
            "Subtypes": None,
            "Address": None,
            "geoLocation": None,
            "Distance": -1,
            "Details": None,
            }

    def _convert_id(self, row_dict):
        """Convert the Mongo _id field to a API friendly id value in a hash"""
        row_dict['id'] = str(row_dict['_id'])
        row_dict.pop('_id')
        return row_dict
    
    def _get_records(self, table):
        """Return a list of records from the donor or recipient table"""
        ret_val = []
        for record in self.db[table].find():
            # Merge record and mandatory_fields so mandatory fields will always be present in the output,
            # regardless of record state
            v = self.mandatory_fields.copy()
            v.update(record)
            self._convert_id(v)
            ret_val.append(v)

        return ret_val

    def get_donation_types(self):
        """Return a list of donation types"""
        ret_val = []
        for record in self.db['donationTypes'].find():
            ret_row = self._convert_id(record.copy())
            # Add a unique ID to the subtypes
            if ret_row['Subtypes'] is not None:
                for c in range(0, len(ret_row['Subtypes'])):
                    ret_row['Subtypes'][c]['id'] = "%s.%s" % (ret_row['id'], c)
            ret_val.append(ret_row)
        return ret_val        

    def get_donors(self):
        """Return a list of donors"""
        return self._get_records('donors')

    def get_recipients(self):
        """Return a list of recipients"""
        return self._get_records('recipients')
