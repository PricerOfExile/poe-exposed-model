def reshape(scalar, scale) -> int:
    return scalar*100/scale

def translate(input_list: list):
    positive_scale = sum([i for i in input_list if i >= 0])
    return {
        "E": reshape(input_list[0], positive_scale),
        "D": reshape(input_list[1], positive_scale),
        "C": reshape(input_list[2], positive_scale),
        "B": reshape(input_list[3], positive_scale),
        "A": reshape(input_list[4], positive_scale),
        "S": reshape(input_list[5], positive_scale)
    }
