#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.jianshu.com/p/2052d21a704c
"""

import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    content = open("/tmp/ana", "rb").read()

    #tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text = " ".join(tags)
    text = unicode(text)
    print text
    exit()
    
    #read the mask
    d = path.dirname(__file__)
    text_coloring = imread(path.join(d, "test.jpg"))
    wc = WordCloud(font_path='simsun.ttc',
        background_color="white", max_words=300, mask=text_coloring,
        max_font_size=40, random_state=42)

    #generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(text_coloring)

    plt.imsave(wc)
    plt.axis("off")

