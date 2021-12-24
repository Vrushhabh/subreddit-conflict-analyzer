import string

from hyperlink import Hyperlink

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
    make_network (file: name):
        makes network from dataset tsv (txt) file
    insert_subreddit (sub: string):
        inserts subreddit into  network

    insert_hyperlink (start_sub : string, end_sub : string, hyperlink : Hyperlink):
        inserts directed hyperlink into the network

    get_hyperlinks (start_sub : string , end_sub :string)
        returns all the directed hyperlinks (edges) that go from start_sub to end_sub

    get_hyperlinks (start_sub : Subreddit):
        returns all the hyperlinks that come from one subreddit for analysis
        (can figure out average sub user tendencies)

    get_network ():
        returns the data structure that represents a graph

    """

    def __init__(self):
        self.network_map = {}

    def make_network(self, string_path, body_check=True):
        with open(string_path) as f:
            # makes block of the data from the test cvs file that gets turned into a edge
            hyperlink_blocks = f.readlines()
        f.close()
        index = 1
        while index < len(hyperlink_blocks):
            hyperlink = Hyperlink(hyperlink_blocks[index], body_check)
            self.insert_subreddit(hyperlink.start_sub)
            self.insert_hyperlink(hyperlink.start_sub, hyperlink.end_sub, hyperlink)
            index += 1

    def insert_subreddit(self, sub: string):
        if (self.network_map.get(sub) is  None):
            h_list = []
            self.network_map[sub] = {}
            #just giving a place holder value
            self.network_map[sub][""] = h_list

    def insert_hyperlink(self, start_sub: string, end_sub: string, hyperlink:Hyperlink):
        #two cases if the starting_sub already linked the previous sub or if it doesn't in which it creates a new list
        if (self.network_map.get(start_sub) is not None):
            if (self.network_map.get(start_sub).get(end_sub) is None):
                hyper_list = list()
                hyper_list.append(hyperlink)
                self.network_map.get(start_sub, None).update({end_sub : hyper_list})
            else:
                self.network_map.get(start_sub).get(end_sub).append(hyperlink)

    def get_network(self):
        #basic getter
        return self.network_map











