# def printMaxActivities(s, f):
#     n = len(f)
#     print("Following activities are selected")
#
#     # The first activity is always selected
#     i = 0
#     print(i, end=' ')
#
#     # Consider rest of the activities
#     for j in range(1, n):
#
#         # If this activity has start time greater than
#         # or equal to the finish time of previously
#         # selected activity, then select it
#         if s[j] >= f[i]:
#             print(j, end=' ')
#             i = j
#
#
# # Driver code
# if __name__ == '__main__':
#     s = [1, 3, 0, 5, 8, 5]
#     f = [2, 4, 6, 7, 9, 9]
# 
#     # Function call
#     printMaxActivities(s, f)


# not sorted

def MaxActivities(arr, n):
    selected = []


    Activity.sort(key=lambda x: x[1])


    i = 0
    selected.append(arr[i])

    for j in range(1, n):


        if arr[j][0] >= arr[i][1]:
            selected.append(arr[j])
            i = j
    return selected


# Driver code
if __name__ == '__main__':
    Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
    n = len(Activity)

    # Function call
    selected = MaxActivities(Activity, n)
    print("Following activities are selected :")
    print(selected[0], end="");
    for i in range(1, len(selected)):
        print(",", end=" ")
        print(selected[i], end="")