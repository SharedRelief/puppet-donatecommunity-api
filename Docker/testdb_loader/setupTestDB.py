#!/usr/bin/python -tt
# Set up a test DB

import argparse
import yaml
from pymongo import MongoClient

def parse_arguments():
    parser = argparse.ArgumentParser(description='Populate a test MongoDB', 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--dbhost", action='store', type=str, default='127.0.0.1', help='MongoDB Host')
    parser.add_argument("--dbport", action='store', type=int, default=27017, help='MongoDB Port')

    parser.add_argument("--database", action='store', type=str, required=True, help='Database to populate')
    parser.add_argument("--sourcefile", action='store', type=str, required=True, help='Source yaml data file')

    args = parser.parse_args()

    return args

def load_data(datafile):
    with open(datafile, 'r') as fd:
        data = fd.read()

    return yaml.load(data)

def populate_db(db, data):
    for key in data.keys():
        for row in data[key]:
            print "Inserting %s into %s" %(row, key)
            db[key].insert(row)

def main():
    args = parse_arguments()
    data = load_data(args.sourcefile)
    
    client = MongoClient(args.dbhost, args.dbport)

    client.drop_database(args.database)
    populate_db(client[args.database], data)

    return 0

if __name__ == '__main__':
    main()
