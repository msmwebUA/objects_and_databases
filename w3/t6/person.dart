class Person {
  String firstName;
  String lastName;
  int _age;

  // short constructor 
  Person(this.firstName, this.lastName,this._age);

  // getter for age 
  int get getAge => _age;

  void ageUp() {
    _age += 1;
  }

  String getFullname() {
    return "$firstName $lastName";
  }

  void printFullname() {
    print("$firstName $lastName");
  }
}