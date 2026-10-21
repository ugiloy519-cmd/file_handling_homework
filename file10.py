def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    row=data.split()
    large=0
    for i in row:
        if len(i)>large:
            large=len(i)
    return large
f=open("data/data10.txt")
data=f.read()
l=main(data)
print(l)
# Read data from file