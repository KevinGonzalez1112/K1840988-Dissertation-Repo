import json
import pandas as pd


def json_test_data_to_dictionary():
    # Open the JSON file

    file = open('json_files/JSON_TEST_DATA.json')

    # Convert JSON into Dictionaries

    file_data = json.load(file)

    # Creating an empty array that will store the data that will be used for the dataframe

    dataframe_data = []

    for row in file_data['article_urls']:
        dataframe_data.append(
            [
                row['article_title'],
                row['assessment'],
                row['page_size'],
                row['revisions'],
                0,  # Registered Edits
                row['ip_edits'],
                row['bot_edits'],
                row['unique_editors'],
                0,  # Major Edits
                row['minor_edits'],
                row['semi_auto_edits'],
                row['reverted_edits'],
                row['average_time_between_edits'],
                row['average_edits_per_user'],
                row['average_edits_per_day'],
                row['average_edits_per_month'],
                row['average_edits_per_year'],
                row['edits_made_by_top_10']
            ]
        )

    articles_df = pd.DataFrame(
        data=dataframe_data,
        columns=
        [
            'Title',
            'Assessment Grade',
            'Size in Bytes',
            'Revisions',
            'Registered Edits',
            'IP Edits',
            'Bot Edits',
            'Unique Editors',
            'Major Edits',
            'Minor Edits',
            'Semi Auto Edits',
            'Reverted Edits',
            'Average Time Between Edits',
            'Average Edits Per User',
            'Average Edits Per Day',
            'Average Edits Per Month',
            'Average Edits Per Year',
            'Edits Made By Top 10'
        ]
    )

    # Save dataframe to a CSV file

    articles_df.to_csv(r'C:\Users\Kevin\Desktop\TEST-DATA-1.csv', index=False, header=True)

    # Close the JSON file

    file.close()
