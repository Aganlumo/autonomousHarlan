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
include examples/CMakeFiles/curve_fitting.dir/depend.make

# Include the progress variables for this target.
include examples/CMakeFiles/curve_fitting.dir/progress.make

# Include the compile flags for this target's objects.
include examples/CMakeFiles/curve_fitting.dir/flags.make

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o: examples/CMakeFiles/curve_fitting.dir/flags.make
examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o: /home/agustin/lidar_ws/src/ceres-solver/examples/curve_fitting.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/curve_fitting.dir/curve_fitting.cc.o -c /home/agustin/lidar_ws/src/ceres-solver/examples/curve_fitting.cc

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/curve_fitting.dir/curve_fitting.cc.i"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/agustin/lidar_ws/src/ceres-solver/examples/curve_fitting.cc > CMakeFiles/curve_fitting.dir/curve_fitting.cc.i

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/curve_fitting.dir/curve_fitting.cc.s"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/agustin/lidar_ws/src/ceres-solver/examples/curve_fitting.cc -o CMakeFiles/curve_fitting.dir/curve_fitting.cc.s

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.requires:

.PHONY : examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.requires

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.provides: examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.requires
	$(MAKE) -f examples/CMakeFiles/curve_fitting.dir/build.make examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.provides.build
.PHONY : examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.provides

examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.provides.build: examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o


# Object files for target curve_fitting
curve_fitting_OBJECTS = \
"CMakeFiles/curve_fitting.dir/curve_fitting.cc.o"

# External object files for target curve_fitting
curve_fitting_EXTERNAL_OBJECTS =

bin/curve_fitting: examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o
bin/curve_fitting: examples/CMakeFiles/curve_fitting.dir/build.make
bin/curve_fitting: lib/libceres.a
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libglog.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libgflags.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libspqr.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libtbb.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libtbbmalloc.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcholmod.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libccolamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcolamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libamd.so
bin/curve_fitting: /usr/lib/liblapack.so
bin/curve_fitting: /usr/lib/libf77blas.so
bin/curve_fitting: /usr/lib/libatlas.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/librt.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libspqr.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libtbb.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libtbbmalloc.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcholmod.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libccolamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcolamd.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libamd.so
bin/curve_fitting: /usr/lib/liblapack.so
bin/curve_fitting: /usr/lib/libf77blas.so
bin/curve_fitting: /usr/lib/libatlas.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/librt.so
bin/curve_fitting: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/curve_fitting: examples/CMakeFiles/curve_fitting.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/curve_fitting"
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/curve_fitting.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/CMakeFiles/curve_fitting.dir/build: bin/curve_fitting

.PHONY : examples/CMakeFiles/curve_fitting.dir/build

examples/CMakeFiles/curve_fitting.dir/requires: examples/CMakeFiles/curve_fitting.dir/curve_fitting.cc.o.requires

.PHONY : examples/CMakeFiles/curve_fitting.dir/requires

examples/CMakeFiles/curve_fitting.dir/clean:
	cd /home/agustin/lidar_ws/build/ceres-solver/examples && $(CMAKE_COMMAND) -P CMakeFiles/curve_fitting.dir/cmake_clean.cmake
.PHONY : examples/CMakeFiles/curve_fitting.dir/clean

examples/CMakeFiles/curve_fitting.dir/depend:
	cd /home/agustin/lidar_ws/build/ceres-solver && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/agustin/lidar_ws/src/ceres-solver /home/agustin/lidar_ws/src/ceres-solver/examples /home/agustin/lidar_ws/build/ceres-solver /home/agustin/lidar_ws/build/ceres-solver/examples /home/agustin/lidar_ws/build/ceres-solver/examples/CMakeFiles/curve_fitting.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/CMakeFiles/curve_fitting.dir/depend

