# -*- coding: UTF-8 -*-

''' Metadata, Copyright, License: 
------------------------------------------------------------------------
Name:       Convert_Table_To_CSV_Standalone_List_Comprehension.py
Purpose:    This script converts a table to a CSV table with selected
            fields.
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

# Input feature class or standalone table
input_table = arcpy.management.MakeFeatureLayer('https://services2.arcgis.com/eQgAMgHr2CRobt2r/arcgis/rest/services/UnconventionalWellsPA/FeatureServer/0',
                                                'Unconventional Wells')

# Identify list of field names to be exported
field_names = ['Shape', 'PERMIT_NO', 'FARM_NAME', 'COUNTY', 'PROD_GAS_QUANT']

# Output CSV file path and name
output_csv = r'{Copy CSV folder Path here...}\UnconventionalWells.csv'



''' Script '''

# Read the feature class or standalone table data

# Create a list of the data
data = [row for row in arcpy.da.SearchCursor(input_table, field_names)]

# Print first 10 rows
# print(data[:10])


# Create and open the output CSV file
with open(output_csv, 'w', newline='') as csv_file:
    # Creates CSV Writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the field names to the new CSV file
    csv_writer.writerow(field_names)
    
    # Write the feature class or standalone table data to the new CSV file
    csv_writer.writerows(data)

# Message that the script is finished
print("CSV file complete; located at {}".format(output_csv))