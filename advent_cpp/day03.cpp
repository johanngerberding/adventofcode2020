#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>


std::string INPUT = R"(..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#)";

std::vector<std::vector<int>> STEP_SIZES {
    {1,1},
    {3,1},
    {5,1},
    {7,1},
    {1,2}
};


std::vector<std::string> mlstr2vec(std::string in) 
{
    std::vector<std::string> input;
    while (in.find("\n") < std::string::npos) {
        input.push_back(in.substr(0, in.find("\n")));
        in = in.substr((in.find("\n") + 1));
    }
    input.push_back(in);
    return input;
}

std::vector<std::string> read_input(std::string & fileName)
{
    std::vector<std::string> forrest;
    std::ifstream in(fileName.c_str());

    // Check if the object is valid
    if (!in) {
        std::cerr << "Cannot open the file: " << fileName << std::endl;
    }

    std::string str;
    // Read in the file, line by line
    while (std::getline(in, str)) 
    {
        if (str.size() > 0)
            forrest.push_back(str);
    }
    // Close the file
    in.close();

    return forrest;
}

int traverse_forrest(std::vector<std::string> forrest, int right=3, int down=1) 
{
    int x = 0;
    int trees = 0;
    int max_x = forrest[0].size();
    for (size_t y = 0; y < forrest.size(); y += down) 
    {
        char pos = forrest[y][x];
        if (pos == '#') 
            trees++;

        x += right;
        if (x > (max_x - 1)) {
            x = x - max_x;
        }
        

    }
    return trees;
}

long multiply_trees(std::vector<std::string> forrest, std::vector<std::vector<int>> step_sizes)
{
    std::vector<int> trees;
    for (std::vector<int> step : step_sizes) {
        trees.push_back(traverse_forrest(forrest, step[0], step[1]));
    }

    long mul = 1;
    for (int t: trees) {
        mul *= t;
    }
    return mul;
}


int main() {
    std::string fileName {"../inputs/day03.txt"};
    std::vector<std::string> forrest = read_input(fileName);

    assert(traverse_forrest(mlstr2vec(INPUT)) == 7);
    
    std::cout << traverse_forrest(forrest) << std::endl;

    long mul = multiply_trees(forrest, STEP_SIZES);
    std::cout << mul << std::endl;

    return 0;
}