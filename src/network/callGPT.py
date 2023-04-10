import os
import openai
from executor import executeScript, voiceAnswer

def promptDataToGPT(action_prompt: str, context: dict[str, str]):

        is_code = False
        external_code = False

        promptGuide = promptTopicToGPT(action_prompt, context)
        if not promptGuide[1]:
                return
        elif promptGuide[1] == "[C]":
                is_code = True
                external_code = True
        else:
                try:
                        if promptGuide[0].find("python") != -1:
                                is_code = True
                                promptGuide[0] = promptGuide[0] + "\n" + getPrompts("python_structure/python_code")
                except:
                        if context['VOICE']:
                                voiceAnswer.main("Please give me more context.", "ERROR_OCURRED")
                        return

        if promptGuide[1] != "[C]":
                promptGuide[0] = getPrompts("python_structure/required") + "\n" + promptGuide[0]

        try:
                message = openAICall(promptGuide[0], action_prompt, context)
                print(message)
                global notes
                global name_file
                try:
                        notes = message.split("&&&")[1]
                except:
                        pass
                if is_code:
                        parts = message.split("%%%")
                        code = parts[1]
                        if not external_code:
                                executeScript.main(parts[1], notes)
                        else:
                                file_metadata_prompt = getPrompts("code_prompt/file_metadata")
                                metadata = openAICall(file_metadata_prompt, code, context)
                                metadata_name = metadata.split("%%%")
                                saveCode(code, metadata_name[1])
                                
                else:   
                        if context['VOICE'] and not external_code:
                                voiceAnswer.main(message.replace("$$$", "").replace("%%%",""), "GENERAL_TOPIC")
                return
        
        except Exception as error:
                print(error)

def promptTopicToGPT(user_action, config):

    try:
        topic = openAICall(getPrompts("topic_selector"), user_action, config)
        topic_prompt = getPrompts(f"topic_prompts/{topic}")
        return [topic_prompt, topic]

    except Exception as e:
        voiceAnswer.main("TOPIC ERROR", "TOPIC_DETECTOR_ERROR")
        return [None, None]
    
def getPrompts(file_path):
        print(file_path)
        with open(os.path.abspath(f"./settings/{file_path}.txt"), "r") as Topic:
            getText = Topic.readlines()
            Topic.close()
            return " ".join(getText)

def saveCode(code: str, title: str):
    with open(f"./{title}", "w") as f:
        f.write(code)
        print("\n COOPER - Code saved")
        f.close()

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