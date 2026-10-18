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
            result.append(i)
    return result
data=input()
print(main(data))   
# Read data from file