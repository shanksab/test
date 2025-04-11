public class Person {
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display info
    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    // Main method to run the program
    public static void main(String[] args) {
        Person p1 = new Person("Alice", 22);
        Person p2 = new Person("Bob", 30);

        p1.displayInfo();
        p2.displayInfo();
    }
}
