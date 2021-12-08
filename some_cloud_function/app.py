from people_app import add_user


def handler(event, context):
    all_users = add_user(event['name'], event['last_name'])
    return [
        {'id': user.id, 'name': user.name, 'last_name': user.last_name}
        for user in all_users
    ]
