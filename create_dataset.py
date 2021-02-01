# slugify
non_alpha_num_char = ['"', '#', '$', '%', '&', '+',
                    ',', '/', ':', ';', '=', '?',
                    '@', '[', '\\', ']', '^', '`',
                    '{', '|', '}', '~', "'"]
def slugify(text):
    """
    Turn the text content of a header into a slug for use in an ID
    """
    non_safe = [c for c in text if c in non_alpha_num_char]
    if non_safe:
        for c in non_safe:
            text = text.replace(c, '')
    # Strip leading, trailing and multiple whitespace, convert remaining whitespace to _
    text = u'_'.join(text.split())
    return text


user_events = dict()
# structure of user_events
#     user_events = {
#         'user_id': {
#             'slug_event_name': count
#         } 
#     }
def create_datastructure(data):
    for d in data:
        user_id = d.get('properties').get('user_id')
        event = d.get('event')

    #     slugify event name for uniqueness
        slug_event_name = slugify(event)
    #     loop through
        if not user_events.get(user_id):
            user_events[user_id] = dict()

        if not user_events.get(user_id).get(slug_event_name):
            user_events[user_id][slug_event_name] = 0


        user_events[user_id][slug_event_name] += 1

    return user_events