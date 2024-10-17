// robot.h

#include <vector>

#ifndef ROBOT_H
#define ROBOT_H

using namespace std;

class Robot {

    private:
        
        vector<float> position_;
        bool is_moving_;

        void _update_position(vector<float> new_position);
        void _move(vector<float> direction, float speed, float duration);

    public:

        void setPosition(vector<float> position);
        vector<float> getPosition();

        void startMoving(vector<float> destination);
        void stopMoving();
        
};

#endif