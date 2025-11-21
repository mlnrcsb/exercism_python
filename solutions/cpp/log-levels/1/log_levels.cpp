#include <string>

namespace log_line {
std::string message(std::string line) {
    std::size_t pos = line.find("]: ");
    return line.substr(pos + 3);
}

std::string log_level(std::string line) {
    std::size_t pos = line.find("]: ");
    return line.substr(1, pos - 1);
}

std::string reformat(std::string line) {
    return message(line) + " (" + log_level(line) + ")";
}
}  // namespace log_line
