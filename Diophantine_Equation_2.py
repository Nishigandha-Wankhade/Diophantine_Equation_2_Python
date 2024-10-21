"""
-----------------------------------------------------------------------
Assignment 3 Problem 3: To let the customer know the next feasible quantity and 
                        the minimum cost option of chicken nuggets they can order.
October 20, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""


def three_variable_diophantine(n):
    """
    Function to solve the Diophantine equation 6a + 9b + 22c = n.
    Input: n = number of chicken nuggets ordered by the customer
    Output: returns (solutions) possible number of combinations to buy nuggets
    """
    solutions = []

    # Try different values of c
    for c in range(0, n // 22 + 1):    # c cannot be greater than n // 22
        remaining = n - 22 * c   # solving for 6a + 9b = remaining

        # Check if remaining is divisible by 3 (since 6 and 9 are both divisible by 3)
        if remaining % 3 != 0:
            continue  # Skip this c if the remaining value isn't divisible by 3

        # Try different values of a and calculate b
        for a in range(0, remaining // 6 + 1):
            if (remaining - 6 * a) % 9 == 0:
                b = (remaining - 6 * a) // 9   # Calculate b
                solutions.append((a, b, c))    # Store the solution (a, b, c)

    return solutions


def is_feasible(n):
    """
    Function to Checks if a given number 'n' can be expressed as 6a + 9b + 22c
    Input: quantity of nuggets from minumum to maximum (number entered by the customer)
    Returns: True if it's feasible, False otherwise.
    """
    for c in range(0, n // 22 + 1):
        remaining = n - 22 * c
        if remaining % 3 == 0:
            for a in range(0, remaining // 6 + 1):
                if (remaining - 6 * a) % 9 == 0:
                    return True  # Feasible solution found
    return False  # No feasible solution found


def find_non_feasible_numbers(n):
    """
    Function to find all non-feasible numbers upto 'n'
    input: number of chicken nuggets 'n' entered by the user
    output: returns the list of non-feasible numbers 
    """
    non_feasible = []
    for i in range(1, n + 1):
        if not is_feasible(i):  # if solutions are not found
            non_feasible.append(i)
    #print(f"\n Non-feasible numbers (Just for Info..)= {non_feasible}")
    return non_feasible


def find_nearest_feasible_number(n):
    """
    Finds the nearest feasible number >= n.
    A feasible number is one that can be expressed as 6a + 9b + 22c.
    Input: Number entered by the customer
    Returns: feasible number and its solution 
    """
    while True:
        nearest_solutions = three_variable_diophantine(n)
        if nearest_solutions:
            return n, nearest_solutions  # Return the feasible number and its solutions
        n += 1  # Increment n and check for the next feasible number


def calculate_cost(a, b, c):
    """
    Function to calculate the total cost for a given solution.
    Input: values of a, b, and c depending on the provided options
    Output: as per cost equation 3a + 4b + 9c
    Return: Total cost
    """
    return 3 * a + 4 * b + 9 * c


def find_least_expensive_option(solutions):
    """
    Function to find the least expensive option based on the cost.
    Input: List of available options.
    Returns: minimum cost and least expensive option
    """
    least_exepensive = None   # None servers as a placeholder before the program finds a solution
    min_cost = float('inf')   # float('inf') represents positive infinity in Python
                            # By initializing min_cost to infinity, we ensure that any valid cost calculated later will be smaller than this value.
    for sol in solutions:
        a, b, c = sol
        cost = calculate_cost(a, b, c)
        if cost < min_cost:
            min_cost = cost
            least_exepensive = (a, b, c)

    return least_exepensive, min_cost



"""
Main Function
Input: Number of nuggets entered by the user
Output: Possible combinations for the entered quantity, if not suggestions for next feasible quantity to order
"""
ans = 'y'
while ans.lower() == 'y':  # Continue until the user decides to stop
    try:
        n = int(input("\n\t\t How many chicken nuggets would you like to order? \t"))
        non_feasible_numbers = find_non_feasible_numbers(n)

        solutions = three_variable_diophantine(n)
        #print(f"\n Solutions:{solutions}")
        
        if solutions:
            # find the  least expensive option
            least_expensive_sol, total_cost = find_least_expensive_option(solutions)
            a, b, c = least_expensive_sol

            print(f"\n\t\t For an order size of {n}, the least expensive option is:")
            print(f"\n\t\t\t\t 'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
            print(f"\n\t\t\t\t TOTAL COST: ${total_cost}")

            #print(f"\n\t\tFor an order size of {n}, choose from the following {len(solutions)} option(s):")
            #for i, sol in enumerate(solutions):
            #    print(f"\n\t\t\t\t Option {i + 1}: 'Six_piece': {sol[0]}, 'Nine_piece': {sol[1]}, 'Twenty_two_piece': {sol[2]}")
        else:
            print("\n\t\tSORRY...!...You cannot order the requested quantity :( ")
            print("\n\t\tBut you can reorder with the following quantities:")
            
            # Find the nearest feasible number and present the options
            nearest_feasible, nearest_solutions = find_nearest_feasible_number(n)
            
            least_expensive_sol, total_cost = find_least_expensive_option(nearest_solutions)
            a, b, c = least_expensive_sol
            
            print(f"\n\t\tThe closest feasible number is {nearest_feasible} nuggets. The least expensive option is:") 
            print(f"\n\t\t\t\t 'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
            print(f"\n\t\t\t\t TOTAL COST: ${total_cost}")
            
            #print(f"\n\t\tThe closest feasible number is {nearest_feasible} nuggets. You have the following options:")
            #for i, sol in enumerate(nearest_solutions):
            #    print(f"\n\t\t\t\t Option {i + 1}: 'Six_piece': {sol[0]}, 'Nine_piece': {sol[1]}, 'Twenty_two_piece': {sol[2]}")


        ans = input("\n\n\t\tDo you want to reorder [y/n]? ")
        if ans.lower() != 'y':
                print("\n\t\tThank you! Have a nice day!")
                break
        
    except ValueError:      # To check wheather entered data is a valid number or not
        print("\n\t\t Please enter a valid number.")
