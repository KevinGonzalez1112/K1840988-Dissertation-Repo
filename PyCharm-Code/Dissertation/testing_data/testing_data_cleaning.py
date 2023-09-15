import pandas as pd


def test_data_cleaning():
    # Reading in initial CSV file

    df = pd.read_csv(r'C:\Users\Kevin\Desktop\DISSERTATION-TEST-DATA-1.csv')

    # Removing unused text in data

    df['Size in Bytes'] = df['Size in Bytes'].str.split(' ').str[0]
    df['IP Edits'] = df['IP Edits'].str.split(' ').str[0]
    df['Bot Edits'] = df['Bot Edits'].str.split(' ').str[0]
    df['Minor Edits'] = df['Minor Edits'].str.split(' ').str[0]
    df['Average Time Between Edits'] = df['Average Time Between Edits'].str.split(' ').str[0]
    df['Edits Made By Top 10'] = df['Edits Made By Top 10'].str.split(' ').str[1]

    # Removing commas in numbers

    df = df.replace(',', '', regex=True)

    # Changing Data Types

    df['Size in Bytes'] = df['Size in Bytes'].astype(str).astype(int)
    df['IP Edits'] = df['IP Edits'].astype(str).astype(int)
    df['Bot Edits'] = df['Bot Edits'].astype(str).astype(int)
    df['Unique Editors'] = df['Unique Editors'].astype(str).astype(int)
    df['Minor Edits'] = df['Minor Edits'].astype(str).astype(int)
    df['Semi Auto Edits'] = df['Semi Auto Edits'].astype(str).astype(int)
    df['Reverted Edits'] = df['Reverted Edits'].astype(str).astype(int)
    df['Average Time Between Edits'] = df['Average Time Between Edits'].astype(str).astype(float) * 24
    df['Edits Made By Top 10'] = df['Edits Made By Top 10'].astype(str).astype(int)

    # Saving Changes to a CSV File 

    df.to_csv(r'C:\Users\Kevin\Desktop\TEST-DATA-1-CLEAN.csv', index=False, header=True)
