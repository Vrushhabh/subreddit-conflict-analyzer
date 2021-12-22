class Hyperlink:
    """
    -A class used represent a link in a body (in a starting subreddit) of a post that leads to another subreddit
    -Another class was used because SNAP reddit dataset has a lot of the information in the edges (which is good because
    more analysis can be done)
    ...

    Attributes
    ----------
    start_sub : str
        the subreddit that the link comes from
    end_sub : str
        the subreddit that the link takes you to
    negative_sentiment : bool
        This sentiment variable lets us know if there is some type of conflict or controversy in the post relating
        to the post from another sub. This sentiment was calculated from a trained text based classifier.
        More info in the paper right below

        S. Kumar, W.L. Hamilton, J. Leskovec, D. Jurafsky.
        Community Interaction and Conflict on the Web. World Wide Web Conference, 2018.

    post_id: str
        You have a chance of posting this into the google search bar and finding the post that the link relates too
        this is fun because you can see if you agree with the scores that this dataset assigns to the post (most of
        the times it does which is cool because most of data was determined by a algorothm)

    char_total : int
        the total amount of characters in the body of the post

    char_total_no_spaces : int
        the amount of characters that aren't spaces

    fraction_of_digits : double
        this is the percentage of the post that are numbers (more numbers in most cases might mean there are more
        statistics in the post)

    fraction_of_special_chars : double
        this is the number of special characters like ", ! ?" in the post.

    num_words : int
        num of words in the post

    num_unique_words : int
        this can tell us about the vocabulary of the average user in a subreddit if there are enough posts

    num_of_long_words : int
        the number of long words (6 letters or more) in a post

    avg_word_length : double
        average word length in a post

    avg_num_of_sentences : int
        average num of sentences in a post

    AR_index: int
        Readability score ( that can give a rough idea of what age group the text is ment for

    positive_sentiment : double
        How positive the post was according to VADER (Valence Aware Dictionary for sEntiment Reasoning.)

    negative_sentiment : double
        How negative the post was according to VADER (Valence Aware Dictionary for sEntiment Reasoning.)

    LIWC_future : double
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to the future.

    LIWC_present : double

    LIWC_past : double

    LIWC_numbers : double

    LIWC_social : double

    LIWC_posemo : double
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to positive language
        This was what the label was named in the data set

    LIWC_negemo : double
        Linguistic Inquiry and Word Count (LIWC) gives the percentage of words relating to negative language
    """
