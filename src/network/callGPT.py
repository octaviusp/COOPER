import os
import openai
from executor import executeScript, voiceAnswer

def promptDataToGPT(action_prompt: str, context: dict[str, str]):

        is_code = False
        promptGuide = promptTopicToGPT(action_prompt, context)
        if not promptGuide:
                print("ERROR")
                return

        try:
                if promptGuide.find("python") != -1:
                        is_code = True
                        promptGuide = promptGuide + "\n" + getPrompts("python_structure/python_code")
                else:
                        promptGuide = "You are a linux assistant\n" + promptGuide
        except:
                if context['VOICE']:
                        voiceAnswer.main("Please give me more context.", "ERROR_OCURRED")
                return

        promptGuide = getPrompts("python_structure/required") + "\n" + promptGuide
        
        print(promptGuide)
        try:
                message = openAICall(promptGuide, action_prompt, context)
                print(message)
                global notes
                notes = ""
                try:
                        notes = message.split("&&&")[1]
                except:
                        pass
                if is_code:
                        code = message.split("%%%")[1]
                        executeScript.main(code, notes)
                else:   
                        if context['VOICE']:
                                voiceAnswer.main(message.replace("$$$", "").replace("%%%",""), "GENERAL_TOPIC")
                return
        
        except Exception as error:
                print(error)

def promptTopicToGPT(user_action, config):

    try:
        get_response = openAICall(getPrompts("topic_selector"), user_action, config)
        print(get_response)
        return getPrompts(f"topic_prompts/{get_response}")

    except Exception as e:
        print("ERROR Ocurred.")
        return None
    
def getPrompts(file_path):
        print(file_path)
        with open(os.path.abspath(f"./settings/{file_path}.txt"), "r") as Topic:
            getText = Topic.readlines()
            Topic.close()
            return " ".join(getText)

def openAICall(promptGuide, actionPrompt, context):

        NUMBER_RESPONSES = 1 if len(actionPrompt) < 150 else  2
        try:
                response = openai.ChatCompletion.create(
                        model=context['MODEL'],
                        max_tokens=context['MAX_TOKENS'],
                        temperature=context['TEMPERATURE'],
                        messages=[{"role":"system", "content": promptGuide},
                        {"role":"user", "content":f"[{actionPrompt}]"}]
                        ,
                        n=NUMBER_RESPONSES
                )
        except Exception as error:
                if context['VOICE']:
                        voiceAnswer.main("Network error.", "ERROR_CALL")
                print(error)
                return

        return response.choices[0].message.content