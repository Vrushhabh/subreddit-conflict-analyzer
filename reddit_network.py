

class Subreddit:
    """
       -A class used to represent a subreddit or a node in the reddit network

       -Since the subreddit names are unique you don't need another seperate id to
       identify the node
       ...
       Attributes
       ----------
       _sub_name : str
           name of the subreddit

       """
    def __init__(self, sub_name):
        self._sub_name = sub_name




