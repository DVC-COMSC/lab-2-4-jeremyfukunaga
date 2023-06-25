def main():
    ##################################################
    # Comlete your code here
    ##################################################
    # pass

    # Original string
    original_str = "Python Programming"

    # Extract "Python" from the original string
    sub1 = original_str[0:6]

    # Extract "Programming" from the original string
    sub2 = original_str[7:]

    # Merge the two substrings using string concatenation
    merged_str = sub2 + " " + sub1

    # Print the merged string
    print(sub2)
    print(sub1)
    print(merged_str)
    return sub1, sub2, merged_str

if __name__ == '__main__':
    main()
