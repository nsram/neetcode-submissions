from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for e in arr2:
        if e in arr1:
            arr1.remove(e)
    return arr1


# do not modify below this linehttps://lh3.googleusercontent.com/a/ACg8ocJxde4vuuORY_gqmTfppSZ0wBAXs9WeXv-J55iaqtzlr4oJnVQ=s96-c$0
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
