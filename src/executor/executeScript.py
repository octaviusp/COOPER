import subprocess
import sys
import re
import hashlib
import platform

APP_NAME = "A"
def main(python_code: str):
    try:
        print("{APP_NAME} - Executing action sir...")
        m = hashlib.md5()
        m.update(python_code[:50].encode('utf-8'))

        temporaly_filename = m.hexdigest() + "_temp.py"

        with open(temporaly_filename, "w") as f:
                f.write(python_code)
        
        python_version = re.search(r"^\d+?", str(sys.version)).group(0)
        prefix = ""
        if int(python_version) >= 3:
                prefix = "python3"
        else:
                prefix = "python"

        subprocess.run([prefix, temporaly_filename])

        remove_file(temporaly_filename)

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



