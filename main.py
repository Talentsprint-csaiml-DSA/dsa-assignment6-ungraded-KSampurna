def longest_box_sequence(boxes):
    #ToDo 
    #Write your code here.
    
    boxes.sort(key=lambda box: (box[0], box[1], box[2]))

    n = len(boxes)
    dp = [1] * n  # dp[i] stores the maximum number of boxes ending at index i

    for i in range(n):
        for j in range(i):
            # Check if box j can fit inside box i
            if (boxes[j][0] < boxes[i][0] and
                boxes[j][1] < boxes[i][1] and
                boxes[j][2] < boxes[i][2]):
                dp[i] = max(dp[i], dp[j] + 1)
                    
    return max(dp)

if __name__ == "__main__":
    boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]
    result = longest_box_sequence(boxes)
    print(result)
    
