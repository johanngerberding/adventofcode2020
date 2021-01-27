#include <iostream>
#include <fstream>
#include <string>
#include <vector>

const std::vector<std::string> INPUT {
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
};

std::vector<std::string> split(std::string pw) 
{
    std::vector<std::string> pw_parts;
    // is there a " "
    int start = 0;
    size_t pos = pw.find(" ");
    while (pos != -1) {
        pw_parts.push_back(pw.substr(start, pos));
        start = pos;
        pw = pw.substr(pos+1);
        pos = pw.find(" ");
    }
    return pw_parts;
    
}

int check_passwords(std::vector<std::string> passwords) 
{
    int valid_pwds = 0;
    //for (std::string pwd : passwords) 
    //{

    //}
    return 0;
}

int main() 
{
    std::string test = "1-3 a: abcde\n";

    std::vector<std::string> parts = split(test);
    for (std::string part: parts) {
        std::cout << part << std::endl;
    }

    std::size_t pos = test.find(" ");
    std::string test_2 = test.substr(0, pos);
    int pos_ = test_2.find("-");
    std::string min_pos = test_2.substr(0,pos_);
    std::string max_pos = test_2.substr(pos_+1);
    int min_c = std::stoi(min_pos);
    int max_c = std::stoi(max_pos);
    std::cout << "Min: " << min_c << std::endl;
    std::cout << "Max: " << max_c << std::endl;

    std::string test_3 = test.substr(pos+1);
    std::cout << test_3 << std::endl; 
    std::size_t pos_char = test_3.find(":");
    std::string c = test_3.substr(0,pos_char);
    std::cout << "Character: " << c << std::endl;

    pos = test_3.find(" ");
    std::string test_4 = test_3.substr(pos+1);
    std::cout << test_4 << std::endl;

    pos_ = test.find("q");
    std::cout << pos_ << std::endl; 
    
    return 0;
}