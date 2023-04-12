def validTopic(topic:str):
    import re

    return re.match(r"\[.*\]", topic)