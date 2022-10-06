#include <iostream>
#include <set>
#include <map>

using namespace std;

map <string, set <string>> synonyms;

void ADD (){
    string word1, word2;
    cin >> word1 >> word2;
    synonyms[word1].insert(word2);
    synonyms[word2].insert(word1);
}

void COUNT (){
    string word;
    cin >> word;
    cout << synonyms[word].size()<<endl;
}

void CHECK(){
    string word1, word2;
    cin >> word1 >> word2;
    if (synonyms[word1].count(word2)>0){
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }
}

int main(){
    int q;
    string command;
    cin >> q;
    for (int i = 0; i < q; i++){
        cin >> command;
        if (command == "ADD"){
            ADD();
        }
        if (command == "COUNT"){
            COUNT();
        }
        if (command == "CHECK"){
            CHECK();
        }
    }
    return 0;
}