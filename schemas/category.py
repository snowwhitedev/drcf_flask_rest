from ma import ma
from models.category import CategoryModel


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        dump_only = ("id",)
