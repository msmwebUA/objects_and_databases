#include <iostream>
#include <string>

class Person {
  private:
    int age;
  public:
    std::string first_name;
    std::string last_name;

    Person(std::string fname, std::string lname, int age) {
      this->first_name = fname;
      this->last_name = lname;
      this->age = age;
    }

    int getAge() {
      return this->age;
    }

    void ageUp() {
      this->age++;
    }

    std::string getFullname() {
      return first_name + " " + last_name;
    }

    void printFullname() {
        std::cout << first_name << " " << last_name << std::endl;
    }
};