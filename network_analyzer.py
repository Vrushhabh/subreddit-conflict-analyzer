import reddit_network

def rank_activity(network: dict):
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
    subreddits = network.keys()
    sub_edge_count = {}

    for sub in subreddits:
        linked_subs = network[sub].keys()
        sub_activity = 0
        for link in linked_subs:
            sub_activity += len(network[sub][link])

        sub_edge_count[sub] = sub_activity

    sorted_dict = {}
    sorted_keys = sorted(sub_edge_count, key=sub_edge_count.get)

    for w in sorted_keys:
       sorted_dict[w] = sub_edge_count[w]

    #sorted_dict = reversed(sorted_dict)
    sorted_relevancy = list(reversed(sorted_dict.keys()))
    print(sorted_relevancy)
    return sorted_dict, sorted_relevancy


