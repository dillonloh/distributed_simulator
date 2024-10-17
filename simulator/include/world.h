// world.h

#include <vector>

#ifndef WORLD_H
#define WORLD_H

using namespace std;

class World {
    public:
        World(float x_dim = 100.0f, float y_dim = 100.0f, float z_dim = 100.0f); // (x, y, z)
        
        bool isPositionValid(vector<float> position);
        vector<float> getWorldDimensions();

    private:
        float x_dim_;
        float y_dim_;
        float z_dim_;
        float x_min_;
        float y_min_;
        float z_min_;
        float x_max_;
        float y_max_;
        float z_max_;
};

#endif 