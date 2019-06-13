import requests
import random
import os
import wikipediaapi
w = wikipediaapi.Wikipedia('en')


def get_random_page_titles(n):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action":"query",
        "format":"json",
        "list": "random",
        "rnlimit": str(n),
        "rnnamespace": 0,
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    page_titles = []
    for random_article in DATA['query']['random']:
        page_titles.append(random_article['title'])

    return page_titles

def get_page_summary(title):
    try:
        return w.page(title).summary
    except:
        return ""

def collect_corpus(n):
    titles = get_random_page_titles(n)

    summaries = []
    for i in range(len(titles)):
        print(i, "/", n)
        summaries = get_page_summary(titles[i])
 
    title_summary_pairs = list(zip(titles, summaries))

    # Cleaning
    long_enough = []
    for data_point in title_summary_pairs:
        if len(data_point[1]) > 200:
            long_enough.append(data_point)

    # Transforming
    title_marker = "---###<title>###---"
    summary_marker = "---###<summary>###---"
    end_marker = "---###<end>###---"
    annotated_text = ""
    for (title, summary) in long_enough:
        annotated_text += title_marker + title + summary_marker + summary + end_marker

    if not os.path.isdir("downloaded_summaries"):
        os.mkdir("downloaded_summaries")

    filename = "downloaded_summaries/summaries" + str(random.random())[-10:] + ".txt"
    f = open(filename, 'w+')
    f.write(annotated_text)


if __name__ == '__main__':
    collect_corpus(500)