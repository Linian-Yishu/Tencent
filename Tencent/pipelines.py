# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentPipeline(object):
    def __init__(self):
        '''初始化参数'''
        self.filename = open("tencent.json", "wb")


    def process_item(self, item, spider):
        #转换为 str
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # 写入
        self.filename.write(text.encode("utf-8"))
        return item


    def close_spider(self, spider):
        '''关闭时调用这个方法'''
        self.filename.close()
