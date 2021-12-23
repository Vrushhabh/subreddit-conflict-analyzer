from hyperlink import *

with open("singleEdge_test.cvs") as f:
    # makes block of the data from the test cvs file that gets turned into a edge
    contents = f.readlines()
f.close()
x = 0
league_to_trt_link = Hyperlink(contents[0])

assert (league_to_trt_link.start_sub == "offmychest")
assert (league_to_trt_link.end_sub == "askreddit")
assert (league_to_trt_link.char_total == 1763)
assert (league_to_trt_link.num_words == 310)
#if the post had conflict with the subreddit it was linking
assert (league_to_trt_link.negative_sentiment == True)

