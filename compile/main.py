import ast

FRAME_SIZE = 64

LAST_FRAME = "<" * FRAME_SIZE
NEXT_FRAME = ">" * FRAME_SIZE

RETURN_START = f">[{LAST_FRAME}]<"

# convert [p] to [pad, p, p+1, p+2, p+3, pad]
OPERATIONS = {
    ">" : ">>>>>",
    "<" : "<<<<<",
    "+" : "+>+[<->[->>>>+<<<<]]>>>>[-<<<<+>>>>]<<<<<[>>+[<<->>[->>>+<<<]]>>>[-<<<+>>>]<<<<<[>>>+[<<<->>>[->>+<<]]>>[-<<+>>]<<<<<[->>>>+<<<<]]]",
    "-" : "+>[<->[->>>>+<<<<]]>>>>[-<<<<+>>>>]<<<<<[>>[<<->>[->>>+<<<]]>>>[-<<<+>>>]<<<<<[>>>[<<<->>>[->>+<<]]>>[-<<+>>]<<<<<[->>>>-<<<<]>>>-<<<]>>-<<]>-<",
    "[" : ">[<+>[->>>>+<<<<]]>>>>[-<<<<+>>>>]<<<[<<+>>[->>>+<<<]]>>>[-<<<+>>>]<<[<<<+>>>[->>+<<]]>>[-<<+>>]<[<<<<+>>>>[->+<]]>[-<+>]<<<<<[[-]",
    "]" : ">[<+>[->>>>+<<<<]]>>>>[-<<<<+>>>>]<<<[<<+>>[->>>+<<<]]>>>[-<<<+>>>]<<[<<<+>>>[->>+<<]]>>[-<<+>>]<[<<<<+>>>>[->+<]]>[-<+>]<<<<<]",
    "." : ">.<",
}
CONVERT_32 = lambda code : "".join(OPERATIONS[x] for x in code)

def make_stack_frame():
    code = []

    code.append(RETURN_START)
    code.append(">>")
    code.append("+")

    return "".join(code)

def run_compile(input_file: str, output_file: str) -> None:
    _ = output_file

    with open(input_file, "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source, filename=input_file)
    print(ast.dump(tree, indent=2))

    code_parts: list[str] = []

    # we make the initial box
    code_parts.append("->>+<<")

    n = 2
    for _ in range(n):code_parts.append(NEXT_FRAME)
    for _ in range(n):code_parts.append(LAST_FRAME)

    # code_parts.append(make_stack_frame())

    # we write it out
    code = "".join(code_parts)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(code)
