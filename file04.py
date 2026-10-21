def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result=[]
    for i in data:
        if not i.isdigit():
            result+=[i]
    return result
f=open("data/data04.txt")
data=f.read()
l=main(data)
print(l)   
# Read data from file