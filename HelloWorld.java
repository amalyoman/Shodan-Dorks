public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("This is a sample Java application.");
        
        // Demonstrate basic Java features
        String message = "Welcome to Java programming!";
        System.out.println(message);
        
        // Simple loop example
        System.out.println("\nCounting from 1 to 5:");
        for (int i = 1; i <= 5; i++) {
            System.out.println("Count: " + i);
        }
        
        // Method call example
        greetUser("Developer");
    }
    
    // Simple method example
    public static void greetUser(String name) {
        System.out.println("\nHello, " + name + "!");
        System.out.println("Thank you for checking out this Java sample.");
    }
}