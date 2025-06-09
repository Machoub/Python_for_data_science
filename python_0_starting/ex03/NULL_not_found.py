def NULL_not_found(object: any)-> int:
    objtype = type(object)
    ret = None
    match object:
        case None:
            ret = f'Nothing: {object}  {objtype}'
        case float()if object != object:
            ret = f'Cheese: {object} {objtype}'
        case bool() if object is False:
            ret = f'Fake: {object} {objtype}'
        case int() if object == 0:
            ret = f'Zero : {object} {objtype}'
        case str() if not object:
            ret = f'Empty : {objtype}'
  
    if ret is not None:
        print(ret)
        return 0
    else:
        print("Type not found")
        return 1