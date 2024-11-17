import java.util.Scanner;

public class UserInput {
    public static String returnCountry(Scanner scanner) {
        String[] regions = {"Italy", "China", "Japan", "India", "America"};
        String returnedCountry = null;
        boolean found = false;
        while (!found) {
                System.out.print("Would you like your cuisine to be from Italy, China, Japan, India, or America? ");
                String country = scanner.nextLine();

                for (String region : regions) {
                    if (country.equalsIgnoreCase(region)) {
                        returnedCountry = region;
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    System.out.println("Please pick a country from Italy, China, Japan, India, or America.");
                }
            }

            return returnedCountry;
    }
}
