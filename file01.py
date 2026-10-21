def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    
    """
    result=[]
    for i in data.split(","):
        result += [int(i)]
    return result
        
f=open("data/data01.txt")
data=f.read()
l=main(data)
print(l)

# Read data from file 