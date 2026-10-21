def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    total=0
    for i in data:
        if i.isdigit():
            total += int(i)
    return total
f=open("data/data07.txt")
data=f.read()
l=main(data)
print(l)

    
# Read data from file