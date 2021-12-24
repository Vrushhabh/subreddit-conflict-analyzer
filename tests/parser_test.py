from hyperlink import *

with open("singleEdge_test.cvs") as f:
    # makes block of the data from the test cvs file that gets turned into a edge
    contents = f.readlines()
f.close()
x = 0
offmychest_to_askreddit_link = Hyperlink(contents[0])

assert (offmychest_to_askreddit_link.start_sub == "offmychest")
assert (offmychest_to_askreddit_link.end_sub == "askreddit")
assert (offmychest_to_askreddit_link.char_total == 1763)
assert (offmychest_to_askreddit_link.num_words == 310)
#if the post had conflict with the subreddit it was linking
assert (offmychest_to_askreddit_link.negative_sentiment == True)

