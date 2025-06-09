def all_thing_is_obj(object: any)-> int:
    objtype = type(object)
    ret = None
    match object:
        case str():
            ret = f'{object} is in the kitchen : {objtype}'
        case list():
            ret = f'List : {objtype}'
        case tuple():
            ret = f'Tuple : {objtype}'
        case set():
            ret = f'Set : {objtype}'
        case dict():
            ret = f'Dict : {objtype}'  
    if ret is not None:
        print(ret)
    else:
        print("Type not found")
        return 42