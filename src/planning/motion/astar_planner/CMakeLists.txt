cmake_minimum_required(VERSION 2.8.3)
project(astar_planner)
add_compile_options(-std=c++11)

find_package(autoware_msgs REQUIRED)

find_package(vector_map REQUIRED)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  pcl_ros
  pcl_conversions
  tf
  waypoint_follower
  autoware_msgs 
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS roscpp std_msgs tf waypoint_follower autoware_msgs vector_map
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${vector_map_INCLUDE_DIRS}
  ${autoware_msgs_INCLUDE_DIRS}
)

add_executable(velocity_set nodes/velocity_set/velocity_set.cpp nodes/velocity_set/velocity_set_path.cpp nodes/velocity_set/velocity_set_info.cpp nodes/velocity_set/libvelocity_set.cpp)
target_link_libraries(velocity_set ${catkin_LIBRARIES})
add_dependencies(velocity_set 
${catkin_EXPORTED_TARGETS})

add_executable(obstacle_avoid nodes/obstacle_avoid/obstacle_avoid.cpp nodes/obstacle_avoid/astar_search.cpp nodes/obstacle_avoid/search_info_ros.cpp nodes/obstacle_avoid/astar_util.cpp)
target_link_libraries(obstacle_avoid ${catkin_LIBRARIES})
add_dependencies(obstacle_avoid ${catkin_EXPORTED_TARGETS})

add_executable(obstacle_sim nodes/obstacle_avoid/obstacle_sim/obstacle_sim.cpp nodes/obstacle_avoid/obstacle_sim/obstacle_sim_node.cpp)
target_link_libraries(obstacle_sim ${catkin_LIBRARIES})
add_dependencies(obstacle_sim ${catkin_EXPORTED_TARGETS})
