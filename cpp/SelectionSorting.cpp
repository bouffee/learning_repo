#include <iostream>
#include <vector>

using namespace std;
//selection sorting for the vector of numbers

int find_smallest(vector <int> numbers) {
    int smallest = numbers[0];
    int smallest_index = 0;

    for (int i = 1; i < numbers.size(); i++){
        if (numbers[i] < smallest){
            smallest = numbers[i];
            smallest_index = i;
            return smallest_index;
        }
    }
}

vector <int> selection_sort(vector <int> numbers){
    vector <int> sorted_vec;
    int smallest;
    int num = numbers.size();

    for (int i = 0; i < num; i++){
        smallest = find_smallest(numbers);
        sorted_vec.push_back(numbers[smallest]);
        numbers.erase(numbers.begin()+smallest);
    }

    return sorted_vec;
}

void print_vec (vector <int> a){
    for (auto x : a){
        cout << x << " ";
    }
    cout << endl;
}

