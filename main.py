
"""
 ==> Rule For Binary Search
    Note: If search value is Smaller then change Upper Bond & Mid Becomes New Upper Bond
                                 OR
          If search value is Biggeer then change Lower Bond & Mid Becomes New Lower Bond

Here,
       Upper Bond Means Greatest or Last Value
       Lower Bond Means Shortest or First Value
"""

def binary_search(list,key):
    lower_value = 0
    higher_value = len(list) - 1
    found = False

    while lower_value <= higher_value and not found:
        mid_value = (lower_value + higher_value)//2
        if key == list[mid_value]:
            found = True
        elif key > list[mid_value]:
            lower_value = mid_value + 1
        else:
            higher_value = mid_value - 1
    if found ==True:
        print("Key Is Found")
    else:
        print("Key Is Not Found")


list = [500,100,2668,3489,6920,200,392,100000,25489,17492,14892156225,358,23,14]
list.sort()
print("\n Values Of List Are :\n" ,list)
print("\n Binary Search Program")
print(" =====================")
key = int(input("Enter The Value Of  Key: "))
binary_search(list,key)
