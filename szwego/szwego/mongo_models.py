import mongoengine as db
from mongoengine import EmbeddedDocument
from datetime import datetime


class Base(db.Document):
    meta = {
        'abstract': True,
    }

    create_time = db.DateTimeField(default=datetime.now)
    modified_time = db.DateTimeField(default=datetime.now)
    delete_time = db.DateTimeField(default=None)


class GoodsAttribute(EmbeddedDocument):
    attribute_name = db.StringField(required=True)
    attribute_value = db.StringField(required=True, default="")


class Goods(EmbeddedDocument):
    sku = db.StringField()
    weight = db.IntField()
    price = db.FloatField()
    goods_image = db.StringField()
    goods_attrs = db.ListField(db.EmbeddedDocumentField(GoodsAttribute))
    goods_extra_image = db.ListField(db.StringField())

    def get_attr(self, key):
        """
        获取goods的属性key的值
        :param key:
        :return: str|None
        """
        attrs = {}
        for attr in self.goods_attrs:
            attr_key = attr.attribute_name.strip() if isinstance(attr.attribute_name, str) else attr.attribute_name
            value = attr.attribute_value.strip() if isinstance(attr.attribute_value, str) else attr.attribute_value
            attrs[attr_key] = value
        return attrs.get(key, None)


class SizeChart(EmbeddedDocument):
    key = db.StringField(required=True)
    value = db.StringField(required=True)


class Supplier(EmbeddedDocument):
    supplier_site = db.StringField()
    supplier_name = db.StringField()
    supplier_platform = db.StringField()


class CollectionProduct(Base):
    batch_number = db.StringField(max_length=64)
    supplier = db.EmbeddedDocumentField(Supplier)
    name = db.StringField(max_length=1024)
    spu = db.StringField(required=True)
    create_user_id = db.IntField()
    create_user_name = db.IntField()
    colors = db.ListField(db.StringField())
    size_chart = db.ListField(db.EmbeddedDocumentField(SizeChart))
    main_picture = db.StringField()
    product_extra_image = db.ListField(db.StringField())
    product_gallery = db.ListField(db.StringField())
    product_description = db.StringField()
    goods_list = db.ListField(db.EmbeddedDocumentField(Goods))
    product_source = db.StringField()
    category = db.ListField(db.StringField())
