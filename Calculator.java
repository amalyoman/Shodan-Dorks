/**
 * A simple Calculator class demonstrating basic Java OOP concepts
 */
public class Calculator {
    private String name;
    
    // Constructor
    public Calculator(String name) {
        this.name = name;
    }
    
    // Addition method
    public double add(double a, double b) {
        return a + b;
    }
    
    // Subtraction method
    public double subtract(double a, double b) {
        return a - b;
    }
    
    // Multiplication method
    public double multiply(double a, double b) {
        return a * b;
    }
    
    // Division method with error handling
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero!");
        }
        return a / b;
    }
    
    // Power method
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }
    
    // Getter for name
    public String getName() {
        return name;
    }
    
    // Main method to demonstrate usage
    public static void main(String[] args) {
        Calculator calc = new Calculator("Java Calculator");
        
        System.out.println("=== " + calc.getName() + " ===");
        System.out.println();
        
        // Demonstrate basic operations
        double x = 10.0;
        double y = 3.0;
        
        System.out.println("Numbers: " + x + " and " + y);
        System.out.println("Addition: " + x + " + " + y + " = " + calc.add(x, y));
        System.out.println("Subtraction: " + x + " - " + y + " = " + calc.subtract(x, y));
        System.out.println("Multiplication: " + x + " * " + y + " = " + calc.multiply(x, y));
        System.out.println("Division: " + x + " / " + y + " = " + calc.divide(x, y));
        System.out.println("Power: " + x + " ^ " + y + " = " + calc.power(x, y));
        
        // Demonstrate error handling
        try {
            System.out.println("\nTrying to divide by zero...");
            calc.divide(x, 0);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        System.out.println("\nCalculation completed successfully!");
    }
}