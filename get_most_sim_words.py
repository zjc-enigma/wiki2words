#!/usr/bin/python
# coding:utf8

import sys
import gensim
vec_file = "../all_vector"

model = gensim.models.Word2Vec.load_word2vec_format(vec_file, binary=False)

disease_list = ['xingbing',
                'baidianfeng',
                'dianxian',
                'nanke']
src_dir = "../data/"
dest_dir = "../out/"

def get_most_sim_list(word):
    ret = ""
    try:
        ret = model.most_similar(word.decode('utf8'))
    except Exception , e:
        print e
        return ret

    res = []
    for item in ret:
        res.append(item[0].encode('utf8'))

    return res


for disease in disease_list:
    src_file = src_dir + disease
    dest_file = dest_dir + disease
    w = open(dest_file, 'w')
    f = open(src_file)


    for word in f:
        w.write(word)
        word = word.strip('\n')
        ret_list = get_most_sim_list(word)
        if ret_list != "":
            for ret in ret_list:
                w.write(ret + '\n')
    w.close()
    f.close()
