import scrapy
from urllib.parse import urlencode
from scrapy.http import JsonRequest
from ..items import CollectionProductItem
from datetime import datetime
import time


class WeishangxiangceSpider(scrapy.Spider):
    name = 'weishangxiangce'
    allowed_domains = ['szwego.com']
    start_url = 'https://www.szwego.com/album/personal/all'

    def start_requests(self):
        album_id = self.settings.attributes.get("ALBUM_ID").value
        batch_number = str(int(time.time())) + "_" + album_id
        params = {
            "albumId": album_id,
            "searchValue": "",
            "searchImg": "",
            "startDate": "",
            "endDate": "",
            "sourceId": "",
            "requestDataType": "",
            "transLang": "en",
        }
        data = {
            "tagList": "%5B%5D"
        }
        url = self.start_url + "?" + urlencode(params)

        yield JsonRequest(url, data=data, callback=self.parse, meta={"batch_number": batch_number})

    def parse(self, response):
        data = response.json()
        if data.get("success") == False:
            raise RuntimeError(data.get('errmsg'))
        result = data.get("result")
        supplier = {
            "supplier_site": result.get("share").get("path"),
            "supplier_name": result.get("share").get("posterTitle"),
            "supplier_platform": "微商相册",
        }

        for item in result.get("items"):
            size_chart = []
            if item.get("formats"):
                for format in item.get("formats"):
                    size_chart.append({
                        "key": format.get("formatName"),
                        "value": format.get("formatType"),
                    })

            colors = []
            if item.get("colors"):
                for color in item.get("colors"):
                    colors.append(color.get("formatName"))

            category = []
            for tag in item.get("tags"):
                category.append(tag.get("tagName"))

            item_data = {
                "batch_number": response.meta.get("batch_number"),
                "supplier": supplier,
                "name": item.get("title"),
                "spu": item.get("parent_goods_id"),
                "colors": colors,
                "size_chart": size_chart,
                "main_picture": item.get("imgsSrc")[0] if item.get("imgsSrc") else None,
                "product_extra_image": item.get("imgsSrc"),
                "product_gallery": item.get("imgsSrc"),
                "product_description": "",
                "goods_list": [],
                "product_source": "https://www.szwego.com/" + item.get("link"),
                "category": category
            }

            yield CollectionProductItem(**item_data)
