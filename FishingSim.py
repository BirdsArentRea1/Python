#include <iostream>
#include <windows.h>  
#include <chrono>
#include <thread>
#include <random>
using namespace std;
using namespace std::this_thread; // This line already includes the necessary functionality
using namespace std::chrono_literals;
using std::chrono::system_clock;

string inventory[10];
void Fishing();

// Random number generator setup
random_device rd;
mt19937 gen(rd());
uniform_int_distribution<> distr(1, 5); // Random between 1 and 5 seconds

int main() {
    char input = 'a';
    int room = 1;

    while (input != 'q') {
        cout << "your inventory:" << endl;
        for (int i = 0; i < 10; i++)
            cout << inventory[i] << " ";
        cout << endl;

        switch (room) {
        case 1:
            cout << "Press F to fish" << endl;
            cin >> input;
            if (input == 'F' || input == 'f') {
                cout << "fishing..." << endl;
                int random_seconds = distr(gen); // Generate a random number for sleep duration
                sleep_for(chrono::seconds(random_seconds)); // Use std::chrono::seconds
                Fishing();
            }
            break;
        }
    }
}

void Fishing() {
    int num = rand() % 100;
    if (num < 33) {
        cout << "You got a carp" << endl;
        inventory[0] = "carp";
    }
    else if (num < 66) {
        cout << "You got a Woodskip" << endl;
        inventory[1] = "woodskip";
    }
    else if (num < 99) {
        cout << "You got a Catfish" << endl;
        inventory[2] = "catfish";
    }
}
