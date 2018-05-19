#!/bin/env python3
#-*- encoding: utf-8 -*-

import os
import codecs
import re
from collections import Counter
import jieba
# from conf import nlp_cfg
# from log import g_log_inst as logger


class NLPUtil(object):
    _valid_token_len = 5

    _wordseg_pattern_cfg = [
        re.compile(r'{.*?}', re.U),
    ]

    # _emoji_pattern_cfg = re.compile(r'[\U0001f600-\U0001f9ef]', re.U)
    _emoji_pattern_cfg = re.compile(u'('
        u'\ud83c[\udf00-\udfff]|'
        u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
        u'[\u2600-\u2B55])+', flags=re.UNICODE)

    _replace_pattern_cfg = {
        'float_t': re.compile('\d+\.\d+'),
        'phone_t': re.compile(r'1[0-9\*]{10}|\d{3}[-\s]\d{4}[-\s]\d{4}|\+861[0-9]{10}|[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{4}-[0-9]{7,8}|[8|6][0-9]{7}'),
        'email_t': re.compile(r'[^@|\s]+@[^@]+\.[^@|\s]+'),
    }

    replace_patterns = [
        # ('date_t' , re.compile(ur'\d{2,4}-\d{1,2}-\d{1,2}|\d{2,4}\.\d{1,2}\.\d{1,2}|\d{1,2}\.\d{1,2}|[0-9一二三四五六七八九十]{1,2}月[0-9一二三四五六七八九十]{1,2}[日号]?|[0-9一二三四五六七八九十]{1,2}月[份]?|[0-9一二三四五六七八九十]{1,2}[日号]')),
        # ('time_t' , re.compile(ur'\d{1,2} :\d{1,2}:\d{1,2}|\d{1,2}:\d{1,2}|\d{1,2}点\d{1,2}分?|\d{1,2}点半?')),
        # ('url_t'  , re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]|www\.[.*]\.[cn|com]')),
        ('', re.compile(r'\[.*\]'))
    ]

    _illegal_char_set = set([])

    # init jieba
    jieba.initialize()
    # load user-define dictionary
    # if os.path.exists(nlp_cfg['jieba_dict_fpath']):
    #     with codecs.open(nlp_cfg['jieba_dict_fpath'], 'r', 'utf8') as in_f:
    #         _ = map(lambda x: nlp_cfg['g_ud_words_cfg'].add(x.strip('\n')), in_f.readlines())
    # for w in nlp_cfg['g_ud_words_cfg']:
    #     jieba.add_word(w, freq = 1000000)
    # # print 'load user-define jieba dict success!'
    # # load stopwords
    # if os.path.exists(nlp_cfg['stopword_fpath']):
    #     with codecs.open(nlp_cfg['stopword_fpath'], 'r', 'utf-8') as in_f:
    #         words = map(lambda w: w.strip('\n'), in_f.readlines())
    #         _ = map(lambda x: nlp_cfg['g_stop_words_cfg'].add(x), words)
        # print 'load stopwords success!'

    @classmethod
    def remove_illegal_gbk_char(cls, text_unicode):
        try:
            text_unicode.encode('gbk')
            return text_unicode
        except UnicodeEncodeError as e:
            illegal_ch = e.object[e.start : e.end]
            illegal_set = cls._illegal_char_set
            illegal_set.add(illegal_ch)
            # try to replace directly
            for ch in illegal_set:
                text_unicode = text_unicode.replace(ch, '')
            # remove recursively
            return cls.remove_illegal_gbk_char(text_unicode)

    @classmethod
    def remove_emoji_char(cls, text_unicode):
        res = cls._emoji_pattern_cfg.sub('', text_unicode)
        return res


    # @classmethod
    # def conv_fenc_u8_to_gbk(cls, in_fpath, out_fpath):
    #     try:
    #         with codecs.open(in_fpath, 'r', 'utf-8') as rfd, \
    #             codecs.open(out_fpath, 'w', 'gbk') as wfd:
    #             # read utf8, write gbk
    #             for line in rfd:
    #                 line = cls.remove_illegal_gbk_char(line)
    #                 wfd.write(line)
    #     except Exception as e:
    #         logger.get().warn('errmsg=%s' % (e))

    @classmethod
    def tokenize_via_jieba(cls, text, normalize=True, filter_stop_word = False):
        # remove emoji
        text = cls.remove_emoji_char(text)
        # normalize text
        if normalize:
            text = cls._normalize_text(text)
            # print 'after normalize_text:',text
        tokens = jieba.lcut(text.lower())
        return tokens


    # @classmethod
    # def stat_token_freq(cls, in_fpath, out_fpath):
    #     stop_words = nlp_cfg['g_stop_words_cfg']
    #     try:
    #         word_counter = Counter()
    #         with codecs.open(in_fpath, 'r', 'utf-8') as rfd:
    #             for line in rfd:
    #                 raw_str, word_seg = line.strip('\n').split('\t')
    #                 tokens = word_seg.split()
    #                 tokens = filter(lambda x: x not in stop_words, tokens) 
    #                 tokens = map(cls._normalize_token, tokens)
    #                 for t in tokens:
    #                     if ('{[' not in t) and len(t) <= cls._valid_token_len:
    #                         word_counter[t] += 1
    #                     else:
    #                         logger.get().warn('invalid token, token=%s' % (t))
    #                         # tokenize via jieba 
    #                         for n_t in jieba.cut(t):
    #                             word_counter[n_t] += 1
    #                             logger.get().debug('jieba cut, token=%s' % (n_t))
    #         # dump word_counter
    #         sorted_words = sorted(word_counter.keys(),
    #             key = lambda k: word_counter[k], reverse = True)
    #         with codecs.open(out_fpath, 'w', 'utf-8') as wfd:
    #             for word in sorted_words:
    #                 tmp = '%s\t%s\n' % (word, word_counter[word]) 
    #                 wfd.write(tmp)
    #     except Exception as e:
    #         logger.get().warn('errmsg=%s' % (e))


    @classmethod
    def _normalize_token(cls, token):
        token = token.lower()
        try:
            # 11 usually means phone number
            if len(token) != 11 and token.isdigit():
                token = 'int_t'
            for k, v in cls._replace_pattern_cfg.items():
                if v.match(token):
                    token = k
                    break
            if '{[' not in token:
                return token
            for item in cls._wordseg_pattern_cfg:
                token = item.sub('', token)
            return token
        except Exception as e:
            logger.get().warn('token=%s, errmsg=%s' % (token, e))
            return token

    @classmethod
    def _normalize_text(cls, text): 
        the_patterns = []
        for i,(name, pattern) in enumerate(cls.replace_patterns):
            if pattern.search(text): 
                the_patterns.append((pattern, name))
        if not the_patterns:
            return text
        else:
            replaced_str = text
            for pattern, name in the_patterns:
                replaced_str = re.sub(pattern, name, replaced_str)
            return replaced_str

# if '__main__' == __name__:
#     logger.start('./log/test.log', __name__, 'DEBUG')
    '''
        test tokenize
    '''
    # print '|'.join(NLPUtil.tokenize_via_jieba(u'1月1日到6月30日'))
    # print '|'.join(NLPUtil.tokenize_via_jieba(u'我就问首单红包怎么用不了'))
    # print '|'.join(NLPUtil.tokenize_via_jieba(u'应该是9月9号入住'))
    # print NLPUtil._normalize_text('133****5454')
    # print NLPUtil._normalize_text(u'1月1日到6月30日')
    
    '''
        normalize text
    '''
    # with codecs.open('../data/question/qunar.question.dat', 'r', 'utf8') as in_f, \
    #     codecs.open('../data/question/new_qunar.question.dat', 'w', 'utf8') as out_f:
    #     for line in in_f:
    #         line = line.strip('\n')
    #         line = NLPUtil._normalize_text(line)
    #         out_f.write(line + '\n')
    
