from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")


#article_tag = soup.find(name = "a", class_= "titlelink") gives the first occurrence
articles = soup.find_all(name = "a", class_= "titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

print(article_texts)
print(article_links)

article_upvotes = []
votes = soup.find_all(name = "span", class_ = "score")
for article_score in votes:
    vote = article_score.getText()
    vote_number = int(vote.split(' ')[0]) #'43 points'
    article_upvotes.append(vote_number)

# highest_vote = article_upvotes[0]
# for vote in article_upvotes:
#     if vote > highest_vote:
#         highest_vote = vote

highest_vote = max(article_upvotes)
index_of_highest_vote = article_upvotes.index(highest_vote)
print(index_of_highest_vote)

print(f" The article with the highest votes is '{article_texts[index_of_highest_vote]}', available at {article_links[index_of_highest_vote]}")