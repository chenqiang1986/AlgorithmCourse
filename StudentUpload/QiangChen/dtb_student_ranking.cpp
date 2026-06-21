#include <iostream>
#include <vector>
#include <algorithm>

struct StudentWithScore {
    std::string name;
    int score;

    // Returns true if this should be ranked before other.
    bool operator< (const StudentWithScore& other) const {
        if (score > other.score) {
            return true;
        }
        if (score == other.score && name < other.name) {
            return true;
        }

        return false;
    }
};

int main() {
    int n;
    std::cin >> n;

    std::vector<StudentWithScore> students;
    for (int i = 0; i < n; i++) {
        StudentWithScore new_student;
        std::cin >> new_student.name >> new_student.score;

        students.push_back(new_student);
    }

    std::sort(students.begin(), students.end());

    for (int i = 0; i < n; i++) {
        std::cout << students[i].name << std::endl;
    }
}