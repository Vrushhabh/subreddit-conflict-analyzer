class Subreddit:

    def __init__(self, sub_name: str):
        self._sub_name = sub_name

    def get_sub(self):
        return self._sub_name

    def __eq__(self, string: str):
        # operator overloading equals so the Subreddit object can be compared to a string
        if self._sub_name == string:
            return True
        else:
            return False


class RedditNetwork:
    """
    -A class used represent the Reddit network of nodes (subreddit) and edges (hyperlink)
    ...

    Attributes
    ----------
    network_map : dict <string, dict<string, list[Hyperlink]>
        We are using an adjacency list to make this network. Subreddit "A" has a connection to Subreddit "B" if sub
        "B" is a key in sub "A"'s dictionary. Since sub can link multiple times to the same sub there is a list of edges
        with alot of information.

    Methods
    ----------
    insert_subreddit (sub: Subreddit):
        inserts subreddit into  network

    insert_hyperlink (start_sub : Subreddit, end_sub : Subreddit, hyperlink : Hyperlink):
        inserts directed hyperlink into the network

    get_hyperlinks (start_sub : Subreddit , end_sub : Subreddit):
        returns all the directed hyperlinks (edges) that go from start_sub to end_sub

    get_hyperlinks (start_sub : Subreddit):
        returns all the hyperlinks that come from one subreddit for analysis
        (can figure out average sub user tendencies)

    get_network ():
        returns the data structure that represents a graph

    """




