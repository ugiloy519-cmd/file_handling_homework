def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result=[0,0]
    for i in data:
        if i.isdigit():
            result[0]+=1
        else:
            result[1]+=1
    return result
f=open("data/data05.txt")

data=f.read()
l=main(data)
print(l)
    
# Read data from