#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

// если имя неизвестно, возвращает пустую строку
string FindNameByYear(const map<int, string>& names, int year) {
    string name;  // изначально имя неизвестно
    // перебираем всю историю по возрастанию ключа словаря, то есть в хронологическом порядке
    for (const auto& item : names) {
        // если очередной год не больше данного, обновляем имя
        if (item.first <= year) {
            name = item.second;
        } else {
            // иначе пора остановиться, так как эта запись и все последующие относятся к будущему
            break;
        }
    }
    return name;
}

void print_map (const map <int, vector <string>>& a, int year){
    for (const auto& i : a){
        if (i.first == year){
            for (const auto& x : i.second){
                cout << x << " ";
            }
        }
    }
    cout << endl;
}

bool search (const map <int, vector <string>>& a, int year, string name){
    for (const auto& x : a){
        if (x.first == year){
            for (const auto& y : x.second){
                if (y == name){
                    return true;
                }
            }
        }
    }
    return false;
}

class Person {
public:
    void ChangeFirstName(int year, const string& first_name) {
        first_names[year] = first_name;
        if (!search (names_history, year, first_name)){
            names_history[year].push_back(first_name);
        }
    }
    void ChangeLastName(int year, const string& last_name) {
        last_names[year] = last_name;
        if (!search (surnames_history, year, last_name)){
            surnames_history[year].push_back(last_name);
        }

    }
    string GetFullName(int year) {
        // получаем имя и фамилию по состоянию на год year
        const string first_name = FindNameByYear(first_names, year);
        const string last_name = FindNameByYear(last_names, year);

        // если и имя, и фамилия неизвестны
        if (first_name.empty() && last_name.empty()) {
            return "Incognito";

            // если неизвестно только имя
        } else if (first_name.empty()) {
            return last_name + " with unknown first name";

            // если неизвестна только фамилия
        } else if (last_name.empty()) {
            return first_name + " with unknown last name";

            // если известны и имя, и фамилия
        } else {
            return first_name + " " + last_name;
        }
    }
    string GetFullNameWithHistory(int year) {
        int count1 = 0;
        int count2 = 0;
        const string first_name = FindNameByYear(first_names, year);
        const string last_name = FindNameByYear(last_names, year);
        cout << first_name << " ";
        for (const auto& x : names_history){
            if (x.first <= year){
                for (const auto& y : x.second){

                }
            }
        }
        // получить все имена и фамилии по состоянию на конец года year
    }

private:
    map<int, string> first_names;
    map<int, string> last_names;
    map <int, vector <string>> names_history;
    map <int, vector <string>> surnames_history;
};
