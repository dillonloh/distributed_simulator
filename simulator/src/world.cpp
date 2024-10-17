#include <iostream>
#include <vector>

#include "../include/world.h"


using namespace std;

World::World(float x_dim, float y_dim, float z_dim) {
    x_dim_ = x_dim;
    y_dim_ = y_dim;
    z_dim_ = z_dim;
    x_min_ = -x_dim / 2;
    y_min_ = -y_dim / 2;
    z_min_ = -z_dim / 2;
    x_max_ = x_dim / 2;
    y_max_ = y_dim / 2;
    z_max_ = z_dim / 2;
    printf("World created with dimensions: (%f, %f, %f)\n", x_dim_, y_dim_, z_dim_);
};

vector<float> World::getWorldDimensions() {
    return vector<float> {x_dim_, y_dim_, z_dim_};   
};

bool World::isPositionValid(vector<float> position) {
    if (position.size() != 3) {
        cout << "Invalid position size" << endl;
        return false;
    };

    if (position[0] < x_min_ || position[0] > x_max_) {
        cout << "Invalid x position" << endl;
        return false;
    };

    if (position[1] < y_min_ || position[1] > y_max_) {
        cout << "Invalid y position" << endl;
        return false;
    };

    if (position[2] < z_min_ || position[2] > z_max_) {
        cout << "Invalid z position" << endl;
        return false;
    };

    return true;
};




