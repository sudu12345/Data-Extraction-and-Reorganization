import pandas as pd
import os
import openpyxl

folder_path = 'Bucket 01'
op_file = 'Output.xlsx'

output_data = {
    'File Name' :[],
    'Full Name' :[],
    'Date of Birth' :[],
    'Member ID' :[],
    'Policy Number' :[],
    'Claim Number' :[],
}

df = pd.DataFrame(output_data)

output = openpyxl.Workbook()
output_sheet = output.active
output_sheet.title = 'output data'
