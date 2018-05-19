#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-31 15:33:40
# @Author  : AlexTang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
# @Description : 

# from conf import wmd_sim_cfg
# from log import g_log_inst as logger
from nlp_util_py3 import NLPUtil
from gensim import models
from gensim.similarities import WmdSimilarity

class WmdUtil(object):

    # _w2v_model = models.KeyedVectors.load_word2vec_format(wmd_sim_cfg['w2v_fpath'], binary=False)
    _w2v_model = models.KeyedVectors.load_word2vec_format('v1.w2v_sgns_min2_win1_d80_it7.kv', binary=False)
    _w2v_model.init_sims(replace=True)

    @classmethod
    def get_sims(cls, question, documents):
        keywords = NLPUtil.tokenize_via_jieba(question)
        # print(keywords)
        documents = NLPUtil.tokenize_via_jieba(documents)
        # print(keywords)
        # print(documents)
        score = cls._w2v_model.wmdistance(keywords, documents)
        return score
    #     wmd_inst = cls.get_wmd_inst(documents)
    #     similar_docs = wmd_inst[keywords]
    #     print(similar_docs)
    #     return similar_docs[0][1]

    # @classmethod
    # def get_wmd_inst(cls, documents):
    #     wmd_corpus = map(NLPUtil.tokenize_via_jieba, documents)
    #     wmd_inst = WmdSimilarity(list(wmd_corpus), cls._w2v_model,
    #         num_best=3,
    #         normalize_w2v_and_replace=False)
    #     return wmd_inst

def test():
    doc      = '纽斯汗蒸会所'
    doc_data = '纽斯商务宾馆（解放路总店）'

    print(10000 if WmdUtil.get_sims(doc, doc_data) > 10000 else WmdUtil.get_sims(doc, doc_data))

if __name__ == '__main__':
    # logger.start('../log/wmd_util.log', name=__name__, level='DEBUG')
    test()
