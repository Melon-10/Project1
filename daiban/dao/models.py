from tortoise import Model,fields

class Todo(Model):
    id=fields.IntField(pk=True)
    content=fields.CharField(max_length=500)
    create_at=fields.DatetimeField(auto_now_add=True)
    updated_at=fields.DatetimeField(auto_now=True)