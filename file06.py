def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result=[]
    r=data.split()
    for i in r:
        result.append(len(i))
    return result
f=open("data/data06.txt")
data=f.read()
l=main(data)
print(l)
    
# Read data from file