#include <iostream>
#include <map>
#include <vector>

using namespace std;

map < string, vector <string>> routes;


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

map <string, vector<string>> buses_for_stop(map <string, vector <string>>& stops) {
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
		cout << "No stops" << endl;
		return stops;
	}
	else {
		cout << "Stop " << stop << ": ";
		for (const auto& x : stops) {
			for (const auto& word : x.second) {
				if (word == stop) {
					cout << x.first << " ";
				}
			}
		}
		cout << endl;
		return stops; 
	}
}

map <string, vector <string>> stops_for_bus(map <string, vector <string>>& stops) {
	string bus;
	cin >> bus;
	int count = 0;
	if (stops.find(bus) == stops.end()) {
		cout << "No buses" << endl;
		return stops;
	}
	else {
		cout << "Bus " << bus << ": ";
		for (const auto& x : stops) {
			if (x.first == bus) {
				for (const auto& c : x.second) {
					cout << c << " ";
					count++;
				}
			}
			if (count != 0) {
				cout << endl;
			}
		}		
		return stops;
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
	map <string, vector <string>> stops;
	int n;
	cin >> n;
	string command;
	for (int i = 1; i <= n; ++i) {
		cin >> command;
		if (command == "NEW_BUS") {
			new_bus(stops);
		}
		if (command == "BUSES_FOR_STOP") {
			buses_for_stop(stops);
		}
		if (command == "STOPS_FOR_BUS") {
			stops_for_bus(stops);
		}
		if (command == "ALL_BUSES") {
			all_buses(routes);
		}
	}
	return 0;
}