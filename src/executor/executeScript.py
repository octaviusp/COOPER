import subprocess
import sys
import re
import hashlib
import platform
from .voiceAnswer import main as vc

APP_NAME = "COOPER - "
def main(python_code: str, notes: str):
    try:
        print("{APP_NAME} - Executing action sir...")
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

        print(f"\n{APP_NAME} - Executed sir. \n")
        return

    except Exception as error:
        print(error)
        return

def remove_file(file: str):
        if not platform.system().find(r"(linux|LINUX|Linux)"):
                subprocess.run(["del", file], shell=True)
        else:
                subprocess.run(["rm", file])



