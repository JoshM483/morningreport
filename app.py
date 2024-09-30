from duckduckgo_search import DDGS
import json
from datetime import datetime, timedelta
import time


"""
Searches for AI related news.
Generates a list of results.
Summarizes the articles and builds a static site with the data

Uses:
Jekyll

DDGS https://github.com/deedy5/duckduckgo_search

"""

def search_news(ddgs, retries = 3, delay = 5, max_results=10):

    search_terms = 'ai'
    for attempt in range(retries):
        try:
            results = list(ddgs.news(search_terms, timelimit="d", max_results=max_results)) 
            print(f"Search results for {search_terms}(attempt {attempt +1}/{retries}: \n{results})")

            # Review rults by ['title'] and ['source'] (and possibly ['body']) and determine if there are articles that are very simmilar.
            # At some point in the future it wold be beneficial to review and combine simmilar results

            return results
        except Exception as e:
            print(f"Error searching news (attempt {attempt +1}/{retries}): {str(e)}")
            if attempt < retries -1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached")
                return []
            


def summarize(url, title, ddgs, retries=3, delay=15):
    prompt = f"Summarize the following article by creating a bullet point list: {title} \nURL: {url} \nOnly generate the bullet points and no other text"

    for attempt in range(retries):
        try:
            print(f"Attempting to summarize article: {title}")
            summary = ddgs.chat(prompt, model='gpt-4o-mini')
            print(f"Summary generated!")
            return summary
        except Exception as e:
            print(f"Error summarizing article (attempt {attempt + 1}/{retries}): {str(e)}")
            if attempt < retries -1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached")
                return "Summary is unavailable due to an unexpected error."
            

def sort_and_filter(artricles):
    """Future feature to pre-sort the article by importance"""
    pass

def format_date(date_str):
    date_obj = datetime.fromisoformat(date_str)
    date = date_obj.strftime('%m-%d-%y')
    return date


def update_data():
    print(f"Starting news update process...")
    ddgs = DDGS()

    articles = search_news(ddgs)
    if not articles:
        print("No articles available. Aborting update process.")
        return
    
    # Sort and filter articles?

    for article in articles:
        summary = summarize(url=article['url'], title=article['title'], ddgs=ddgs)
        article['summary'] = summary
        article['date'] = format_date(article['date'])
        print(f"Article: {article['title']}\nDate: {article['date']}\nSummary: {summary}")

    with open('_data/news_data.json', 'w') as f:
        json.dump(articles, f, indent=2)

if __name__ == '__main__':
    update_data()
