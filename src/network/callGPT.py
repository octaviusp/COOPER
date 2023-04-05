import openai
import re
import platform

from executor import executeScript
from helpers import errors

def promptDataToGPT(action_prompt: str, context: dict[str, str]):
        
        if not context or not action_prompt:
                errors.invalidRequest()

        try:    
                response = openai.ChatCompletion.create(
                                model='gpt-3.5-turbo',
                                max_tokens=2048,
                                temperature=0,
                                messages=[{"role":"system", "content": setRolePrompt()},
                                {"role":"user", "content":f"""
                                %$[{platform.system()}]\n
                                [{action_prompt}]%$
                                """ }]
                                ,
                                n=1
                )

                get_message = response.choices[0].message.content
                notesFromResponse = ""
                codeFromResponse = ""

                try:
                        codeFromResponse = get_message.split('%%%')[1]
                        try:
                                codeFromResponse = codeFromResponse.split('&&&')[0]
                        except:
                                pass
                except:
                        errors.invalidRequest()
                try:
                        notesFromResponse = get_message.split('&&&')[1]
                except:
                        pass
                print("********************************************")
                print(codeFromResponse)
                print("********************************************")
                executeScript.main(codeFromResponse)
                print("********************************************")
                print(notesFromResponse)
                
        except Exception as error:
                print(error)

def setRolePrompt()-> str:
        with open('./settings/prompt_limitations.txt', "r") as prompt_role:
                prompt = prompt_role.readlines()
                prompt_role.close()
                return " ".join(prompt)