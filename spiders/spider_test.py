# -*- coding: utf-8 -*-
"""
Created on 2023-04-14 17:39:29
---------
@summary:
---------
@author: xue
"""

import feapder
from pyquery import PyQuery as pq
from items.local_policy_item import LocalPolicyItem
class SpiderTest(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    # __custom_setting__ = dict(
    #     REDISDB_IP_PORTS="localhost:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    # )

    def start_requests(self):
        for page in range(0, 22):
            yield feapder.Request(
                "http://sousuo.gov.cn/column/30469/{}.htm?".format(page)
            )

    def parse(self, request, response):
        for i in range(0, 20):
            doc = pq(response.text)
            _title = doc('a').eq(i).text()
            date = doc('span.date').eq(i).text()
            tile = _title + '_' + date
            source = doc('a').eq(i).attr('href')
            yield feapder.Request(
                source,
                callback=self.parse_detail,
                metadata={"tile": tile, "source": source},
            )
    def parse_detail(self, request, response):
        # doc = pq(response.text)
        content = response.text
        yield LocalPolicyItem(
            content=content,
            tile=request.metadata["tile"],
            source=request.metadata["source"],
        )

from pyquery import PyQuery
if __name__ == "__main__":
    SpiderTest(redis_key="yyy").start()
    #pip输出到文件命令


    #pip install -r requirements.txt -t ./lib
