cmake_minimum_required(VERSION 3.26)
project(lista5 C)

set(CMAKE_C_STANDARD 11)

add_executable(lista5
        zad10.c)

# Link the math library
target_link_libraries(lista5 m)