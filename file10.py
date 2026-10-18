def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    row=data.split(',')
    large=0
    for i in row:
        if len(row)> large:
            large=len(row)
    return large
data=input()
print(main(data))
# Read data from file