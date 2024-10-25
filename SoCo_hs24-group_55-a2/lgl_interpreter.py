import sys
import json


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


def do_func(envs_stack, args):
      
    assert len(args) == 2
    parameters = args[0]
    body = args[1]
    return ["func", parameters, body]


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
    assert len(arguments) == len(params), \
            f"{func_name} 
    local_env = dict(zip(params, arguments))

    
    envs_stack.append(local_env)
    result = do(envs_stack, body)
    envs_stack.pop()

    return result


def set_in_envs_stack(envs_stack, name, value):
    
    
    assert isinstance(name, str)
    for each_env in reversed(envs_stack):
        if name in each_env:
            each_env[name] = value
            return
    top_environment = envs_stack[-1]
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
    assert isinstance(expr, list)
    assert expr[0] in OPS, f"Unknown operation {expr[0]}"
    operation = OPS[expr[0]]
    return operation(envs_stack, expr[1:])



OPS = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}


def main():
    program = ""
    assert len(sys.argv) == 2, 
    with open(sys.argv[1], "r") as source:
        program = json.load(source)
    envs_stack = []  
    global_environment = {} 
    envs_stack.append(global_environment) 
    result = do(envs_stack, program)
    print(result)


if __name__ == "__main__":
    main()