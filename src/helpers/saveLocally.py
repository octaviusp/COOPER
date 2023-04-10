def main(code: str, title: str, extension:str):
    with open(f"./{title}.{extension}", "w") as f:
        f.write(code)
        print("\n COOPER - Code save")
        f.close()
        