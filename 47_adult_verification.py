ADULT_AGE: int = 18

def is_adult(age: int) -> bool:
    """
    Determines if the given age qualifies as an adult.
    :param age: The age to check.
    :return: True if age is greater than or equal to ADULT_AGE, otherwise False.
    """
    return age >= ADULT_AGE
def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()