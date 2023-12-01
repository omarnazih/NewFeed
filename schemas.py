from marshmallow import Schema, fields, validate

class PostSchema(Schema):
    """Schema for a post."""    
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.String(validate=validate.Length(min=1), required=True)

class PostUpdateSchema(Schema):
    """Schema for updating a post."""    
    title = fields.Str()
    content = fields.String(validate=validate.Length(min=1))