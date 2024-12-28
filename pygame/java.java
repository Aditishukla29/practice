import java.util.Scanner;

class Student {
    // Attributes of the Student class
    private String name;
    private int age;

    // Method to get details from the user
    public void getDetails() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = scanner.nextLine();
        System.out.print("Enter age: ");
        age = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
    }

    // Method to display the details of the student
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class StudentTest {
    public static void main(String[] args) {
        // Create three objects of the Student class
        Student student1 = new Student();
        Student student2 = new Student();
        Student student3 = new Student();

        System.out.println("Enter details for Student 1:");
        student1.getDetails();
        
        System.out.println("\nEnter details for Student 2:");
        student2.getDetails();
        
        System.out.println("\nEnter details for Student 3:");
        student3.getDetails();

        // Display details of the students
        System.out.println("\nDetails of Student 1:");
        student1.displayDetails();

        System.out.println("\nDetails of Student 2:");
        student2.displayDetails();

        System.out.println("\nDetails of Student 3:");
        student3.displayDetails();
    }
}
