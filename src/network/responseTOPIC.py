import openai

def promptTopicToGPT(user_action, config):

    NUMBER_RESPONSES = 1 if len(user_action) < 150 else 2

    try:

        response = openai.ChatCompletion.create(
                    model=config['MODEL'],
                    max_tokens=config['MAX_TOKENS'],
                    temperature=config['TEMPERATURE'],
                    messages=[{"role":"system", "content": getPrompts("topic_selector")},
                    {"role":"user", "content":f"[{user_action}]"}]
                    ,
                    n=NUMBER_RESPONSES
                )

        get_response = response.choices[0].message.content

        return getPrompts(f"topic_prompts/{get_response}")

    except Exception as e:
        print(e)
        return None
    
def getPrompts(file_path):
    with open(f"./settings/{file_path}.txt", "r") as Topic:
        getText = Topic.readlines()
        Topic.close()
        return " ".join(getText)