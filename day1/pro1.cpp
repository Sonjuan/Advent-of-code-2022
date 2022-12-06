#include <iostream>
#include <fstream>
using namespace std;


int main(void) {
    string line;
    ifstream myfile("input.txt");
    if(myfile.is_open()) {
        while(getline(myfile, line)) {
            cout << line << endl;
        }

        myfile.close();
    }else {
        cout << "unable to open" << endl;
    }
    return 0;
}
