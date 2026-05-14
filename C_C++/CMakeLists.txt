cmake_minimum_required(VERSION 3.20)
project(C_C++)

set(CMAKE_CXX_STANDARD 23)

# This line finds all your .cpp files automatically
file(GLOB SOURCES "*.cpp")

add_executable(app ${SOURCES})