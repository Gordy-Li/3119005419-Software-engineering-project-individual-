import numpy as np
import re
import jieba
import warnings

warnings.filterwarnings('ignore')


class Text(object):
    def __init__(self, text_route):
        self.text_route = text_route

    def get_word_list(self, num=0):
        with open(self.text_route, 'r', encoding='utf-8') as f:
            text = f.read()
        if num == 1:
            print('分字\n')
            res = re.compile(r"([\u4e00-\u9fa5])")  # 正则包根据单个中文文字分割字符串
            text_list_init = res.split(text)
        else:
            print('分词\n')
            text_list_init = jieba.lcut(text)  # jieba包根据词语分割字符串
        text_list_result = []
        for literacy in text_list_init:
            if '\u4e00' <= literacy <= '\u9fa5':  # 除去非中文的列表元素
                text_list_result.append(literacy)
        return text_list_result


def get_word_vector(word_list1, word_list2):
    key_word = list(set(word_list1 + word_list2))
    # 给定形状和类型的用0填充的矩阵存储向量
    word_vector1 = np.zeros(len(key_word))
    word_vector2 = np.zeros(len(key_word))
    # 计算词频
    # 依次确定向量的每个位置的值
    for i in range(len(key_word)):
        # 遍历key_word中每个词在句子中的出现次数
        for j in range(len(word_list1)):
            if key_word[i] == word_list1[j]:
                word_vector1[i] += 1
        for k in range(len(word_list2)):
            if key_word[i] == word_list2[k]:
                word_vector2[i] += 1
    return word_vector1, word_vector2


def cos_dist(vector1, vector2):
    # 返回向量余弦相似度
    dist = float(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
    return dist


if __name__ == '__main__':
    # 'C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig.txt'
    # 'C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig_0.8_add.txt'
    text1 = Text(input('请输入第一个文本的绝对路径: '))
    text2 = Text(input('请输入第二个文本的绝对路径: '))
    vec1, vec2 = get_word_vector(text1.get_word_list(), text2.get_word_list())
    distance = cos_dist(vec1, vec2)
    print('文本重复率为:' + str(distance))
