import java.util.Scanner;

public class Output {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String selectedCountry = UserInput.returnCountry(scanner);
            if (selectedCountry.equalsIgnoreCase("Italy")) {
                Ingredients.italianDishes(scanner);
            } else if (selectedCountry.equalsIgnoreCase("China")) {
                Ingredients.chineseDishes(scanner);
            } else if (selectedCountry.equalsIgnoreCase("Japan")) {
                Ingredients.japaneseDishes(scanner);
            } else if (selectedCountry.equalsIgnoreCase("India")) {
                Ingredients.indianDishes(scanner);
            } else if (selectedCountry.equalsIgnoreCase("America")) {
                Ingredients.americanDishes(scanner);
            } else {
                System.out.println("No valid country selected.");
            }
        scanner.close();
      }
}
