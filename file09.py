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
            if int(i)<sm:
                sm=int(i)
    return sm
f=open("data/data09.txt")
data=f.read()
l=main(data)
print(l)


# Read data from file