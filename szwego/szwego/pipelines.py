# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .items import CollectionProductItem
from mongoengine import connect
from .mongo_models import CollectionProduct


class CollectionProductPipeline:
    def open_spider(self, spider):
        connect(host=spider.settings.get("MONGO_URI"))

    def process_item(self, item, spider):
        if not isinstance(item, CollectionProductItem):
            return item

        model = CollectionProduct(**item)
        model.save()
