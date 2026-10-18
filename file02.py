def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)
file=open('file_handling_homework\data\data02.txt','r')
data=file.read
print(main(data))
# Read data from file 