#include <iostream>
#include <map>
#include <vector>

using namespace std;

map < string, vector <string>> routes;

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
    }
}

void buses_for_stop(map <string, vector <string>>& stops) {
    int count = 0;
    string stop;
    cin >> stop;
    for (const auto& x : stops) {
        for (const auto& word : x.second) {
            if (word == stop) {
                count++;
            }
        }
    }
    if (count == 0) {
        cout << "No stop" << endl;
    }
    else {
        for (const auto& x : stops) {
            for (const auto& word : x.second) {
                if (word == stop) {
                    cout << x.first << " ";
                }
            }
        }
        cout << endl;
    }
}

void stops_for_bus(map <string, vector <string>>& stops) {
    string bus;
    cin >> bus;
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
                            cout << piece.first << ' ';
                            ++count;
                        }
                    }
                }
            }
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
