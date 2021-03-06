import gensim
from gensim import models
from gensim import similarities
from gensim import corpora

import numpy as np
import os
import pandas as pd

from pythonModules import preProcess

def get_lsi_scores(query_string, dictionary, lsi_model, lsi_doc_index):
    topK = 5
    query_string_pre_process = preProcess.pre_process_sent(query_string)[0]
    query_string_bow = dictionary.doc2bow(query_string_pre_process)
    query_lsi = lsi_model[query_string_bow]
    sims = lsi_doc_index[query_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    scores=[]
    for idx,score in enumerate(sims[:topK]):
        scores.append([score[0],score[1]])
    return scores
