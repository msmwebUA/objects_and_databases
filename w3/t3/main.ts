class Person {
  first_name: string;
  last_name: string;
  private age: number;

  constructor(fname: string, lname: string, age: number) {
    this.first_name = fname;
    this.last_name = lname;
    this.age = age;
  }

  getAge(): number {
    return this.age;
  }

  ageUp(): void {
    this.age++;
  }

  getFullname(): string {
    return `${this.first_name} ${this.last_name}`;
  }

  printFullname(): void {
    console.log(`${this.first_name} ${this.last_name}`);
  }
}

class Main {
  constructor() {
    console.log('Program starting.');
    console.log('Creating person...');
    const person = new Person('John', 'Doe', 30);
    console.log('Person created.');
    console.log(`Name: ${person.getFullname()}`);
    console.log(`Age: ${person.getAge()}`);
    console.log('Person has now birthday...');
    person.ageUp();
    console.log(`New age: ${person.getAge()}`);
    console.log('Program ending.');
  }
}

const app = new Main();