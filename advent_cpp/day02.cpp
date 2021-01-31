#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

const std::vector<std::string> INPUT {
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
};

std::vector<std::string> read_input(std::string & fileName)
{
    std::vector<std::string> passwords;
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
            passwords.push_back(str);
    }
    // Close the file
    in.close();

    return passwords;
}

int check_passwords(std::vector<std::string> passwords) 
{
    int valid = 0;
    for (std::string pwd : passwords) 
    {
        // remove newline from the end of the pwd
        pwd.erase(std::remove(pwd.begin(), pwd.end(), '\n'), pwd.end());
        std::size_t p = pwd.find(" ");
        // extract min and max number for character
        std::string min_max = pwd.substr(0, p);
        std::size_t min = std::stoi(min_max.substr(0, min_max.find("-")));
        std::size_t max = std::stoi(min_max.substr((min_max.find("-")+1)));

        // extract the character and the password
        pwd = pwd.substr((p+1));
        char character = pwd.substr(0, pwd.find(":"))[0];
        std::string password = pwd.substr((pwd.find(" ") + 1));
        // count the char occurences
        std::size_t n = std::count(password.begin(), password.end(), character);
        if (n >= min and n <= max) {
            valid++;
        } 

    }
    return valid;
}

int main() 
{   
    std::string fileName {"../inputs/day02.txt"};
    std::vector<std::string> passwords = read_input(fileName);
    std::cout << "Read input successfully." << std::endl;

    assert((check_passwords(INPUT) == 2));
    std::cout << "First test passed!" << std::endl;

    assert((check_passwords(passwords) == 465));
    std::cout << "Second test passed!" << std::endl;
    
    return 0;
}