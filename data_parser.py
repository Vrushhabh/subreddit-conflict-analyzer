from reddit_network import RedditNetwork
import network_analyzer
import matplotlib.pyplot as plt

mega_network = RedditNetwork()
#first make network from hyperlink from bodies of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-body1.tsv")

#second grow network from hyperlinks from titles of posts
mega_network\
    .make_network("/Users/vrushhabh/PycharmProjects/subreddit-conflict-graph-analyzer/soc-redditHyperlinks-title.tsv"
                  ,False)

#def extract_violin_plt_data(network: dict, sub:str, body_check=True, neg_sentiment=True, data_type="num_words")
dict, subs_with_most_activity = network_analyzer.rank_activity(mega_network.get_network())
#print(subs_with_most_activity)
sub_with_most_activity = subs_with_most_activity[0]
sub2 = subs_with_most_activity[3]
sub3 = subs_with_most_activity[4]
body_t = True
body_check = body_t

data_t = "num_unique_words"
word_count=network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub_with_most_activity, data_type= data_t,body_check = body_t)

word_count1= network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub_with_most_activity, neg_sentiment = False,data_type=data_t,body_check = body_t)

word_count2=network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub2,data_type=data_t,body_check = body_t)

#
word_count3= network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub2, neg_sentiment = False,data_type=data_t,body_check = body_t)

word_count4=network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub3,data_type=data_t,body_check = body_t)

#
word_count5= network_analyzer.extract_violin_plt_data(mega_network.get_network(), sub3, neg_sentiment = False,data_type=data_t,body_check = body_t)
fig, (ax7, ax8, ax9, ax10, ax11, ax12) = plt.subplots(nrows=1, ncols=6)
#ax1, ax2, ax3, ax4, ax5, ax6,
# ax1.violinplot(word_count, showmedians=True)
# ax1.set_title('Negative Sentiment')
# # plt.show()
# # Plot violin plot on axes 2
# ax2.violinplot(word_count1, showmedians=True)
# ax2.set_title('Positive Sentiment')
#
# ax3.violinplot(word_count2, showmedians=True)
# ax3.set_title('Negative Sentiment')
#
# ax4.violinplot(word_count3, showmedians=True)
# ax4.set_title('Postitive Sentiment')
#
# ax5.violinplot(word_count4, showmedians=True)
# ax5.set_title('Negative Sentiment')
#
# ax6.violinplot(word_count5, showmedians=True)
# ax6.set_title('Postitive Sentiment')


ax12.boxplot(word_count)
ax12.set_title('Negative Sentiment')

ax7.boxplot(word_count1)
ax7.set_title('Positive Sentiment')

ax8.boxplot(word_count2)
ax8.set_title('Negative Sentiment')

ax9.boxplot(word_count3)
ax9.set_title('Postitive Sentiment')

ax10.boxplot(word_count4)
ax10.set_title('Negative Sentiment')

ax11.boxplot(word_count5)
ax11.set_title('Postitive Sentiment')

plt.show()

