import ast

def run_compile(input_file: str, output_file: str) -> None:
    _ = output_file

    with open(input_file, "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source, filename=input_file)
    print(ast.dump(tree, indent=2))
