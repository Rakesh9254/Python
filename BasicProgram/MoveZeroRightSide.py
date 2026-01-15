class Solution:
    def moveZeroes(self, arr):
        index = 0  # Position for the next non-zero element

        # Step 1: Move all non-zero elements forward
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[index] = arr[i]
                index += 1

        # Step 2: Fill the remaining positions with zeroes
        while index < len(arr):
            arr[index] = 0
            index += 1

# Main part to test the moveZeroes function
if __name__ == "__main__":
    solution = Solution()
    
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print("Original array:", arr)
    
    solution.moveZeroes(arr)
    
    print("Array after moving zeroes:", arr)
