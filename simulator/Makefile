CXX = g++
CXXFLAGS = -Iinclude
SRCS = $(wildcard src/*.cpp)
OBJS = $(patsubst src/%.cpp, build/%.o, $(SRCS))
TARGET = main


all: $(TARGET)
	echo "Building" && echo "$(SRCS)" && echo "$(OBJS)"
	
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Compile each .cpp file into .o object files
build/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

