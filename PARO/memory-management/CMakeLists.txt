cmake_minimum_required(VERSION 3.25)
project(memory_management)

set(CMAKE_CXX_STANDARD 14)

include_directories(exercises/resources/include)
include_directories(exercises/resources/include/resources)
include_directories(research/buddy_allocation)

add_executable(memory_management
        exercises/cmake-build-debug/resources/cmake_install.cmake
        exercises/cmake-build-debug/resources/CTestTestfile.cmake
        exercises/cmake-build-debug/resources/libkernel-resource.a
        exercises/cmake-build-debug/Testing/Temporary/CTestCostData.txt
        exercises/cmake-build-debug/Testing/Temporary/LastTest.log
        exercises/cmake-build-debug/Testing/Temporary/LastTestsFailed.log
        exercises/cmake-build-debug/build.ninja
        exercises/cmake-build-debug/cmake_install.cmake
        exercises/cmake-build-debug/CMakeCache.txt
        exercises/cmake-build-debug/CTestTestfile.cmake
        exercises/cmake-build-debug/example_leak
        exercises/cmake-build-debug/example_leak_array
        exercises/cmake-build-debug/example_leak_exception
        exercises/cmake-build-debug/example_leak_fds
        exercises/cmake-build-debug/example_leak_raii
        exercises/cmake-build-debug/log.txt
        exercises/resources/include/resources/kernel.h
        exercises/resources/include/resources/kernel_resource.h
        exercises/resources/src/kernel_resource.cpp
        exercises/resources/tests/test_kernel_resource.cpp
        exercises/Testing/Temporary/CTestCostData.txt
        exercises/Testing/Temporary/LastTest.log
        exercises/Testing/Testing/Temporary/CTestCostData.txt
        exercises/Testing/Testing/Temporary/LastTest.log
        exercises/CMakeLists.txt
        exercises/example_leak.cpp
        exercises/example_leak_array.cpp
        exercises/example_leak_exception.cpp
        exercises/example_leak_fds.cpp
        exercises/example_leak_raii.cpp
        exercises/README_PL.md
        research/buddy_allocation/Heap.cpp
        research/buddy_allocation/Heap.hpp
        research/buddy_allocation/heap_allocation.cpp
        research/buddy_allocation/heap_deallocation.cpp
        research/buddy_allocation/heap_print.cpp
        research/buddy_allocation/logger.cpp
        research/buddy_allocation/logger.hpp
        research/buddy_allocation/main.cpp
        research/buddy_allocation/tests_allocation.cpp
        research/buddy_allocation/tests_deallocation.cpp
        research/CMakeLists.txt
        research/README_PL.md)
