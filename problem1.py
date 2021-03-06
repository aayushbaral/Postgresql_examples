#!/usr/bin/env python3

"""
	problem1.py - Python3 program
	Author: Aayush Baral (aayushbaral@bennington.edu)
	Created: 10/14/2017
"""

import psycopg2
import psycopg2.extras

def business_to_csv(filename="business.csv"):

	with open(filename, 'w') as csv_file: 

		try:
			connection = psycopg2.connect("dbname = 'yelp_db' user = 'aayushbaral'")
			cur = connection.cursor() 
			cur.execute("""SELECT * FROM business""")
			total_rows = cur.fetchall() 
			csv_file.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}\n'.format('id', 'name', 'neighborhood', 'address', 'city', 'state', 'postal_code', 'lattitude', 'longitude', 'stars', 'review_count', 'is_open'))
			for row in total_rows: 
				comma_separated_value = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}\n".format(row[0], row[1].replace(",", ""), row[2], row[3].replace(",", ""), row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
				csv_file.write(comma_separated_value)
			
			csv_file.close()

		except Exception as e:
			print("Couldn't open the database: {0}".format(e))

business_to_csv()



