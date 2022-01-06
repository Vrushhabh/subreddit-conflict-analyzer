import reddit_network
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

def make_dataframe(network:dict, sub_list: [str]):
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
    #the code is very vertical for dataframe parameters for ease of visibility
    dataframe = pd.DataFrame(columns=["start_sub" ,
                                      "end_sub",
                                      "post_id",
                                      "body_check",
                                      "date_posted",
                                      "time_posted" ,
                                      "negative_sentiment",
                                      "num_words",
                                      "num_unique_words",
                                      "num_of_long_words",
                                      "avg_word_length",
                                      "AR_index",
                                      "positive_sentiment_value",
                                      "negative_sentiment_value",
                                      "LWIC_future",
                                      "LIWC_present",
                                      "LIWC_past",
                                      "LWIC_numbers"])

    #have to traverse through 2 dictionaries and edge list (adjacency list for graph network)
    index = 0
    for sub in sub_list:
        linked_subs = network[sub].keys()
        for linked_sub in linked_subs:
            # count the number of times the sub_a a posted a link to sub_b
            for hyperlink in network[sub][linked_sub]:
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

                dataframe.loc[len(dataframe)] = row
                index += 1

    return dataframe
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
    if len(distribution) > 0:
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
            The subreddit we want to make the correlation plot (scatter) for

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
    for linked_sub in all_hyper_links:
        all_links_to_sub = network[sub][linked_sub]
        for link in all_links_to_sub:
            if (link.body_check == body_check):
                y_data.append(link.get_data(y))
                x_data.append(link.get_data(x))
                print(link.get_data(y))

    y_data.pop(0)  # get rid of place holder map value when node is first initialized (not right type)
    x_data.pop(0)
    return y_data, x_data
















