# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CollectionProductItem(scrapy.Item):
    batch_number = scrapy.Field()
    supplier = scrapy.Field()
    name = scrapy.Field()
    spu = scrapy.Field()
    create_user_id = scrapy.Field()
    create_user_name = scrapy.Field()
    colors = scrapy.Field()
    size_chart = scrapy.Field()
    main_picture = scrapy.Field()
    product_extra_image = scrapy.Field()
    product_gallery = scrapy.Field()
    product_description = scrapy.Field()
    goods_list = scrapy.Field()
    product_source = scrapy.Field()
    category = scrapy.Field()
