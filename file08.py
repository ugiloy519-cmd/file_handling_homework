def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    total=0
    for i in data:
        if i.isdigit():
            if int(i) > total:
             total=int(i)
    return total
f=open("data/data08.txt")
data=f.read()
l=main(data)
print(l)
# Read data from file