from text import Text
import numpy as np


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


def main():
    # 'C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig.txt'
    # 'C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig_0.8_add.txt'
    text1 = Text(input('请输入第一个文本的绝对路径C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig.txt:\n'))
    text2 = Text(input('请输入第二个文本的绝对路径C:/Users/allmi/Desktop/软件工程作业/软件工程个人作业/测试文本2/orig_0.8_add.txt:\n'))
    vec1, vec2 = get_word_vector(text1.get_word_list(), text2.get_word_list())
    distance = cos_dist(vec1, vec2)
    print(f'文件重复率为{distance:.2f}')
    print('答案文件的路径为：C:/Users/allmi/Desktop/result.txt')
    filename = 'C:/Users/allmi/Desktop/result.txt'
    with open(filename, 'w') as f:
        f.write(f'文件重复率为{distance:.2f}')
    input('press to quit')


if __name__ == '__main__':
    main()
