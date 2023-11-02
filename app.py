import sys
from find_pairs import find_pairs_with_sum

def main():
    # Check if the command line arguments are provided correctly
    if len(sys.argv) != 3:
        print("Please use the following format for inputs: python app.py <comma-separated-list-of-numbers> <target-sum>")
        sys.exit(1)

    # Parse command line arguments
    input_values = sys.argv[1].split(',')
    input_values = [int(num) for num in input_values if num.strip()]
    target_sum = int(sys.argv[2])

    # Find pairs
    pairs = find_pairs_with_sum(input_values, target_sum)
    # Print the answer
    if not pairs:
        print("Not pairs found\n")
    else:
        for pair in pairs:
            print('+ ', pair[0], ',', pair[1])

if __name__=='__main__':
    main()
