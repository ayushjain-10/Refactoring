# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def print_stat():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

    # Calculate the mean and standard deviation of the grades
def calculate_mean_sd(grade_list):
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    # return mean and sd
    return mean, sd

def print_output(mean, sd):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def main():
    """Calculates the mean and standard deviation of a list of grades."""
    mean, sd = calculate_mean_sd(print_stat())
    print_output(mean, sd)

if __name__ == "__main__":
    main()
