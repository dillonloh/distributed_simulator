#include <iostream>
#include <vector>
#include <string>

#include "../include/world.h"
#include "../include/robot.h"

using namespace std;

int main() {
    World world(10.0, 10.0, 10.0);
    Robot robot;
    
    string input = "";

    vector<float> dimensions = world.getWorldDimensions();
    cout << "World dimensions: (" << dimensions[0] << ", " << dimensions[1] << ", " << dimensions[2] << ")" << endl;

    vector<float> valid_position = {0, 0, 0};
    vector<float> invalid_position = {0, 0, 11};

    
    while (input != "gay") {
        cout << "Enter a position (x, y, z): ";
        cin >> valid_position[0] >> valid_position[1] >> valid_position[2];
        cout << "Position is " << (world.isPositionValid(valid_position) ? "valid" : "invalid") << endl;
        cout << "Continue? [Y/gay(no)]";
        cin >> input;
    }
    
    return 0;
}