#include <bits/stdc++.h>
using namespace std;

// Function to find the union of two sorted arrays
vector<int> FindUnion(int arr1[], int arr2[], int n, int m)
{
  int i = 0, j = 0;  // Pointers to iterate over arr1 and arr2
  vector<int> Union; // Vector to store the union of arr1 and arr2

  // Traverse both arrays until one of them is exhausted
  while (i < n && j < m)
  {
    // Case 1 and 2: If current element of arr1 is less than or equal to current element of arr2
    if (arr1[i] <= arr2[j])
    {
      // If the Union vector is empty or the last element in Union is not equal to arr1[i], add arr1[i]
      if (Union.size() == 0 || Union.back() != arr1[i])
        Union.push_back(arr1[i]);
      i++;
    }
    else
    {
      // Case 3: If current element of arr1 is greater than current element of arr2
      // If the Union vector is empty or the last element in Union is not equal to arr2[j], add arr2[j]
      if (Union.size() == 0 || Union.back() != arr2[j])
        Union.push_back(arr2[j]);
      j++;
    }
  }

  // If there are remaining elements in arr1, add them to Union
  while (i < n)
  {
    if (Union.back() != arr1[i])
      Union.push_back(arr1[i]);
    i++;
  }

  // If there are remaining elements in arr2, add them to Union
  while (j < m)
  {
    if (Union.back() != arr2[j])
      Union.push_back(arr2[j]);
    j++;
  }

  return Union; // Return the union vector
}

int main()
{
  int n = 10, m = 7;                            // Sizes of arr1 and arr2
  int arr1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // First sorted array
  int arr2[] = {2, 3, 4, 4, 5, 11, 12};         // Second sorted array

  // Call FindUnion to get the union of arr1 and arr2
  vector<int> Union = FindUnion(arr1, arr2, n, m);

  // Output the result
  cout << "Union of arr1 and arr2 is:" << endl;
  for (auto &val : Union)
    cout << val << " ";

  return 0;
}
