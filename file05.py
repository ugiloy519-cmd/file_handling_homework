def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    dg=0
    non_dg=0
    for i in data:
        if i.isdigit():
            dg +=1
        else:
            non_dg += 1
    return [dg,non_dg]
data=input()
print(main(data))
    
# Read data from file