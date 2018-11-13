"""
$ pip install jieba
$ pip install wordcloud
$ pip install PIL
"""
# 用jieba成词和权重的字典
import jieba
from PIL._imaging import font
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

font = r'C:\Windows\Fonts\simhei.ttf'

content=jieba.analyse.set_stop_words("data/stop_words.txt")
def tokenize_content(content):
    tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)
    word_tokens_rank = dict()
    for tag in tags:
        word_tokens_rank[tag[0]] = tag[1]
    return word_tokens_rank


"""
第一步 还是去掉一些停用词，例如口语词汇或者意义不大的词，停用词可以自定义，在data目录下的stop_words.txt中。
第二步 按照权重抽取前50个词，并转换成词典的形式。
"""

tags=tokenize_content(content)
def generate_wordcloud(tags, mask):
    word_cloud = WordCloud(width=512, height=512, random_state=10, background_color='white', font_path=font,
                           stopwords=STOPWORDS, mask=mask)

    word_cloud.generate_from_frequencies(tags)
    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
