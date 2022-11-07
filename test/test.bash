#!/bin/bash -xv

### Run roscore in the background ###
roscore &

### Run test script ###
python ../src/listener_test.py