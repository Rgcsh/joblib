# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren <rgc@bvrft.com>
All rights reserved
create time '2021/2/23 15:58'

Usage:

"""
import logging
import multiprocessing as mp


def mp_util_info(msg):
    """

    """
    msg = f'joblib:{msg}'
    logging.info(msg)
    mp.util.info(msg)


def mp_util_debug(msg):
    """

    """
    msg = f'joblib:{msg}'
    logging.debug(msg)
    mp.util.debug(msg)
