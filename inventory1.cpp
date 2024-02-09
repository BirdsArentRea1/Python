#include<iostream>
using namespace std;

string inventory[10];
int coin = 100;
void shop();

int main() {
	for (int i = 0; i < 10; i++)
		inventory[i] = " ";

	cout << "welcome to the text based game!" << endl;
	char input = 'a';
	int room = 1;
	while (input != 'q') {
		cout << "your inventory:" << endl;
		for (int i = 0; i < 10; i++)
			cout << inventory[i] << " ";
		cout << endl;

		switch (room) {
		case 1:
			cout << "your in room 1, you can go (s)outh." << endl;
			if (inventory[0] != "key")
				cout << "you see a shiny (k)ey on the floor" << endl;
			cin >> input;
			if (input == 's')
				room = 2;
			if (input == 'k')
				inventory[0] = "key";
			break;
		case 2:
			cout << "your in room 2, you can go (n)orth or (s)outh." << endl;
			cin >> input;
			if (input == 'n')
				room = 1;
			if (input == 's')
				if (inventory[0] == "key") {
					cout << "you unlock the door with the key!" << endl;
					inventory[0] = " ";
				room = 3;
				}
			
				break;
		case 3:
			cout << "your in room 3, there is a shop. you can go (n)orth, or (S)hop." << endl;
			cin >> input;
			if (input == 'n')
				room = 2;
			if (input == 'S')
				shop();

				break;

		}//end switch


	}//end game loop


}//end main

//functions
void shop() {
	int input = 'a';
	while(input != 0) {
	cout << "--------------------------------------------------"
	cout << "welcome to the shop " << endl;
	cout << "items for sale:" << endl;
	cout << "1) suspicious stew $5"<<  endl;
	cout << "2) live chicken $10" << endl;
	cout << "3) key $50" << endl;
	cout << "your coin:" << coin << endl;
	cout << "0 to quit" << endl;

	cout << "your inventory:" << endl;
	for (int i = 0; i < 10; i++)
		cout << inventory[i] << " ";
	cout << endl << endl;

	cout << "what would you like to purchase" << endl;
	cin >> input;

	if (input == 1) {
		if (coin >= 5) {
			cout << "you bought the suspicious stew" << endl;
			inventory[1] = "stew";
			coin -= 5;
		}
		else
			cout << "you dont have enough gold!" << endl;
	}
	if (input == 2) {
		if (coin >= 10) {
		cout << "you bought the live chicken" << endl;
		inventory[2] = "chicken";
		}
		cout << "you dont have enough gold!" << endl;
	}
	if (input == 3) {
		if (coin >= 50) {
			cout << "you bought the key" << endl;
			inventory[0] = "key";
		}
		cout << "you dont have enough gold!" << endl;
	}
	else if (input == 0)
		cout << "goodbye" << endl;
	else {
		cout << "not an option idiot" << endl;
		}//end mini game loop
	}


}
