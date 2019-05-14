# Install script for directory: /home/lke/kusv_ke/kusv_ros/src/common/libs/diagnostics_lib/fake_autoware_nodes

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lke/kusv_ke/kusv_ros/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lke/kusv_ke/kusv_ros/build/common/libs/diagnostics_lib/fake_autoware_nodes/catkin_generated/installspace/fake_autoware_nodes.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fake_autoware_nodes/cmake" TYPE FILE FILES
    "/home/lke/kusv_ke/kusv_ros/build/common/libs/diagnostics_lib/fake_autoware_nodes/catkin_generated/installspace/fake_autoware_nodesConfig.cmake"
    "/home/lke/kusv_ke/kusv_ros/build/common/libs/diagnostics_lib/fake_autoware_nodes/catkin_generated/installspace/fake_autoware_nodesConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fake_autoware_nodes" TYPE FILE FILES "/home/lke/kusv_ke/kusv_ros/src/common/libs/diagnostics_lib/fake_autoware_nodes/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fake_autoware_nodes/launch" TYPE DIRECTORY FILES "/home/lke/kusv_ke/kusv_ros/src/common/libs/diagnostics_lib/fake_autoware_nodes/launch/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/fake_autoware_nodes" TYPE DIRECTORY FILES "/home/lke/kusv_ke/kusv_ros/src/common/libs/diagnostics_lib/fake_autoware_nodes/include/fake_autoware_nodes")
endif()

