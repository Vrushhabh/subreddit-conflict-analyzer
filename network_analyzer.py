import reddit_network

def rank_activity(network : dict):
   """
   This function looks ranks the activity of each of the subs according to the amount of hyperlinks that comes from
   them. The purpose of this is to

    Parameters:
        network(dict<str,<str,Hyperlink>>) : The reddit network that contains the subreddits that are being ranked

    Returns:
        sorted_relevancy (list[str]) : A list of all the subreddits in the network sorted from most activity
        (most direct edges coming from it) to least
        sub_edge_count (dict<str, int>) : A dictionary that keeps track of how many hyperlinks comes from a single sub
   """