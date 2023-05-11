#factorial
""" Compute factorial of n
    
    Args:
        n (int)
    
    Returns:
        int: factorial of n
    """
def factorial(n):
    ...


  
# Wallis function
def wallisPi(n):
    """ Compute the approximation of pi/2 with n iterations
        using the Wallis's formula
    
    Args:
        n (int)
    
    Returns:
        float: approximation of pi/2
    """
    ...

 
#  Gregory function
def gregoryPi(n):
    """ Compute the approximation of pi/4 with n iterations
        using the Gregory's formula
    
    Args:
        n (int)
    
    Returns:
        float: approximation of pi/4
    """
    ...


# Ramanujan function
def ramanujanPi(n):
    """ Compute the recursive part of the pi approximation
    defined by Ramanujan
    
    Args:
        n (int)
    
    Returns:
        float: part of the denominator of Ramanujan's approximation
    """
    ...

    
# compute distance
def distComputRec(lst, q, lst_dist):
    """ Compute all the distances between a query value 
    and all the elements in a list.
    And return the distances in a list of distance
    
    Args:
        lst (list): input list of element
        q (int/float): query value
        lst_dist (list): list containing the resulting distances
        This last argument should be initialized with an empty list []
    
    Returns:
        void function
    """
    ...


# compute min
def findMinRec(lst, min=None):
    """ Find minimum element in a list
    
    Args:
        lst (list): input list containing numerical values
        min (int/float): keeping track of the minimum value (initialized to None)
    
    Returns:
        int/float: returns minimum value in the list
    """
    ...


# compute occurences
def countOccurenceRec(lst, query, count=0):
    """ Count the number of occurence of a query in a list
    
    Args:
        lst (list): input list containing numerical values
        query (int/float): query value for which we count the number of occurences
        count (int): a counter we increment when we meet an element == query
        The latest argument is initialized to zero
    
    Returns:
        int: number of occurences of the query in the list
    """
    ...




# check sort
def checkSortRec(lst):
    """ Check is the list is properly sorted
    
    Args:
        lst (list): input list containing numerical values
    
    Returns:
        bool: True if the list is sorted, otherwise False
    """
    ...
    

# MAIN
def main():
    # compute pi
    import math
    print(math.pi)
    print(wallisPi(900)*2)
    print(gregoryPi(900)*4)
    print(9801/(2*(2**0.5)*ramanujanPi(100)))

    # compute distance
    lst = [45, 10, 97, 103, 1, 52, 100]
    query = 1
    lst_dist = []
    distComputRec(lst, query, lst_dist)
    print(lst_dist)

    # find min
    min_val = findMinRec(lst)
    print(min_val)

    # count occurence
    lst = [45, 10, 97, 10, 1, 10, 100]
    print(countOccurenceRec(lst, 10))

    # check sorted list
    lst1 = [45, 10, 97, 10, 1, 10, 100]
    lst2 = [1, 2, 3, 4, 5, 6, 7]
    print(checkSortRec(lst1))
    print(checkSortRec(lst2))

main() # Run the main code