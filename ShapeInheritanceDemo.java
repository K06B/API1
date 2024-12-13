// Parent class representing a basic shape
class Shape {
    // Protected attribute that can be used by child classes
    protected String color;

    // Constructor
    public Shape(String color) {
        this.color = color;
    }

    // Method to calculate area (will be overridden by child classes)
    public double calculateArea() {
        System.out.println("Calculating area for a generic shape");
        return 0;
    }

    // Method to display shape information
    public void displayInfo() {
        System.out.println("This is a " + color + " shape.");
    }
}

// Child class representing a Rectangle
class Rectangle extends Shape {
    // Additional attributes specific to Rectangle
    private double length;
    private double width;

    // Constructor
    public Rectangle(String color, double length, double width) {
        // Call the parent class constructor
        super(color);
        this.length = length;
        this.width = width;
    }

    // Override the area calculation method
    @Override
    public double calculateArea() {
        double area = length * width;
        System.out.println("Rectangle Area: " + area + " square units");
        return area;
    }

    // Additional method specific to Rectangle
    public void displayDimensions() {
        System.out.println("Length: " + length + ", Width: " + width);
    }
}

// Child class representing a Circle
class Circle extends Shape {
    // Additional attribute specific to Circle
    private double radius;

    // Constructor
    public Circle(String color, double radius) {
        // Call the parent class constructor
        super(color);
        this.radius = radius;
    }

    // Override the area calculation method
    @Override
    public double calculateArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Circle Area: " + area + " square units");
        return area;
    }

    // Additional method specific to Circle
    public void displayRadius() {
        System.out.println("Radius: " + radius);
    }
}

// Main class to demonstrate inheritance
public class ShapeInheritanceDemo {
    public static void main(String[] args) {
        // Create a Rectangle object
        Rectangle rectangle = new Rectangle("Blue", 5, 3);
        // Demonstrate inherited and overridden methods
        rectangle.displayInfo();         // Inherited method
        rectangle.calculateArea();       // Overridden method
        rectangle.displayDimensions();   // Rectangle-specific method

        System.out.println(); // Add a blank line for readability

        // Create a Circle object
        Circle circle = new Circle("Red", 4);
        // Demonstrate inherited and overridden methods
        circle.displayInfo();            // Inherited method
        circle.calculateArea();          // Overridden method
        circle.displayRadius();          // Circle-specific method
    }
}