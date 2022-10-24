def format_persons_response(persons):
    """formate the responses of get persons"""
    return [{
        "id": person[0].id,
        "name": person[0].name,
        "email": person[0].email
    } for person in persons]


def format_vehicles_response(vehicles):
    """format vehicles joined to persons"""
    return [
        {
            "id": vehicle[0].id,
            "model": vehicle[0].model,
            "color": vehicle[0].color,
            "created_at": vehicle[0].created_at,
            "updated_at": vehicle[0].created_at,
            "person": {
                "id": vehicle[1].id,
                "name": vehicle[1].name,
                "email": vehicle[1].email
            }
        } for vehicle in vehicles
    ]
