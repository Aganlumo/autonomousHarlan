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
include internal/ceres/CMakeFiles/covariance_test.dir/depend.make

# Include the progress variables for this target.
include internal/ceres/CMakeFiles/covariance_test.dir/progress.make

# Include the compile flags for this target's objects.
include internal/ceres/CMakeFiles/covariance_test.dir/flags.make

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o: internal/ceres/CMakeFiles/covariance_test.dir/flags.make
internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o: /home/agustin/lidar_ws/src/ceres-solver/internal/ceres/covariance_test.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o"
	cd /home/agustin/lidar_ws/build/ceres-solver/internal/ceres && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/covariance_test.dir/covariance_test.cc.o -c /home/agustin/lidar_ws/src/ceres-solver/internal/ceres/covariance_test.cc

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/covariance_test.dir/covariance_test.cc.i"
	cd /home/agustin/lidar_ws/build/ceres-solver/internal/ceres && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/agustin/lidar_ws/src/ceres-solver/internal/ceres/covariance_test.cc > CMakeFiles/covariance_test.dir/covariance_test.cc.i

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/covariance_test.dir/covariance_test.cc.s"
	cd /home/agustin/lidar_ws/build/ceres-solver/internal/ceres && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/agustin/lidar_ws/src/ceres-solver/internal/ceres/covariance_test.cc -o CMakeFiles/covariance_test.dir/covariance_test.cc.s

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.requires:

.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.requires

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.provides: internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.requires
	$(MAKE) -f internal/ceres/CMakeFiles/covariance_test.dir/build.make internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.provides.build
.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.provides

internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.provides.build: internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o


# Object files for target covariance_test
covariance_test_OBJECTS = \
"CMakeFiles/covariance_test.dir/covariance_test.cc.o"

# External object files for target covariance_test
covariance_test_EXTERNAL_OBJECTS =

bin/covariance_test: internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o
bin/covariance_test: internal/ceres/CMakeFiles/covariance_test.dir/build.make
bin/covariance_test: lib/libtest_util.a
bin/covariance_test: lib/libceres.a
bin/covariance_test: lib/libgtest.a
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libspqr.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libtbb.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libtbbmalloc.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libcholmod.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libccolamd.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libcamd.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libcolamd.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libamd.so
bin/covariance_test: /usr/lib/liblapack.so
bin/covariance_test: /usr/lib/libf77blas.so
bin/covariance_test: /usr/lib/libatlas.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/librt.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/covariance_test: /usr/lib/liblapack.so
bin/covariance_test: /usr/lib/libf77blas.so
bin/covariance_test: /usr/lib/libatlas.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libsuitesparseconfig.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/librt.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libcxsparse.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libgflags.so
bin/covariance_test: /usr/lib/x86_64-linux-gnu/libglog.so
bin/covariance_test: internal/ceres/CMakeFiles/covariance_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/agustin/lidar_ws/build/ceres-solver/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/covariance_test"
	cd /home/agustin/lidar_ws/build/ceres-solver/internal/ceres && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/covariance_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
internal/ceres/CMakeFiles/covariance_test.dir/build: bin/covariance_test

.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/build

internal/ceres/CMakeFiles/covariance_test.dir/requires: internal/ceres/CMakeFiles/covariance_test.dir/covariance_test.cc.o.requires

.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/requires

internal/ceres/CMakeFiles/covariance_test.dir/clean:
	cd /home/agustin/lidar_ws/build/ceres-solver/internal/ceres && $(CMAKE_COMMAND) -P CMakeFiles/covariance_test.dir/cmake_clean.cmake
.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/clean

internal/ceres/CMakeFiles/covariance_test.dir/depend:
	cd /home/agustin/lidar_ws/build/ceres-solver && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/agustin/lidar_ws/src/ceres-solver /home/agustin/lidar_ws/src/ceres-solver/internal/ceres /home/agustin/lidar_ws/build/ceres-solver /home/agustin/lidar_ws/build/ceres-solver/internal/ceres /home/agustin/lidar_ws/build/ceres-solver/internal/ceres/CMakeFiles/covariance_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : internal/ceres/CMakeFiles/covariance_test.dir/depend

