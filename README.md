# duckietown-gym-ros

This repository is a boilerplate for integrating the duckietown gym environment with ROS. Intented to be used with [this docker compose template](https://github.com/dguisti/duckietown-gym).

Currently outputs gym simulated camera observations to `/fakebot/camera_node/image/compressed` and reads wheel data from `/fakebot/joy_mapper_node/car_cmd`. Passing wheel as action to gym environment is still a work in progress.
