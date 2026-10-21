def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    result=0
    for i in data:
        result+=1
    return result
file=open('data/data02.txt')
data=file.read()
l=main(data)
print(l)

# Read data from file 