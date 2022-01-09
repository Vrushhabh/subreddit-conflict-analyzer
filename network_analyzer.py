import reddit_network
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt


def make_dataframe(network: dict, sub_list: [str]):
    """
    It was forgotten that I could manually make a pandas dataframe(so analysis is faster and I don't have to use the
    extractor functions and don't have to rely on a previously well-made cvs) so this function basically takes the
    Hyperlink objects I made and makes a dataframe with the values.  To make the runtime lower, extra columns will be
    added as needed. This is not important but funny enough I remembered this as I was taking my morning shower

    Parameters
    ----------
    network (dict<str,<str,Hyperlink>>)
        The adjacency list that contains the subreddits that are being ranked
    sub_list: [str]
        The list of subs that the hyperlinks in the dataframe are gotten from

    Returns
    -------
    dataframe : pd.DataFrame
        the pandas data frame made from the hyperlinks
    """

    rows = []
    for sub in sub_list:
        linked_subs = network[sub].keys()
        for linked_sub in linked_subs:
            # count the number of times the sub_a a posted a link to sub_b
            for hyperlink in network[sub][linked_sub]:
                # the list is very vertical for dataframe parameters for ease of visibility
                row = [hyperlink.start_sub,
                       hyperlink.end_sub,
                       hyperlink.post_id,
                       hyperlink.body_check,
                       hyperlink.date_posted,
                       hyperlink.time_posted,
                       hyperlink.negative_sentiment,
                       hyperlink.num_words,
                       hyperlink.num_unique_words,
                       hyperlink.num_of_long_words,
                       hyperlink.avg_word_length,
                       hyperlink.AR_index,
                       hyperlink.positive_sentiment_value,
                       hyperlink.negative_sentiment_value,
                       hyperlink.LIWC_future,
                       hyperlink.LIWC_present,
                       hyperlink.LIWC_past,
                       hyperlink.LIWC_numbers]

                rows.append(row)

    return pd.DataFrame(rows, columns=["start_sub",
                                      "end_sub",
                                      "post_id",
                                      "body_check",
                                      "date_posted",
                                      "time_posted",
                                      "negative_sentiment",
                                      "num_words",
                                      "num_unique_words",
                                      "num_of_long_words",
                                      "avg_word_length",
                                      "AR_index",
                                      "positive_sentiment_value",
                                      "negative_sentiment_value",
                                      "LIWC_future",
                                      "LIWC_present",
                                      "LIWC_past",
                                      "LWIC_numbers"])


def rank_activity(network: dict):
    """
    This function looks ranks the activity of each of the subs according to the amount of hyperlinks that comes from
    them. The purpose of this is to get the subreddits with more samples of data  so we can make more reasonable
    assumptions about the people that use the sub.

    Parameters:
        network(dict<str,<str,Hyperlink>>) : The reddit network that contains the subreddits that are being ranked

    Returns:
        sorted_relevancy (list[str]) : A list of all the subreddits in the network sorted from most activity
        (most direct edges coming from it) to least
        sub_edge_count (dict<str, int>) : A dictionary that keeps track of how many hyperlinks comes from a single sub

    """
    subreddits = network.keys()
    sub_edge_count = {}

    for sub_a in subreddits:
        linked_subs = network[sub_a].keys()
        sub_activity = 0
        for sub_b in linked_subs:
            # count the number of times the sub_a a posted a link to sub_b
            sub_activity += len(network[sub_a][sub_b])

        sub_edge_count[sub_a] = sub_activity

    sorted_dict = {}
    sorted_keys = sorted(sub_edge_count, key=sub_edge_count.get)

    for w in sorted_keys:
        sorted_dict[w] = sub_edge_count[w]
    # sorted_dict = reversed(sorted_dict)
    sorted_relevancy = list(reversed(sorted_dict.keys()))
    return sorted_dict, sorted_relevancy


