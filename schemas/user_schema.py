user_list_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"},
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        }
    },
    "required": ["page", "data"]
}