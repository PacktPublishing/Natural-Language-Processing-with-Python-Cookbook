import feedparser

myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")
print('Feed Title :', myFeed['feed']['title'])
print('Number of posts :', len(myFeed.entries))
post = myFeed.entries[0]
print('Post Title :',post.title)
content = post.content[0].value
print('Raw content :\n',content)