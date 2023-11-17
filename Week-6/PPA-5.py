def dict_to_list(D):
    return list(
        D.items()
    )


def list_to_dict(L):
    return {item[0]: item[1] for item in L}


print(dict_to_list({'abc': 3, 'def': 10}))
