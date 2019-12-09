# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/agustin/lidar_ws/src/ceres-solver

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/agustin/lidar_ws/build/ceres-solver

# Include any dependencies generated for this target.
include examples/CMakeFiles/libmv_homography.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/libmv_homography.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/libmv_homography.dir/flags.make

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o: examples/CMakeFiles/libmv_homography.dir/flags.make
examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o: /home/agustin/lidar_ws/src/ceres-solver/examples/libmv_homography.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/libmv_homography.dir/libmv_homography.cc.o -c /home/agustin/lidar_ws/src/ceres-solver/examples/libmv_homography.cc

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/libmv_homography.dir/libmv_homography.cc.i"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/agustin/lidar_ws/src/ceres-solver/examples/libmv_homography.cc > CMakeFiles/libmv_homography.dir/libmv_homography.cc.i

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/libmv_homography.dir/libmv_homography.cc.s"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/agustin/lidar_ws/src/ceres-solver/examples/libmv_homography.cc -o CMakeFiles/libmv_homography.dir/libmv_homography.cc.s

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.requires:

.PHONY : examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.requires

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.provides: examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.requires
	$(MAKE) -f examples/CMakeFiles/libmv_homography.dir/build.make examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.provides.build
.PHONY : examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.provides

examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.provides.build: examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o


# Object files for target libmv_homography
libmv_homography_OBJECTS = \
"CMakeFiles/libmv_homography.dir/libmv_homography.cc.o"

# External object files for target libmv_homography
libmv_homography_EXTERNAL_OBJECTS =

bin/libmv_homography: examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o
bin/libmv_homography: examples/CMakeFiles/libmv_homography.dir/build.make
bin/libmv_homography: lib/libceres.a
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libgflags.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libglog.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libgflags.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libspqr.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libtbb.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libtbbmalloc.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libcholmod.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libccolamd.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libcamd.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libcolamd.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libamd.so
bin/libmv_homography: /usr/lib/liblapack.so
bin/libmv_homography: /usr/lib/libf77blas.so
bin/libmv_homography: /usr/lib/libatlas.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/librt.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/libmv_homography: /usr/lib/liblapack.so
bin/libmv_homography: /usr/lib/libf77blas.so
bin/libmv_homography: /usr/lib/libatlas.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/librt.so
bin/libmv_homography: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/libmv_homography: examples/CMakeFiles/libmv_homography.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/libmv_homography"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/libmv_homography.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/libmv_homography.dir/build: bin/libmv_homography

.PHONY : examples/CMakeFiles/libmv_homography.dir/build

examples/CMakeFiles/libmv_homography.dir/requires: examples/CMakeFiles/libmv_homography.dir/libmv_homography.cc.o.requires

.PHONY : examples/CMakeFiles/libmv_homography.dir/requires

examples/CMakeFiles/libmv_homography.dir/clean:
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && $(CMAKE_COMMAND) -P CMakeFiles/libmv_homography.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/libmv_homography.dir/clean

examples/CMakeFiles/libmv_homography.dir/depend:
	cd /home/agustin/lidar_ws/build/ceres-solver && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/agustin/lidar_ws/src/ceres-solver /home/agustin/lidar_ws/src/ceres-solver/examples /home/agustin/lidar_ws/build/ceres-solver /home/agustin/lidar_ws/build/ceres-solver/examples /home/agustin/lidar_ws/build/ceres-solver/examples/CMakeFiles/libmv_homography.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/libmv_homography.dir/depend

