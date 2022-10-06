#include <iostream>
#include <vector>
#include <algorithm>
#include <locale>

using namespace std;

void PrintVec (const vector <string>& a){
    for (auto i : a){
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    string word;
    vector <string> strings;
    vector <string> temp;
    for (int i = 0; i < n; i++){
        cin >> word;
        strings.push_back(word);
    }
    sort(strings.begin(), strings.end(), [](string a, string b){
        for (int i = 0; i < a.size(); i++){
            a[i] = tolower(a[i]);
        }
        for (int i = 0; i < b.size(); i++){
            b[i] = tolower(b[i]);
        }
        return (a<b);
    });
    PrintVec(strings);
    return 0;
}
