// robot.cpp

#include <iostream>
#include <vector>
#include "../include/robot.h"
#include <math.h>

using namespace std;

void Robot::_update_position(vector<float> new_position) {
    position_ = new_position;
}

void Robot::_move(vector<float> direction, float speed, float duration) {
    vector<float> new_position = {position_[0] + direction[0] * speed * duration, position_[1] + direction[1] * speed * duration};
    _update_position(new_position);
}

void Robot::setPosition(vector<float> position) {
    position_ = position;
}

vector <float> Robot::getPosition() {
    return position_;
}

void Robot::startMoving(vector<float> destination) {
    is_moving_ = true;

    // check if destination is reached
    float radius = 2.0; // TODO: change this to a parameter
    bool reached_destination = false;
    float euclidean_distance = sqrt(pow(destination[0] - position_[0], 2) + pow(destination[1] - position_[1], 2));
    
    // get direction vector from current position to destination

    while (!reached_destination) {
        // get direction vector from current position to destination
        vector<float> direction = {destination[0] - position_[0], destination[1] - position_[1]};
        vector<float> unit_direction = {direction[0] / sqrt(direction[0] * direction[0] + direction[1] * direction[1]), direction[1] / sqrt(direction[0] * direction[0] + direction[1] * direction[1])};
        
        // move in that direction at max speed
        _move(unit_direction, 1, 1);

        // check if destination is reached
        euclidean_distance = sqrt(pow(destination[0] - position_[0], 2) + pow(destination[1] - position_[1], 2));
        if (euclidean_distance < radius) {
            reached_destination = true;
            stopMoving();
            break;
        }

        printf("Current position: (%f, %f)\n", position_[0], position_[1]);
    }
}

void Robot::stopMoving() {
    is_moving_ = false;
}

