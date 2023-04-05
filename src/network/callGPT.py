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
                                temperature=0.2,
                                messages=[{"role":"system", "content": setRolePrompt()},
                                {"role":"user", "content":f"""
                                %
                                [{platform.system()}]
                                [admin]
                                [{action_prompt}]%
                                """ }]
                                ,
                                n=1
                )

                print(response)
                get_message = response.choices[0].message.content

                codeFromResponse = re.search(r"%%%(.+?)%%%", get_message)
                notesFromResponse = re.search(r"&&&(.+?)&&&", get_message)

                print(codeFromResponse.group(1))
                if not codeFromResponse:
                       errors.invalidRequest()
                
                extract_code = codeFromResponse.group(1)

                executeScript.main(extract_code)
                
        except Exception as error:
                print(error)

def setRolePrompt()-> str:
        with open('./settings/prompt_limitations.txt', "r") as prompt_role:
                prompt = prompt_role.readlines()
                prompt_role.close()
                return " ".join(prompt)