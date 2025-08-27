import java.util.Scanner;

public class Task1 {
    public static double celsiusToFahrenheit(double c) {
        return (c * 9/5) + 32;
    }
    public static double fahrenheitToCelsius(double f) {
        return (f - 32) * 5/9;
    }
    public static double celsiusToKelvin(double c) {
        return c + 273.15;
    }
    public static double kelvinToCelsius(double k) {
        return k - 273.15;
    }
    public static double fahrenheitToKelvin(double f) {
        return celsiusToKelvin(fahrenheitToCelsius(f));
    }
    public static double kelvinToFahrenheit(double k) {
        return celsiusToFahrenheit(kelvinToCelsius(k));
    }
    public static double convertTemperature(double value, String fromScale, String toScale) {
        fromScale = fromScale.toLowerCase();
        toScale = toScale.toLowerCase();
        if (fromScale.equals(toScale)) return value;
        switch (fromScale) {
            case "celsius":
                if (toScale.equals("fahrenheit")) return celsiusToFahrenheit(value);
                if (toScale.equals("kelvin")) return celsiusToKelvin(value);
                break;
            case "fahrenheit":
                if (toScale.equals("celsius")) return fahrenheitToCelsius(value);
                if (toScale.equals("kelvin")) return fahrenheitToKelvin(value);
                break;
            case "kelvin":
                if (toScale.equals("celsius")) return kelvinToCelsius(value);
                if (toScale.equals("fahrenheit")) return kelvinToFahrenheit(value);
                break;
        }
        throw new IllegalArgumentException("Invalid scale name! Use Celsius, Fahrenheit, or Kelvin.");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Temperature Converter");
        System.out.print("Enter temperature value: ");
        double value = sc.nextDouble();
        sc.nextLine();
        System.out.print("Enter the scale of the value (Celsius, Fahrenheit, Kelvin): ");
        String fromScale = sc.nextLine();
        System.out.print("Enter the scale to convert to (Celsius, Fahrenheit, Kelvin): ");
        String toScale = sc.nextLine();
        try {
            double result = convertTemperature(value, fromScale, toScale);
            System.out.printf("%.2f %s = %.2f %s%n", value, capitalize(fromScale), result, capitalize(toScale));
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        sc.close();
    }
    public static String capitalize(String str) {
        if (str == null || str.isEmpty()) return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }
}
