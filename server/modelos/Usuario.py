from base.models import baseModel
from base.models import fields


class Usuario(baseModel.BaseModel):
    table_name = "dioslli"

    username = fields.Char(length=10)
    password = fields.Char()
