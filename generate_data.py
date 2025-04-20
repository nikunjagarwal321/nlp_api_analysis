from newspaper import Article
import praw

bbc_article_urls = ["https://www.bbc.com/news/articles/czx1g0q43gqo"]

def fetch_bbc_articles(urls):
    articles = []
    for url in urls:
        article = Article(url)
        article.download()
        articles.append(article.parse())
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
            comments.append(comment.body)
    return comments


articles = fetch_bbc_articles(bbc_article_urls)
reddit_comments = fetch_reddit_comments("phone","iphone", 5, 2)

for article in articles:
    print(article.title)

for c in reddit_comments:
    print(c)