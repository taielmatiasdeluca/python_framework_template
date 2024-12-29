from base.models import baseModel
from base.models import fields


class Usuario(baseModel.BaseModel):
    table_name = "dioslli"

    username = fields.Char()
    password = fields.Char()
