# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Collection of available datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from core.config import cfg

# Path to data dir
_DATA_DIR = cfg.DATA_DIR

# Required dataset entry keys
IM_DIR = 'image_directory'
ANN_FN = 'annotation_file'
ANN_FN2 = 'annotation_file2'
ANN_FN3 = 'predicate_file'
# Optional dataset entry keys
IM_PREFIX = 'image_prefix'
DEVKIT_DIR = 'devkit_directory'
RAW_DIR = 'raw_dir'

# Available datasets
DATASETS = {
    # VG dataset
    'vg_train': {
        IM_DIR:
            _DATA_DIR + '/vg/VG_100K',
        ANN_FN:
            _DATA_DIR + '/vg/detections_train.json',
        ANN_FN2:
            _DATA_DIR + '/vg/rel_annotations_train.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # for now vg_val is identical to vg_test
    'vg_val': {
        IM_DIR:
            _DATA_DIR + '/vg/VG_100K',
        ANN_FN:
            _DATA_DIR + '/vg/detections_val.json',
        ANN_FN2:
            _DATA_DIR + '/vg/rel_annotations_val.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # VG80k dataset
    'vg80k_train': {
        IM_DIR:
            _DATA_DIR + '/vg/VG_100K',
        ANN_FN:
            _DATA_DIR + '/vg_80k/detections_train.json',
        ANN_FN2:
            _DATA_DIR + '/vg_80k/rel_annotations_train.json',
        ANN_FN3:
            _DATA_DIR + '/vg_80k/predicates.json',
    },
    # for now vg_val is identical to vg_test
    'vg80k_val': {
        IM_DIR:
            _DATA_DIR + '/vg/VG_100K',
        ANN_FN:
            _DATA_DIR + '/vg_80k/detections_val.json',
        ANN_FN2:
            _DATA_DIR + '/vg_80k/rel_annotations_val.json',
        ANN_FN3:
            _DATA_DIR + '/vg_80k/predicates.json',
    },
    # VRD dataset
    'vrd_train': {
        IM_DIR:
            _DATA_DIR + '/vrd/train_images',
        ANN_FN:
            _DATA_DIR + '/vrd/detections_train.json',
        ANN_FN2:
            _DATA_DIR + '/vrd/new_annotations_train.json',
        ANN_FN3:
            _DATA_DIR + '/vrd/predicates.json',
    },
    'vrd_val': {
        IM_DIR:
            _DATA_DIR + '/vrd/val_images',
        ANN_FN:
            _DATA_DIR + '/vrd/detections_val.json',
        ANN_FN2:
            _DATA_DIR + '/vrd/new_annotations_val.json',
        ANN_FN3:
            _DATA_DIR + '/vrd/predicates.json',
    },
    # tvqa bbt dataset
    'tvqa_vg_bbt_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_bbt_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_bbt_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_bbt_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_bbt_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_bbt_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_bbt1_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_bbt_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_bbt1_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_bbt2_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_bbt_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_bbt2_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # tvqa house dataset
    'tvqa_vg_house_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_house_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_house_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_house_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_house_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_house_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_house1_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_house_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_house1_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_house2_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_house_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_house2_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_house3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_house_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_house3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # tvqa castle dataset
    'tvqa_vg_castle_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_castle_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_castle_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_castle_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_castle_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_castle_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_castle1_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_castle_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_castle1_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_castle2_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_castle_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_castle2_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_castle3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_castle_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_castle3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # tvqa friends dataset
    'tvqa_vg_friends_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_friends_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_friends_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_friends_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_friends_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_friends_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_friends1_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_friends_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_friends1_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_friends2_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_friends_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_friends2_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_friends3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_friends_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_friends3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # tvqa grey dataset
    'tvqa_vg_grey_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_grey_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_grey_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_grey_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_grey_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_grey_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    # tvqa met dataset
    'tvqa_vg_met_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_met_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_met_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
    'tvqa_vg_met_2nd_of_3_test': {
        IM_DIR:
            _DATA_DIR + '/tvqa/tvqa_all_frames',
        ANN_FN:
            _DATA_DIR + '/tvqa/dummy_met_vg_detections_test.json',
        ANN_FN2:
            _DATA_DIR + '/tvqa/dummy_met_2nd_of_3_vg_rel_annotations_test.json',
        ANN_FN3:
            _DATA_DIR + '/vg/predicates.json',
    },
}
