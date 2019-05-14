cmake_minimum_required(VERSION 2.8.3)
project(lidar_euclidean_cluster_detect)
add_compile_options(-std=c++11)

find_package(autoware_build_flags REQUIRED)

find_package(autoware_msgs REQUIRED)
find_package(catkin REQUIRED COMPONENTS
        pcl_ros
        roscpp
        geometry_msgs
        std_msgs
        sensor_msgs
        tf
        vector_map_server
        grid_map_ros
        grid_map_cv
        grid_map_msgs
        autoware_msgs
        )

find_package(OpenMP)
find_package(OpenCV REQUIRED)

set(CMAKE_CXX_FLAGS "-O2 -Wall ${CMAKE_CXX_FLAGS}")

catkin_package(
        CATKIN_DEPENDS
        pcl_ros
        roscpp
        geometry_msgs
        std_msgs
        sensor_msgs
        autoware_msgs
        tf
        vector_map_server
        grid_map_ros
        grid_map_cv
        grid_map_msgs
        INCLUDE_DIRS include
)

include_directories(
        include
        ${catkin_INCLUDE_DIRS}
        ${autoware_msgs_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
)
link_directories(${PCL_LIBRARY_DIRS})
link_directories(${OpenCV_LIBRARY_DIRS})

#Euclidean Cluster
add_executable(lidar_euclidean_cluster_detect
        nodes/lidar_euclidean_cluster_detect/lidar_euclidean_cluster_detect.cpp
        )

add_dependencies(lidar_euclidean_cluster_detect
        ${catkin_EXPORTED_TARGETS}
        )

target_link_libraries(lidar_euclidean_cluster_detect ${catkin_LIBRARIES})

if (OPENMP_FOUND)
    set_target_properties(lidar_euclidean_cluster_detect PROPERTIES
            COMPILE_FLAGS ${OpenMP_CXX_FLAGS}
            LINK_FLAGS ${OpenMP_CXX_FLAGS}
            )
endif ()

install(TARGETS
        lidar_euclidean_cluster_detect
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
)
