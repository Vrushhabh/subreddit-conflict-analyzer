from reddit_network import RedditNetwork
import network_analyzer

mega_network = RedditNetwork()
#first make network from hyperlink from bodies of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-body1.tsv")

#second grow network from hyperlinks from titles of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-title.tsv"
                  ,False)
network_analyzer.rank_activity(mega_network.get_network())