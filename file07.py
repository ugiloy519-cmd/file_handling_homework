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
data=input()
print(main(data))

    
# Read data from file