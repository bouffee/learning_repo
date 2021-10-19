#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

map < string, vector <string>> routes;
vector<string> bus_vec;

void PrintRightBusOrder(vector<string>& bus_order, vector<std::string>& bus_in_scope){
    vector<string> f;
    for(auto& i : bus_order){
        if(count(f.begin(), f.end(), i) == 0){
            f.push_back(i);
        }
    }
    for(auto elem : f){
        for(auto item : bus_in_scope){
            if(elem == item) cout << item << ' ';
        }
    }
}

void print_st_bus(map <string, vector <string>>& stops, vector <string>& st){
    for(const auto& elem : st){
        for (const auto& x : stops) {
            for (const auto& word : x.second) {
                if(word == elem){
                    cout << "Stop " << elem << ": " << x.first << '\n';
                }
            }
        }
    }
}

void new_bus(map <string, vector <string>>& stops) {
    string bus_name;
    int bus_count;
    cin >> bus_name >> bus_count;
    for (int idx = 0; idx < bus_count; ++idx) {
        string bus;
        cin >> bus;
        stops[bus_name].push_back(bus);
        bus_vec.push_back(bus_name);
    }
}

void buses_for_stop(map <string, vector <string>>& stops) {
    int count = 0;
    vector<string> help_vec;
    string stop;
    cin >> stop;
    for (const auto& x : stops) {
        for (const auto& word : x.second) {
            if (word == stop) {
                help_vec.push_back(x.first);
                count++;
            }
        }
    }
    if (count == 0) {
        cout << "No stop" << endl;
    }
    PrintRightBusOrder(bus_vec, help_vec);
    cout << '\n';
}

void stops_for_bus(map <string, vector <string>>& stops) {
    string bus;
    cin >> bus;
    vector<string> help_vec;
    int count = 0;
    if (stops.find(bus) == stops.end()) {
        cout << "No bus" << endl;
    }
    else {
        for(const auto elem : stops[bus]){
            cout << "Stop " << elem << ": ";
            for(const auto piece : stops){
                if(piece.first != bus){
                    for(const auto item : piece.second){
                        if(item == elem){
                            help_vec.push_back(piece.first);
                            ++count;
                        }
                    }
                }
            }
            PrintRightBusOrder(bus_vec, help_vec);
            help_vec.clear();
            if(count == 0){
                cout << "no interchange";
            }
            count = 0;
            cout << '\n';
        }
    }
}

void all_buses(const map <string, vector <string>>& stops) {
    int count = 0;
    if (stops.empty()) {
        cout << "No buses" << '\n';
    }
    for (const auto& x : stops) {
        cout << "Bus " << x.first << ": ";
        for (const auto& y : x.second) {
            cout << y << ' ';
        }
        cout << '\n';
    }
}

int main() {
    int n;
    cin >> n;
    string command;
    for (int i = 1; i <= n; ++i) {
        cin >> command;
        if (command == "NEW_BUS") {
            new_bus(routes);
        }
        if (command == "BUSES_FOR_STOP") {
            buses_for_stop(routes);
        }
        if (command == "STOPS_FOR_BUS") {
            stops_for_bus(routes);
        }
        if (command == "ALL_BUSES") {
            all_buses(routes);
        }
    }
    return 0;
}
