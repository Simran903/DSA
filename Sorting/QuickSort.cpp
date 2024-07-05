#include <bits/stdc++.h>
using namespace std;

// Partition function for QuickSort
int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];  // Choose the first element as pivot
    int i = low;
    int j = high;
    
    while (i < j) {
        // Find element on left side greater than pivot
        while (arr[i] <= pivot && i <= high - 1) {
            i++;
        }
        
        // Find element on right side smaller than or equal to pivot
        while (arr[j] > pivot && j >= low + 1) {
            j--;
        }
        
        // Swap elements if i is still less than j
        if (i < j) swap(arr[i], arr[j]);
    }
    
    // Place pivot in its correct position
    swap(arr[low], arr[j]);
    return j;  // Return the partition index
}

// Recursive QuickSort function
void qs(vector<int> &arr, int low, int high) {
    if (low < high) {
        // Find the partition index
        int pIndex = partition(arr, low, high);
        
        // Recursively sort the left and right subarrays
        qs(arr, low, pIndex - 1);
        qs(arr, pIndex + 1, high);
    }
}

// Wrapper function for QuickSort
vector<int> quickSort(vector<int> arr) {
    qs(arr, 0, arr.size() - 1);
    return arr;
}

int main() {
    vector<int> arr = {4, 6, 2, 5, 7, 9, 1, 3};
    int n = arr.size();
    
    // Print array before sorting
    cout << "Before Using quick Sort: " << endl;
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Apply QuickSort
    arr = quickSort(arr);
    
    // Print array after sorting
    cout << "After Using quick sort: " << "\n";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
    
    return 0;
}