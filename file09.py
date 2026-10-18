def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sm=9
    for i in data:
        if i.isdigit():
            if int(i)>sm:
                sm=int(i)
    return sm
data=input()
print(main(data))


# Read data from file