import numpy as np

###############################################
# https://www.youtube.com/playlist?list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq
###############################################





# create generic array
a = np.array([1,2,3])
a = np.array((1,2,3))



# return dimensions (Tuple[y, x])
a.shape




# create array with default value '0' (2-lines, 3 columns)
c = np.zeros((2,3))
# create array with default value '1'
c = np.ones((2,3))
# create array with given default value
c = np.full((2,3), "A")



# Generate a 3-lines 2-columns array, with values following normal distribution (between -1 and +1)
np.random.randn(3,2)
# Set a fixed seed
np.random.seed(84514254)



# Create a linear-increasing set of values. parameters: starting_value, ending_value, total_steps
np.linspace(0, 3, 7) # [0.0, 0.5, 1, 1.5, 2.0, 2.5, 3.0]
# Create a fixed-increasing set of values. parameters: start_value, ending_value, step
np.arange(0,10,2) # [0,2,4,6,8]



# Change the type of value the array contains, for better optimization. Usable on any array constructor
np.array([1,2,3], dtype=np.int32)



# Stack 2 arrays horizontally
a = np.array((1,2,3))
b = np.array((4,5,6))
np.hstack((a,b)) # array([1, 2, 3, 4, 5, 6])

a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
np.hstack((a,b)) # array([[1, 4],
                 #        [2, 5],
                 #        [3, 6]])

# Stack 2 arrays vertically
a = np.array((1,2,3))
b = np.array((4,5,6))
np.vstack((a, b)) # array([[1, 2, 3],
                  #        [4, 5, 6]])


# Creat an 4x4 array filled with random values 0-9
np.random.randint(0, 10, [4, 4])




# Reshape an array (6x2 => 3x4 for example)
a = np.ones((2,6))
a.reshape((3,4))

# Add a 2nd dimension to a 1D array
# a = a.reshape((a.shape[0], 1))

# Remove 1 dimension from an array
a.squeeze()



# Flatten
a.ravel()



# Slicing
# a[0:4]   # from 0 (inclusive) to 4 (exclusive)
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
a[0]   # [1,2,3,4,5]
a[0,:] # [1,2,3,4,5] - Horizontal slice
a[:,0] # [1,6,11] - Vertical slice
a[1,1] # 7
a[0:2, 0:4]         # [[1,2,3,4],[6,7,8,9]] - x[0..4] for lines y[0..2]
# a[0:2, 0:4] = 0   # Set value 0 for each cell in the slice
a[:, -1]            # last column



# Boolean indexing / masking
a = np.random.randint(0, 10, [4, 4])
mask = a < 5 # return a boolean array of the same dimensions, where each cell is the result of 'cell < 5'
a[a>200] = 250 # cap all values > 200 at 250






# =================================================================
# =================================================================
# =================================================================





def test(m: int, n: int) -> np.array:
    """_summary_

    Args:
        m (int): number of lines
        n (int): number of columns

    Returns:
        a matrix full of normal-distributed values, height = m, width = n+1
        the new rightmost column contains '1'
    """
    ret = np.random.randn(m, n)
    print("ret =", ret)
    tmp = np.ones((m, 1))
    print("tmp =", tmp)
    ret = np.hstack((ret, tmp))
    print("ret =", ret)



test(3,5)