from reddit_network import *
from hyperlink import *

network = RedditNetwork()
sub_A = "A"

network.insert_subreddit(sub_A)

#make sure sub was added to network
assert(network.get_network().get(sub_A) is not None)

offmychest	= "offmychest"
askreddit = "askreddit"

with open("singleEdge_test.cvs") as f:
    # makes block of the data from the test cvs file that gets turned into a edge
    contents = f.readlines()
f.close()
x = 0
offmychest_to_askreddit_link = Hyperlink(contents[0])

network.insert_subreddit(offmychest)
network.insert_subreddit(askreddit)
network.insert_hyperlink(offmychest, askreddit, offmychest_to_askreddit_link)

assert(network.get_network().get(offmychest).get(askreddit)[0].start_sub == "offmychest")
assert(network.get_network().get(offmychest).get(askreddit)[0].end_sub == "askreddit")
assert(network.get_network().get(offmychest).get(askreddit)[0].num_of_words == 310)
assert(network.get_network().get(offmychest).get(askreddit)[0].num_of_long_words == 56) # six or more letters
assert(network.get_network().get(offmychest).get(askreddit)[0].avg_word_length == 4.51612903226)









