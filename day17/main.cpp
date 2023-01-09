//https://github.com/Rickbude/advent-of-code/blob/master/2022/puzzle17/main.cpp
#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

using pos_type = pair<long long, long long>;
const int N_cols = 7;

struct Map {
    vector<bitset<N_cols>> blocks; 
};

struct Shape {
    int rows = 0;
    int cols = 0;
    vector<bool> blocks;
};

bool detect_collision(const Map& map, const Shape& shape, const pos_type& pos) {
    if(pos.second < 0) {
        return true;
    }

    if(pos.first < 0) {
        return true;
    }
}
