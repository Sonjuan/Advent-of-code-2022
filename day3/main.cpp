#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void compensate(string path) {
    ifstream file;
    file.open(path);
    
    string line;
    int result = 0;

    if(file.is_open()) {
        while(file >> line) {
            int table[58] = {0, };
            for(int i = 0; i < line.size()/2; ++i) {table[line[i]-65] = 1;}
            for(int i = line.size()/2; i < line.size(); ++i) {
                if(table[line[i]-65]) {
                    result += (line[i]-65 >= 32) ? line[i]-96 : line[i]-38;
                    break;
                }
            }
        }
    }
    cout << result << endl;
}

void compensate2(string path) {
    ifstream file;
    file.open(path);
    string line1;
    string line2;
    string line3;
    int result = 0;

    if(file.is_open()) {
        while(file >> line1 >> line2 >> line3) {
            int table[58] = {0, };
            for(int i = 0; i < line1.size();++i)    table[line1[i]-65] = 1;      
            for(int i = 0; i < 58; ++i) {
                if(table[i] && (line2.find(i+65) != string::npos) && (line3.find(i+65) != string::npos)) {
                    result += (i >= 32) ? i-31 : i+27;
                }
            }
        }
        cout << result << endl;
    }
}

int main(void) {
    compensate(string{"./input_test.txt"});
    compensate(string{"input.txt"});
    compensate2(string{"./input_test.txt"});
    compensate2(string("./input.txt"));
    return 0;
}
