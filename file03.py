def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result=[]
    for i in data:
        if i.isdigit():
            result += [int(i)]
    return result
f=open("data/data03.txt")
data=f.read()
l=main(data)
print(l)
# Read data from file
