# -*- coding: UTF-8 -*-

''' Metadata, Copyright, License:
------------------------------------------------------------------------
Name:       Convert_Table_To_CSV.py
Purpose:    This script tool converts a table to a CSV table with 
            selected fields with the option to include field aliases.
Author:     Whitacre, James
Created:    2024/04/10
Version:    0.0.1
Copyright:  Copyright <YYYY> <Your Name or Organization>
License:    Licensed under the Apache License, Version 2.0 (the
            "License"); you may not use this file except in compliance
            with the License. You may obtain a copy of the License at
            http://www.apache.org/licenses/LICENSE-2.0
            Unless required by applicable law or agreed to in writing,
            software distributed under the License is distributed on an
            "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
            either express or implied. See the License for the specific
            language governing permissions and limitations under the
            License.
------------------------------------------------------------------------
'''

''' Import Modules '''
import arcpy
import csv


''' Parameters '''
# Input Table (Table View)
input_table = arcpy.GetParameterAsText(0) 

# Output Fields (Field, Multiple values: Yes; Filter: Field [NOT Shape, Blob, Raster, XML]; Dependency: input_table)
field_names = arcpy.GetParameterAsText(1).split(';')

# Output CSV Table (File; Output; Filter: File [csv;txt])
output_csv = arcpy.GetParameterAsText(2)

# Add Field Aliases to CSV Table (String; Type: Optional; Default: NONE; Filter:  Value List [NONE, AS_HEADER, AS_ROW])
alias_incl = arcpy.GetParameterAsText(3)

# Add a message to test the parameter input
# arcpy.AddMessage(field_names) #  output_csv

''' Script '''

# Set the progressor, first count the number of records
rows = int(arcpy.management.GetCount(input_table)[0])
arcpy.SetProgressor('step', '{0} rows in dataset...'.format(rows), 0, rows, 1)


# Read the feature class or standalone table data
# Create an empty list to append data to
data = []

# Create a search cursor to access the data
with arcpy.da.SearchCursor(input_table, field_names) as cursor:
    for row in cursor:
        # Append each row to the data list
        data.append(row)
        # Update the progressor position
        arcpy.SetProgressorPosition()


# Create a describe object of the input table
desc = arcpy.Describe(input_table)

# If aliases are included: Create a list of all of the field aliases in the table
if alias_incl != 'NONE':
    # Create a list of all of the fields in the table
    aliases = [field.aliasName for field in desc.fields if field.name in field_names]


# Reset and create new progressor to show that CSV file is being created
arcpy.ResetProgressor()
arcpy.SetProgressor('default', 'Creating CSV file...')


# Open the new output CSV file
with open(output_csv, 'w', newline='') as csv_file:
    # Creates CSV Writer object
    csv_writer = csv.writer(csv_file)
    
    # Write aliases or fields names as the header to the output CSV file
    if alias_incl == 'AS_HEADER':
        csv_writer.writerow(aliases)
        arcpy.AddMessage('Aliases written as the header...')
    else:
        csv_writer.writerow(field_names)

    # Write aliases as a row to output CSV file if 'AS_ROW' is selected
    if alias_incl == 'AS_ROW':
        csv_writer.writerow(aliases)
        arcpy.AddMessage('Aliases written as a row...')
    
    # Write the feature class or standalone table data to the new CSV file
    csv_writer.writerows(data)


# Message that the script is finished
arcpy.AddMessage('CSV file complete: {0} rows and {1} fields exported.'.format(rows, len(field_names)))