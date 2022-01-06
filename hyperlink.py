class Hyperlink:
    """
    -A class used represent a link in a body (in a starting subreddit) of a post that leads to another subreddit
    -Another file was used for less messiness because SNAP reddit dataset has a lot of the information in the edges (which is good because
    more analysis can be done)
    ...

    Attributes (there are alot (I even cut some ones that I thought were even more irrelevant out from the original
    data set) so I put a * by the interesting ones)
    ----------
    start_sub : str
        the subreddit that the link comes from

    end_sub : str
        the subreddit that the link takes you to

    body_check : bool
    This just lets us know if we are dealing with a link from the body or title of the post

    post_id : str *
        You have a chance (sometimes posts get deleted) of  finding the post that the link relates too if you put in
        https://www.reddit.com/r/<start_sub>/comments/<post_id> into the google search bar
        this is fun because you can see if you agree with the scores that this dataset assigns to the post (most of
        the times it does which is cool because most of data was determined by an algorithm and was not manuel)

    date_posted : str
        The date the link was posted

    time_posted : str
        The time the link was posted

    negative_sentiment : bool *
        This sentiment variable lets us know if there is some type of conflict or controversy in the post relating
        to the post from another sub. This sentiment was calculated from a trained text based classifier.
        More info in the paper right below

        S. Kumar, W.L. Hamilton, J. Leskovec, D. Jurafsky.
        Community Interaction and Conflict on the Web. World Wide Web Conference, 2018.

    char_total : int
        the total amount of characters in the body of the post

    char_total_no_spaces : int
        the amount of characters that aren't spaces

    fraction_of_digits : float *
        this is the percentage of the post that are numbers (more numbers in most cases might mean there are more
        statistics in the post)

    fraction_of_special_chars : float
        this is the number of special characters like ", ! ?" in the post.

    num_words : int
        num of words in the post

    num_unique_words : int *
        this can tell us about the vocabulary of the average user in a subreddit if there are enough posts

    num_of_long_words : int *
        the number of long words (6 letters or more) in a post

    avg_word_length : float *
        average word length in a post

    num_of_sentences : int
        average num of sentences in a post

    AR_index: int *
        Readability score ( that can give a rough idea of what age group the text is ment for

    positive_sentiment_value : float *
        How positive the post was according to VADER (Valence Aware Dictionary for sEntiment Reasoning.)

    negative_sentiment_value : float *
        How negative the post was according to VADER (Valence Aware Dictionary for sEntiment Reasoning.)

    LIWC_future : float *
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to the future.

    LIWC_present : float *

    LIWC_past : float *

    LIWC_numbers : float

    LIWC_social : float

    LIWC_posemo : float *
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to positive language
        This was what the label was named in the data set.

    LIWC_negemo : float *
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to negative language

    Methods
    ----------
    get_data (instance_var: str):
        This function is made like this to reduce repeating code in network_analyzer.py. This function will get slowly
        get updated on the basis if I need a specific field for analysis (plus there is alot of data and it seems
        unnecessary and daunting to add functionality for every field from the start)
    """

    # there are alot of instance variables so we can't just add 20 arguments because of readability
    def __init__(self, cvs_data: str, body: bool):
        """
       Constructs all the necessary attributes for the hyperlink

       Parameters
       ----------
       cvs : str
           The block of data(representing a hyperlink) gotten from the big tsv data

       """
        # if the link is in the title we will change it shortly after
        self.body_check = body
        data_index = cvs_data.split()

        # taking a block of the big TSV file that represents a edge and contructing a hyperlink from how the
        # data was formatted
        self.start_sub = data_index[0]
        self.end_sub = data_index[1]
        self.post_id = data_index[2]
        self.date_posted = data_index[3]
        self.time_posted = data_index[4]
        self.negative_sentiment = True if int(data_index[5]) == -1 else False

        data_points = data_index[6].split(",")

        self.char_total = int(float(data_points[0]))
        self.char_total_no_spaces = int(float(data_points[1]))
        self.fraction_of_digits = float(data_points[3])
        self.fraction_of_special_chars = float(data_points[6])
        self.num_words = int(float(data_points[7]))
        self.num_unique_words = int(float(data_points[8]))
        self.num_of_long_words = int(float(data_points[9]))
        self.avg_word_length = float(data_points[10])
        self.num_of_sentences = int(float(data_points[13]))
        self.AR_index = float(data_points[17])
        self.positive_sentiment_value = float(data_points[18])
        self.negative_sentiment_value = float(data_points[19])

        # LIWC data points
        self.LIWC_future = float(data_points[35])
        self.LIWC_present = float(data_points[34])
        self.LIWC_past = float(data_points[33])
        self.LIWC_numbers = float(data_points[41])
        self.LIWC_social = data_points[43]
        self.LWIC_posemo = data_points[48]
        self.LWIC_negemo = data_points[49]

    def get_data(self, instance_var: str):
        if (instance_var == "num_words"):
            return self.num_words
        elif (instance_var == "num_unique_words"):
            return self.num_unique_words
        elif (instance_var == "LWIC_negemo"):
            return self.LWIC_negemo
        elif (instance_var == "fraction_of_digits"):
            return self.fraction_of_digits
        elif (instance_var == "num_of_sentences"):
            return self.num_of_sentences
        elif (instance_var == "negative_sentiment_value"):
            return self.negative_sentiment_value

