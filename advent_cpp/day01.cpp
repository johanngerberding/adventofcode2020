#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>

const std::vector<int> input_test {1721, 979, 366, 299, 675, 1456};

std::vector<int> read_input(std::string & fileName)
{
    std::vector<int> numbers;
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
            numbers.push_back(std::stoi(str));
    }
    // Close the file
    in.close();

    return numbers;
}


int product_two(std::vector<int> numbers)
{
    for (size_t i=0; i < numbers.size() - 1; ++i)
    {
        for (size_t j=i+1; j < numbers.size(); ++j) 
        {
            if (numbers[i] + numbers[j] == 2020)
                return (numbers[i] * numbers[j]);
        }
    }
    return -1;
}

long product_three(std::vector<int> numbers)
{
    for (size_t i=0; i < numbers.size() - 2; ++i)
    {
        for (size_t j=i+1; j < numbers.size() - 1; ++j)
        {
            for (size_t k=j+1; k < numbers.size(); ++k)
            {
                if (numbers[i] + numbers[j] + numbers[k] == 2020)
                    return  (numbers[i] * numbers[j] * numbers[k]);
            }
        }
    }
    return -1;
}

int main() 
{
    
    std::string fileName {"../inputs/day01.txt"};
    std::vector<int> numbers = read_input(fileName);

    assert((product_two(input_test) == 514579));
    std::cout << "Test passed!" << std::endl;

    int result = product_two(numbers);
    std::cout << "Result (2 numbers): " << result << std::endl;

    assert((product_three(input_test) == 241861950));
    std::cout << "Test passed!" << std::endl;

    result = product_three(numbers);
    std::cout << "Result (3 numbers): " << result << std::endl;

    return 0;

}