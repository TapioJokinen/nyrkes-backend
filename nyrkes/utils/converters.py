def to_camel_case(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def obj_to_camel_case(obj):
    if isinstance(obj, list):
        return [obj_to_camel_case(i) for i in obj]

    new_dict = dict()

    for k, v in obj.items():
        if isinstance(v, (dict, list)):
            new_dict[to_camel_case(k)] = obj_to_camel_case(v)
        new_dict[to_camel_case(k)] = v
    return new_dict
