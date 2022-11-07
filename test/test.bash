#!/bin/bash -xv

### Run roscore in the background ###
roscore &

sleep 3

### Run test script ###
python ./src/listener_test.py