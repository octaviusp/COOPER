import openai
import re
from executor import executeScript, voiceAnswer
from helpers import errors
#from responseTOPIC import promptTopicToGPT

def promptDataToGPT(action_prompt: str, context: dict[str, str]):
        
        if not context or not action_prompt:
                errors.invalidRequest()

        is_code = False

        promptGuide = promptTopicToGPT(action_prompt, context)
        print(promptGuide)
        if promptGuide.find("python") != -1:
                is_code = True
                promptGuide += "\n" + getPrompts("python_structure/python_code")
        print(promptGuide)
        try:
                message = openAICall(promptGuide, action_prompt, context)
                print("\n",message, "\n")
                if is_code:
                        code = message.split("%%%")[1]
                        print("\n code:\n",code)
                        executeScript.main(code)
                else:   
                        voiceAnswer.main(message.replace("$$$", ""))
                return
        
        except Exception as error:
                print(error)

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

def openAICall(promptGuide, actionPrompt, context):

        NUMBER_RESPONSES = 1 if len(actionPrompt) < 150 else  2

        response = openai.ChatCompletion.create(
                model=context['MODEL'],
                max_tokens=context['MAX_TOKENS'],
                temperature=context['TEMPERATURE'],
                messages=[{"role":"system", "content": promptGuide},
                {"role":"user", "content":f"[{actionPrompt}]"}]
                ,
                n=NUMBER_RESPONSES
        )

        return response.choices[0].message.content