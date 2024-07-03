#include <bits/stdc++.h>
using namespace std;

void selection_sort(int arr[], int n)
{
    // selection sort
    // The outer loop iterates n-1 times because after n-1 iterations, the last element will automatically be in its correct position.
    for (int i = 0; i < n - 1; i++)
    {
        int mini = i;
        for (int j = i + 1; j < n; j++)
        // The inner loop starts from i+1 and finds the index of the minimum element in the unsorted portion of the array.
        {
            if (arr[j] < arr[mini])
            {
                mini = j;
            }
        }
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i] = temp;
    }
    cout << "After selection sor: " << "\n";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

int main()
{
    int arr[] = {13, 46, 24, 52, 20, 9, 55, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Before selection sort: " << "\n";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
    selection_sort(arr, n);
    return 0;
}