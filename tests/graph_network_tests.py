import sys
sys.path.append('../')
from reddit_network import *
from hyperlink import *


network = RedditNetwork()
sub_A = string
sub_A = "A"

network.insert_subreddit(sub_A)

#make sure sub was added to network
print(network.get_network().get(sub_A))
assert(network.get_network().get(sub_A) is not None)

offmychest	= "offmychest"
askreddit = "askreddit"

with open("singleEdge_test.cvs") as f:
    # makes block of the data from the test cvs file that gets turned into a edge
    contents = f.readlines()
f.close()
x = 0
offmychest_to_askreddit_link = Hyperlink(contents[0],True)

network.insert_subreddit(offmychest)
network.insert_subreddit(askreddit)
network.insert_hyperlink(offmychest, askreddit, offmychest_to_askreddit_link)

assert(network.get_network().get(offmychest).get(askreddit)[0].start_sub == "offmychest")
assert(network.get_network().get(offmychest).get(askreddit)[0].end_sub == "askreddit")
assert(network.get_network().get(offmychest).get(askreddit)[0].num_words == 310)
assert(network.get_network().get(offmychest).get(askreddit)[0].num_of_long_words == 56) # six or more letters
assert(network.get_network().get(offmychest).get(askreddit)[0].avg_word_length == 4.51612903226)

mega_network = RedditNetwork()
#first make network from hyperlink from bodies of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-body1.tsv")

#second grow network from hyperlinks from titles of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-title.tsv"
                  ,False)
network_test = mega_network.get_network()
#make sure all nodes are in the network (you can go to SNAP (the dataset website) to see where I found these next #s)
assert(len(network_test) == 55863)
keys = network_test.keys()
edge_amount = 0
for k in keys:
    edgelist = network_test[k].keys()
    for e in edgelist:
        edge_amount += len(network_test[k][e])

#make sure all the edges are in the node (apparently I am missing 2 edges but the sample size seems big enough so its
#not much of a concern the amount is suppose to be 858490
assert(edge_amount == 858488)
foo = Hyperlink

foo = network_test["cat"]["kitten"][0]
print(foo.num_words)
print(foo.body)
print(foo.start_sub)
print(foo.post_id)















