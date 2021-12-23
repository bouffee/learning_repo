#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct FullName {
    string Name;
    string Last_name;
};

class Person {
public:
    void ChangeFirstName(int year, const string& first_name) {
        if(names.count(year) == 0) {
            names[year].Last_name = "";
        }
        names[year].Name = first_name;
    }
    void ChangeLastName(int year, const string& last_name) {
        if (names.count(year) == 0){
            names[year].Name = "";
        }
        names[year].Last_name = last_name;
    }
    string GetFullName(int year) {
            for (const auto& x: names) {
                if (year < x.first) {
                    return "Incognito";
                }
                break;
            }
        string check1 = "";
        string check2 = "";
        for (const auto& y : names){
            if (y.first <= year && y.second.Name != ""){
                check1 = y.second.Name;
            }
            if (y.first <= year && y.second.Last_name != ""){
                check2 = y.second.Last_name;
            }
        }
        if (check1 == ""){
            return check2 + " with unknown first name";
        }
        else if (check2 == ""){
            return check1 + " with unknown last name";
        }
        else return check1 + " " + check2;
    }
private:
    map <int, FullName> names;
};



