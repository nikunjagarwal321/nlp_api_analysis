from newspaper import Article
import praw
import json

bbc_article_urls = ["https://www.bbc.com/news/articles/c1jx9ep5l63o",
                    "https://www.bbc.com/news/articles/cedy6gl99eno",
                    "https://www.bbc.com/future/article/20250417-biological-reality-what-genetics-has-taught-us-about-race",
                    "https://www.bbc.com/news/articles/c3v9z45pe93o",
                    "https://www.bbc.com/travel/article/20240327-the-centuries-old-baba-recipe-made-with-96-egg-yolks",
                    "https://www.bbc.com/sport/football/articles/cz6d84v5ezpo",
                    "https://www.bbc.com/sport/cricket/articles/c62xd5x4w49o",
                    "https://www.bbc.com/news/articles/czx1g0q43gqo",
                    "https://www.bbc.com/news/articles/c9qww2rv0y0o"]

def fetch_bbc_articles(urls):
    articles = []
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        articles.append(article.text)
    return articles


def fetch_reddit_comments(subreddit, query, post_count=5, comment_count=2):
    comments = []
    reddit = praw.Reddit(
        client_id="",
        client_secret="",
        user_agent=""
    )

    subreddit = reddit.subreddit(subreddit)
    for post in subreddit.search(query, limit=post_count):
        post.comments.replace_more(limit=0)
        for comment in post.comments[:comment_count]:
            if comment.body is not None:
                comments.append(comment.body)
    return comments


articles = fetch_bbc_articles(bbc_article_urls)
reddit_comments = fetch_reddit_comments("science","exceptional", 10, 2)
product_reviews = fetch_reddit_comments("phone", "iphone", 10, 2)

# For classification and entity recognition
print("Articles:")
for article in articles:
    print(article)

# For classification and entity recognition
print("\nReddit Comments:")
for c in reddit_comments:
    print(c)

# For sentiment analysis
print("\nProduct Reviews:")
for p in product_reviews:
    print(p)


json_data = {
    "articles": articles,
    "comments": reddit_comments,
    "reviews": product_reviews
}

# Write to file
with open("data/input.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

