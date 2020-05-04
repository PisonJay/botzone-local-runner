CXX = g++-9
C_INCLUDE_PATH = -I /usr/local/include
CFLAGS = -O2 -std=c++17

all: runner judger

runner: runner.cpp
	$(CXX) $(C_INCLUDE_PATH) -o runner runner.cpp $(CFLAGS)

judger: judger.cpp
	$(CXX) $(C_INCLUDE_PATH) -o judger judger.cpp $(CFLAGS)