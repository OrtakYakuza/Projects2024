import sys
import json
from datetime import datetime

trace_file_path = None  # store the trace file path
trace_enabled = False  
unique_id_counter = 100000 

def generate_unique_id():
    global unique_id_counter
    unique_id_counter += 1
    return unique_id_counter

header_written = False

def decorator(file_path):
    def trace(func):
        def wrap(*args, **kwargs):
            global header_written 
            unique_id = generate_unique_id() 
            timestamp_start = datetime.now()
            with open(file_path, 'a') as f:
                if not header_written:
                    f.write("id,timestamp,function_name,event\n")
                    header_written = True
                    
                f.write(f"{unique_id},{timestamp_start},{func.__name__},start\n")
            
            result = func(*args, **kwargs)  # Call the actual function
            
            timestamp_end = datetime.now()
            with open(file_path, 'a') as f:
                f.write(f"{unique_id},{timestamp_end},{func.__name__},stop\n")
            return result
        return wrap
    return trace



def do_addieren(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return left + right


def do_betrag(envs_stack, args):
    assert len(args) == 1
    val = do(envs_stack, args[0])
    return abs(val)


def do_sequenz(envs_stack, args):
    assert len(args) > 0
    result = None
    for expr in args:
        result = do(envs_stack, expr)
        print(f"Result of expression {expr}: {result}")
    return result


def do_setzen(envs_stack, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    var_name = args[0]
    value = do(envs_stack, args[1])
    set_in_envs_stack(envs_stack, var_name, value)
    return value


def do_bekommen(envs_stack, args):
    assert len(args) == 1
    assert isinstance(args[0], str)
    value = get_from_envs_stack(envs_stack, args[0])
    return value

def do_and(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return 1 if left and right else 0

def do_or(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return 1 if left or right else 0

def do_xor(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return 1 if (left and not right) or (not left and right) else 0

def do_plus(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return left + right

def do_minus(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return left - right

def do_multiply(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    return left * right

def do_divide(envs_stack, args):
    assert len(args) == 2
    left = do(envs_stack, args[0])
    right = do(envs_stack, args[1])
    assert right != 0, "not possible"
    return left / right

def do_func(envs_stack, args):
    assert len(args) == 2
    parameters = args[0]
    body = args[1]
    func_snap_env = envs_stack.copy()                  #
    return ["func", parameters, body, func_snap_env]     # these two changed


def do_call(envs_stack, args):
    assert len(args) >= 1
    assert isinstance(args[0], str)
    func_name = args[0]
    arguments = [do(envs_stack, a) for a in args[1:]]
    func = get_from_envs_stack(envs_stack, func_name)
    assert isinstance(func, list) and func[0] == "func", \
        f"{func_name} is not a function!"
    params = func[1]
    body = func[2]
    func_snap_env = func[3]                         #
    assert len(arguments) == len(params), f"{func_name} receives a different number of parameters"
    
    local_env = dict(zip(params, arguments))                
    call_env_stack = func_snap_env + [local_env]            #
    result = do(call_env_stack, body)                       # these 3 changed
    return result


def set_in_envs_stack(envs_stack, name, value):
    assert isinstance(name, str)

    if len(envs_stack) > 1:                ##this func changed so it dosnt itaerate over the "envs", but rather local env, if not found -> global env
        envs_stack[-1][name] = value
    else:
        top_environment = envs_stack[0]
        top_environment[name] = value



def get_from_envs_stack(envs_stack, name):
    assert isinstance(name, str)
    for each_env in reversed(envs_stack):
        if name in each_env:
            return each_env[name]
    assert False, f"Name {name} not found"



def do(envs_stack, expr):


    if isinstance(expr, int):
        return expr

    if isinstance(expr, str):
        return get_from_envs_stack(envs_stack, expr)
    
    if isinstance(expr, list) and len(expr) == 1:
        return do(envs_stack, expr[0])
    
    if isinstance(expr, list) and expr[0] in OPS:
        operation = OPS[expr[0]]
        return operation(envs_stack, expr[1:])

    if isinstance(expr, list) and len(expr) == 3 and isinstance(expr[1], str):
        operator = expr[1]
        args = [expr[0], expr[2]]
        assert operator in OPS, f"Unknown operation {operator}"
        return OPS[operator](envs_stack, args)

    
    raise ValueError(f"Invalid expression format: {expr}")


OPS = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}

symbol_to_name = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divide",
    "AND": "and",
    "OR": "or",
    "XOR": "xor"
}

OPS.update({symbol: OPS[name] for symbol, name in symbol_to_name.items() if name in OPS})

def main():
    global trace_enabled, trace_file_path
    program = ""

    assert len(sys.argv) >= 2, "usage: python lgl_interpreter.py example.gsc --trace trace_file.log"

    if "--trace" in sys.argv:
        trace_enabled = True
        trace_index = sys.argv.index("--trace")
        trace_file_path = sys.argv[trace_index + 1] # use index of the file path

    if trace_enabled and trace_file_path:
        for name, func in OPS.items():
            OPS[name] = decorator(trace_file_path)(func) # put decorator on every function

    with open(sys.argv[1], "r") as source:
        program = json.load(source)

    envs_stack = []  
    global_environment = {} 
    envs_stack.append(global_environment)
    result = do(envs_stack, program)


if __name__ == "__main__":
    main()

