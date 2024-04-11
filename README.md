### Project: Implementing 2D Convolution Using Lists

#### **Objective**
Develop a function to perform 2D convolution on an image matrix using a given convolution kernel matrix, using lists to represent the matrices.

#### **Tasks**

1. **Flip the Kernel Matrix (K)**
   - **Input:** Original kernel matrix K
   - **Output:** Flipped kernel matrix K'
   - **Method:** Flip horizontally and then vertically
     - Formula: `K'[i][j] = K[h-i-1][w-j-1]`
       - where `h` is the number of rows and `w` is the number of columns in K

2. **Compute Response Values at Different Positions**
   - **Input:** Image matrix `im`, flipped kernel matrix `K'`, stride length `stride`
   - **Output:** Convolved image matrix `im'`
   - **Method:** Use `K'` to slide over `im` from the top-left corner, moving right and down as per the stride, performing element-wise multiplication and summing up the results to form the convolved matrix `im'`.

#### **Assignment**

Implement the 2D convolution function: `conv2d(im, K, stride=1)`
- **Inputs:** 
  - `im`: 2D array represented by a list of lists
  - `K`: 2D kernel array represented by a list of lists
  - `stride`: The stride length, with a default value of 1
- **Output:** 
  - Convolved 2D array represented by a list of lists

#### **Instructions:**
1. Download the Jupyter Notebook file “第3周大作业1_题目.ipynb” and the image “ruc.jpg”.
2. Read the existing code, which handles reading the image, converting it into a 2D numeric list, and converting 2D numeric lists back into images for output.
3. Write code to implement the `conv2d(im, K, stride)` function that performs the kernel flipping and convolution operation, returning the convolved 2D numeric list.
4. Observe the differences in output images with different convolution kernels.

#### **Test Cases:**

- **Example 1:**
  - Input:
    ```python
    im = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]
    K = [[1, 1],
         [1, 1]]
    stride = 2
    ```
  - Output:
    ```python
    [[4, 0],
     [0, 4]]
    ```

- **Example 2:**
  - Input:
    - Large `im` matrix
    - `K` matrix:
      ```python
      [[ 5, -3,  3,  5,  7],
       [ 0, -9,  8, -8, -8],
       [ 6,  6,  1, -5,  3],
       [-3, -9,  5,  0,  1],
       [ 1, -9, -6,  0,  8]]
      ```
    - `stride = 1`
  - Output for stride=1 and stride=2 provided in the original query.

This structured overview outlines the problem statement for implementing 2D convolution using Python lists, including the main objectives, tasks to be completed, inputs and outputs of the required function, and additional instructions for completing the assignment.
