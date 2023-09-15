import requests
import json
import pywikibot
import pandas as pd


def get_training_articles():
    # Create empty array to store titles

    articles = []

    # Open the JSON file

    file = open('json_files/JSON_TRAIN_ARTICLES.json')

    # Convert JSON into Dictionaries

    file_data = json.load(file)

    for row in file_data['urls']:
        article_title = row.split('/')[5]
        articles.append(article_title)

    return articles


def get_page_revisions(article):
    site = pywikibot.Site("en", "wikipedia")

    # Splitting the URL string to get only the article title from the end

    page = pywikibot.Page(site, article)

    # Getting all the revisions made to a page

    revisions_initial = page.revisions()

    # Converting these to a list to make further work simpler

    revisions = list(revisions_initial)

    return revisions


def get_page_anon_revisions(revisions):
    anon_contributors_list = []

    # Adding the revisions that have been made by anonymous aka IP contributors to an array

    for Revision in revisions:
        if Revision.anon == True:
            anon_contributors_list.append(Revision.user)

    # Converting this array into a set to only keep unique instance of the users id

    anon_contributors_set = set(anon_contributors_list)

    # Finding the length to return the number of unique contributors

    anon_contributors = len(anon_contributors_set)

    return anon_contributors


def get_train_data():
    dataframe_data = []

    # Get the list of articles

    articles = get_training_articles()

    # Using the newly created MediaWiki API to get the remaining data required

    for article in articles:

        bot_count = 0

        link = 'https://xtools.wmcloud.org/api/page/bot_data/enwiki/' + article

        response = requests.get(link).text
        response_info = json.loads(response)

        for bot in response_info['bots']:
            bot_count = bot_count + 1

        revisions = get_page_revisions(article)

        anon_revisions = get_page_anon_revisions(revisions)

        dataframe_data.append([article, 0, anon_revisions, bot_count])

    articles_df = pd.DataFrame(data=dataframe_data,
                               columns=
                               [
                                   'Title',
                                   'Registered Editors',
                                   'IP Editors',
                                   'Bot Editors'
                               ])

    # Save dataframe to a CSV file

    articles_df.to_csv(r'C:\Users\Kevin\Desktop\TRAINING-DATA-2.csv', index=False, header=True)

    return articles_df
