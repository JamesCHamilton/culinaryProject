import java.util.Scanner;
public class Ingredients{
  public static void italianDishes(Scanner scanner) {
    System.out.println("Italian dishes: ");
    final String[] ITALIANDISHES = {"Bolognese", "Parmigiana di melanzane", "Focaccia"};
    final String[][] DISHINGREDIENTS = {
            {"Olive oil", "Butter", "Carrots", "Celery", "Onion", "Heavy cream"," Half and half", "Ground beef", "Store-bought marinara sauce"},
            {"Eggplant", "Eggs", "Breadcrumbs", "Olive oil", "Spaghetti sauce", "Tomato sauce", "Mozzarella cheese", "Parmesan"},
            {"All-purpose flour", "Kosher salt", "Instant yeast", "Tap water", "Soft butter", "Olive oil", "Fresh herbs or Italian seasoning", "Flaky sea salt"}
    };
  for (int i = 0; i < ITALIANDISHES.length; i++){
    System.out.println(ITALIANDISHES[i]);
  }
  System.out.print("Choose one of the dishes above to list its ingredients (enter dish number): ");
  int chosenDishIndex = scanner.nextInt();
  if (chosenDishIndex >= 1 && chosenDishIndex <= ITALIANDISHES.length) {
    System.out.println("Ingredients of " + ITALIANDISHES[chosenDishIndex - 1] + ":");
    for (String ingredient : DISHINGREDIENTS[chosenDishIndex - 1]) {
      System.out.println("- " + ingredient);
    }
  } else {
      System.out.println("Invalid choice. Please choose one of the listed dishes.");
    }
  }
  public static void chineseDishes(Scanner scanner) {
    System.out.println("Chinese dishes: ");
    final String[] CHINESEDISHES = {"Chicken Udon Soup", "Scallion Pancakes with Dim Sum Dipper", "Air Fryer Egg Rolls"};
    final String[][] DISHINGREDIENTS = {{"Peanut oil", "Vegetable oil", "Boneless Chicken thigh", "Chicken breast", "Japaneese sake","Dry sherry", "Soy sauce", "Sugar", "Chicken broth", "Vegetable broth", "Brown mushrooms", "shiitake mushrooms","Green onions", "Ginger", "Cabbage", "Udon noodles"}, {"Flour", "Salt","Boiling water", "Grapeseel oil", "Olive oil","Sesame oil","Kosher salt","Sea salt","Scallions","Soy sauce","Scallions","Rice vinegar","Sambal oelek","Sesame oil"}, {"Cabbage","Carrots","Kosher salt","Shrimp","Vegetable oil", "Garlic", "Ginger","Char siu","Shaoxing rice wine","cooking sherry","oyster sauce","soy sauce","sugar","white pepper", "cornstarch","egg roll wrappers", "Canola oil spray","Sweet chili sauce", "duck sauce" }};
  for (int i = 0; i < CHINESEDISHES.length; i++){
    System.out.println(CHINESEDISHES[i]);
  }
  System.out.print("Choose one of the dishes above to list its ingredients (enter dish number): ");
  int chosenDishIndex = scanner.nextInt();

  if (chosenDishIndex >= 1 && chosenDishIndex <= CHINESEDISHES.length) {

  System.out.println("Ingredients of " + CHINESEDISHES[chosenDishIndex - 1] + ":");
  for (String ingredient : DISHINGREDIENTS[chosenDishIndex - 1]) {
    System.out.println("- " + ingredient);
  }
  } else {
      System.out.println("Invalid choice. Please choose one of the listed dishes.");
    }
  }
  public static void japaneseDishes(Scanner scanner){
    System.out.println("Japanese dishes: ");
    final String[] JAPANESEDISHES = {"Gyudon", "Soba Noodles Salad", "Tamago Sando (Japaneese Egg Sandwich)"};
    final String[][] DISHINGREDIENTS = {{"Onion","Sliced beef", "Dashi", "japanese soup stock","Sake", "Mirin","Soy sauce","Sugar","Japanese short-grain rice", "Pickled red ginger"}, {"Sesame oil","Crushes red pepper","Honey","Soy sauce", "Soba noodles", "buckwheat noodles","Onions","Cilantro","Coriander","Toasted white sesame seeds"}, {"Eggs", "Shokupan", "Japanese milk bread", "Salted butter","Sugar", "Kosher Salt", "Black pepper","Milk", "Kewpie mayonnaise"}};
    for (int i = 0; i < JAPANESEDISHES.length; i++){
      System.out.println(JAPANESEDISHES[i]);
    }

    System.out.print("Choose one of the dishes above to list its ingredients (enter dish number): ");
    int chosenDishIndex = scanner.nextInt();

    if (chosenDishIndex >= 1 && chosenDishIndex <= JAPANESEDISHES.length) {
      System.out.println("Ingredients of " + JAPANESEDISHES[chosenDishIndex - 1] + ":");
      for (String ingredient : DISHINGREDIENTS[chosenDishIndex - 1]) {
        System.out.println("- " + ingredient);
      }
    } else {
        System.out.println("Invalid choice. Please choose one of the listed dishes.");
      }
}
  public static void indianDishes(Scanner scanner){
    System.out.println("Indian dishes: ");
    final String[] INDIANDISHES = {"Chicken Tikka Masala", "Lentil Dal", "Biryani"};
    final String[][] DISHINGREDIENTS = {{"basmati rice", "chicken thighs", "Kosher salt", "black pepper","vegetable oil","onion","tomato paste", "garlic", "minced grated ginger", "garam masala","chili powder", "ground turmeric","tomato sauce", "chicken stock", "heavy cream", "Half and half", "fresh cilantro leaves"}, {"Vegetable oil", "yellow onion", "Garlic", "Ginger","Green chilis", "Cumin","Coriander","Turmeric","Paprika","Cinnamon", "Red lentils", "Diced tomatoes", "Vegetable broth","Kosher salt", "Ground black pepper", "Yogurt"}, {"Chicken", "turmeric powder","coriander powder","garam masala","salt", "Yogurt","Fried onions","Tomato Puree", "Ginger garlic paste","Whole Spices","Mint","Coriander leaves","Ghee","Basmati Rice"}};
    for (int i = 0; i < INDIANDISHES.length; i++){
      System.out.println(INDIANDISHES[i]);
    }
    System.out.print("Choose one of the dishes above to list its ingredients (enter dish number): ");
    int chosenDishIndex = scanner.nextInt();

    if (chosenDishIndex >= 1 && chosenDishIndex <= INDIANDISHES.length) {

    System.out.println("Ingredients of " + INDIANDISHES[chosenDishIndex - 1] + ":");
    for (String ingredient : DISHINGREDIENTS[chosenDishIndex - 1]) {
      System.out.println("- " + ingredient);
    }
    } else {
        System.out.println("Invalid choice. Please choose one of the listed dishes.");
      }
}
  public static void americanDishes(Scanner scanner){
    System.out.println("American dishes: ");
    final String[] AMERICANDISHES = {"Burger", "Pizza", "Hot Dog"};
    final String[][] DISHINGREDIENTS = {{"Ground beef", "Bread crumbs", "Egg", "Butter", "Tomato sauce", "Lettuce", "Cheese", "Onion", "Ketchup", "Mayonnaise"}, {"Dough", "Tomato sauce", "Cheese", "Pizza sauce", "Diced tomatoes", "Bell peppers", "Onion", "Mushrooms", "Bacon", "Hot sauce"}, {"Beef", "Bread crumbs", "Butter", "Ketchup", "Mustard", "Relish", "Hot sauce", "Onion", "Salt", "Pepper", "Relish"}};
    for (int i = 0; i < AMERICANDISHES.length; i++){
      System.out.println(AMERICANDISHES[i]);
    }

    System.out.print("Choose one of the dishes above to list its ingredients (enter dish number): ");
    int chosenDishIndex = scanner.nextInt();

    if (chosenDishIndex >= 1 && chosenDishIndex <= AMERICANDISHES.length) {
      System.out.println("Ingredients of " + AMERICANDISHES[chosenDishIndex - 1] + ":");
      for (String ingredient : DISHINGREDIENTS[chosenDishIndex - 1]) {
        System.out.println("- " + ingredient);
      }
    } else {
        System.out.println("Invalid choice. Please choose one of the listed dishes.");
      }
  }

}
