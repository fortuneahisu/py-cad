cmake_minimum_required(VERSION 3.20)
project(robotics_workspace CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# Set standard to modern C++23
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Automatically grab all your .cpp files
file(GLOB SOURCES "*.cpp")

# Build your executable
add_executable(robot_app ${SOURCES})