import unittest

def find_pairs_with_sum(numbers, target_sum):
    if not numbers:
        return []  # Return an empty list if the input list is empty

    seen = {}  # Dictionary to store seen values as keys with value true
    pairs = [] # Empty list of tuples to store each pair of integers that sums to the target sum  

    for num in numbers:
        complement = target_sum - num  # Calculate the complement needed for the target sum

        # Check if the complement is in the dictionary
        if complement in seen:
            pairs.append((num, complement))
        
        # Add the current number to the dictionary for future checks
        seen[num] = True
    
    return pairs

class TestFindPairsWithSum(unittest.TestCase):
    def test_empty_input(self):
        result = find_pairs_with_sum([], 10)
        self.assertEqual(result, [])

    def test_no_pairs_found(self):
        result = find_pairs_with_sum([1, 2, 3, 4], 10)
        self.assertEqual(result, [])

    def test_pairs_found(self):
        result = find_pairs_with_sum([1, 2, 3, 4, 5, 6], 7)
        self.assertEqual(result, [(4, 3), (5, 2), (6, 1)])

    def test_negative_numbers(self):
        result = find_pairs_with_sum([-1, 2, -3, 4, -5, 6], 1)
        self.assertEqual(result, [(2, -1), (4, -3), (6, -5)])
    
    def test_target_sum_negative(self):
        result = find_pairs_with_sum([1, -2, 2, -3], -1)
        self.assertEqual(result, [(-2, 1), (-3, 2)])

    def test_target_sum_zero(self):
        result = find_pairs_with_sum([1, -1, 2, -2], 0)
        self.assertEqual(result, [(-1, 1), (-2, 2)])

if __name__ == "__main__":
    unittest.main()