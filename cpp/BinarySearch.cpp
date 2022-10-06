#include <iostream>
#include <map>
#include <vector>
//binary search for the vector of numbers

using namespace std;

int binary_search(vector <int> list, int item){
    int low = 0;
    int high = list.size() - 1;
    int mid;
    int guess;

    while (low <= high){
        mid = (low+high)/2; //find a middle
        guess = list[mid]; //make a middle of the list
        if (guess = item){
            return mid;//if it's what we need then end
        }
        else {
            low = mid + 1; //if it's nit then go search in other
        }
        return 0; //case if u don't find anything
    }
}
