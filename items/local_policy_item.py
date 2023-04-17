# -*- coding: utf-8 -*-
"""
Created on 2023-04-14 17:48:15
---------
@summary:
---------
@author: xue
"""

from feapder import UpdateItem


class LocalPolicyItem(UpdateItem):
    """
    This class was generated by feapder
    command: feapder create -i local_policy 1
    """

    __table_name__ = "local_policy"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.content = kwargs.get('content')
        # self.id = kwargs.get('id')
        self.source = kwargs.get('source')
        self.tile = kwargs.get('tile')