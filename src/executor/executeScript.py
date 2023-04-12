import subprocess
import sys
import re
import hashlib
import platform
from .voiceAnswer import main as vc

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(python_code: str, notes: str):
    try:
        print(bcolors.OKBLUE+"[COOPER]", "- Executing action sir...")
        m = hashlib.md5()
        m.update(python_code[:50].encode('utf-8'))

        temporaly_filename = m.hexdigest()
        temporaly_filename_py = temporaly_filename+"_temp.py"
        with open(temporaly_filename_py, "w") as f:
                f.write(python_code)
                f.close()
        
        python_version = re.search(r"^\d+?", str(sys.version)).group(0)
        prefix = ""
        if int(python_version) >= 3:
                prefix = "python3"
        else:
                prefix = "python"

        subprocess.run([prefix, temporaly_filename_py])

        if notes:
                temporaly_filename_notes = temporaly_filename+"_temp_note"
                vc(notes, temporaly_filename_notes)

        remove_file(temporaly_filename_py)
        
        print("\n")

        print(bcolors.OKCYAN +"[COOPER]", "- Executed.")
        return

    except Exception as error:
        print(bcolors.WARNING +"[COOPER]", " Execution error.")
        return

def remove_file(file: str):
        if not platform.system().find(r"(linux|LINUX|Linux)"):
                subprocess.run(["del", file], shell=True)
        else:
                subprocess.run(["rm", file])



