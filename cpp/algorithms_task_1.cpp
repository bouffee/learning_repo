#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void PrintVector (const vector <int>& a){
    for (auto const& x : a){
        cout << x << " ";
    }
    cout << endl;
}

int main (){
    int N, elem;
    vector <int> numbers;
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> elem;
        numbers.push_back(elem);
    }
    sort (numbers.begin(), numbers.end(), [](int x, int y){
        if (abs(x) < abs(y))   {
            return true;
        }
        else return false;
    });
    PrintVector (numbers);
    return 0;
}