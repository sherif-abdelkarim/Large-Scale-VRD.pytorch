import os
import torch.nn as nn
import torch
from torch.autograd import Variable
import numpy as np
import logging
from six.moves import cPickle as pickle

from core.config import cfg
from modeling.get_dataset_counts_rel import get_rel_counts
import sparray
import sparse

logger = logging.getLogger(__name__)


# def add_one_to_bg(arr):
# 	keys = arr.__data.keys()

def concatenate_sp(arr1, arr2):
    for i in arr1.shape[0]:
        for j in arr1.shape[1]:
            arr1[i, j, 0] = arr2[i, j]
    return arr1


class FrequencyBias(nn.Module):
    """
    The goal of this is to provide a simplified way of computing
    P(predicate | obj1, obj2, img).
    """

    def __init__(self, ds_name, eps=1e-3):
        super(FrequencyBias, self).__init__()

        if ds_name.find('vg') >= 0:
            ds_name = 'vg'
        elif ds_name.find('vrd') >= 0:
            ds_name = 'vrd'
        else:
            raise NotImplementedError

        if cfg.MODEL.USE_OVLP_FILTER:
            must_overlap = True
        else:
            must_overlap = False
        sparse_fg_matrix, sparse_bg_matrix = get_rel_counts(ds_name, must_overlap=must_overlap)
        sparse_bg_matrix += 1
        sparse_fg_matrix = sparse.COO(concatenate_sp(sparse.DOK(sparse_fg_matrix), sparse.DOK(sparse_bg_matrix)))

        pred_dist = np.log(sparse_fg_matrix / (sparse_fg_matrix.sum(2)[:, :, None] + 1e-08) + eps)

        self.num_objs = pred_dist.shape[0]
        pred_dist = torch.FloatTensor(pred_dist).view(-1, pred_dist.shape[2])

        self.rel_baseline = nn.Embedding(pred_dist.size(0), pred_dist.size(1))
        self.rel_baseline.weight.data = pred_dist
        
        logger.info('Frequency bias tables loaded.')

    def rel_index_with_labels(self, labels):
        """
        :param labels: [batch_size, 2] 
        :return: 
        """
        return self.rel_baseline(labels[:, 0] * self.num_objs + labels[:, 1])
