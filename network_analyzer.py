import reddit_network
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

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

def extract_distribution_plt_data(network: dict, sub:str, body_check=True, neg_sentiment=True, data_type="num_words"):
    """
    This function is ment to extract the data needed to make particular violin plots that looks at
    correlations. These violin plots lets us know a rough correlation of data_types such as word count
    and how they are related to the sentiment (whether the post is positive or not) if they exhibit distinctly
    different behavior.

    Parameters:
        network : (dict<str,<str,Hyperlink>>)
            The reddit network that contains the subreddits that are being ranked

        sub : str
            The subreddit we want to make the violin plot for

        body_check : bool
            Lets the function know whether we are looking at links from the title or the post
            (this is needed because titles are often times shorter and are used for a different purpose than
            the body)

        neg_sentiment : bool
            Lets the function know whether we are looking at the positive or negative posts

        data_type : str
            Lets the function know what instance variable is being analyzed for the Hyperlink


    Returns:
        data : [data_type] :
            Returns a list to be made into a violin plot. (data_type refers to the type of the instance variable in
            Hyperlink.py)
    """
    distribution = []
    all_hyper_links = network[sub].keys()

    for linked_sub in all_hyper_links:
        all_links_to_sub = network[sub][linked_sub]
        for link in all_links_to_sub:
            if (link.body_check == body_check):
                if (link.negative_sentiment == neg_sentiment):
                    distribution.append(link.get_data(data_type))
    distribution.pop(0)  # get rid of place holder map value when node is first initialized (not right type)
    return distribution



def extract_correlation_plt_data(network: dict, sub:str, body_check=True,  y="negative_sentiment_value",
x="num_words"):
    """
    This function is ment to extract the data needed to make particular correlation plots that look at
    the strength of relationship between 2 instance variable in a  sub

    Parameters:
        network : (dict<str,<str,Hyperlink>>)
            The reddit network that contains the subreddits that are being ranked

        sub : str
            The subreddit we want to make the correlation plot for

        body_check : bool
            Lets the function know whether we are looking at links from the title or the post
            (this is needed because titles are often times shorter and are used for a different purpose than
            the body)

        y : str
            Lets the function know what instance variable is being analyzed for the Hyperlink on the y axis of the
            scatter plot
        x: str
            Lets the function know what instance variable is being analyzed for the Hyperlink on the y axis of the
            scatter plot


    Returns:
        data : [data_type type]
            Returns a list to be made into a violin plot. (data_type refers to the type of the instance variable in
            Hyperlink.py)
        y_data : [data_type]
            Returns a list of random variables that are going to be on the y-axis. Potential dependent variables such as
            things such sentiment which might be correlated things such as word count. (data_type refers to the type of
            the instance variable in Hyperlink.py)

        x_data : [data_type]
            Returns a list of random variables that are going to be on the x-axis. Potential independent variables such
            as things such word count which might be correlated things such as word count. (data_type refers to the type
            of the instance variable in Hyperlink.py)
    """
    y_data = []
    x_data = []
    all_hyper_links = network[sub].keys()



    return y_data, x_data
















