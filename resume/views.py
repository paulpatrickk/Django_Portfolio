from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")


def projects(request):
    projects_show = [
        {
            'title': 'POS for Coffee Shop',
            'path': 'images/Group1_FTP.png',
        },
        {
            'title': 'Portfolio',
            'path': 'images/polportfolio.jpg',
        },
        {
            'title': 'Text-Based Console Game',
            'code': """<//main
import java.util.Random;
import java.util.Scanner;

public class TextBasedGame {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Player Setup
        System.out.print("Enter your name: ");
        String playerName = scanner.nextLine();
        Player player = new Player(playerName);

        // Game Mode Selection
        System.out.println("Select your game mode:");
        System.out.println("1 - Story Mode");
        System.out.println("2 - Survival Mode");
        int gameModeChoice = scanner.nextInt();
        scanner.nextLine(); // Consume a newline

        GameMode gameMode;
        if (gameModeChoice == 1) { //story mode
            gameMode = new StoryMode(player, scanner);
        } else if (gameModeChoice == 2) { //survival mode
            gameMode = new SurvivalMode(player, scanner);
        } else {
            System.out.println("Invalid choice. Exiting the game.");//if wrong

            return;
        }

        gameMode.startGame();

    }
}

//Character class
public abstract class Character {
    protected String name;
    protected int health;
    protected int damage;
    protected int defense;

    public Character(String name, int health, int damage, int defense) {
        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
    }

    public boolean isAlive() {
        return health > 0;
    }

    public void takeDamage(int damage) {
        health -= Math.max(0, damage - defense);
    }

    public abstract void attack(Character target);
}

//Enemy Class
public class Enemy extends Character {
    public Enemy(String name, int health, int damage) {
        super(name, health, damage, 0); // Enemies don't have defense
    }

    @Override
    public void attack(Character target) {
        int damageDealt = (int) (Math.random() * damage) + 1;
        System.out.println(name + " attacks and deals " + damageDealt + " damage!");
        target.takeDamage(damageDealt);
    }

    // Generate a random enemy
    public static Enemy generateRandomEnemy() {
        Random random = new Random();
        String[] enemyNames = {"Goblin", "Orc", "Troll", "Bandit", "Skeleton"};
        String name = enemyNames[random.nextInt(enemyNames.length)];
        int health = 100;
        int damage = random.nextInt(55) + 30;
        return new Enemy(name, health, damage);
    }
}
//Gamemode Class
public interface GameMode {
    void startGame();
}

//Item Class
public class Item {
    private String name;
    private int cost;
    private int value;

    public Item(String name, int cost, int value) {
        this.name = name;
        this.cost = cost;
        this.value = value;
    }

    public String getName() {
        return name;
    }

    public int getCost() {
        return cost;
    }

    public int getValue() {
        return value;
    }
}

//Player Class
public class Player extends Character {
    private int money;
    private int potions;
    private int strengthPotions;
    private int strengthTurns; // Tracks temporary attack boost duration
    private int maxHealth;

    public Player(String name) {
        super(name, 100, 30, 30); // Starting health, damage, defense
        this.money = 100;         // Starting gold
        this.potions = 1;        // Starting health potions
        this.strengthPotions = 1; // Starting strength potions
        this.strengthTurns = 0;  // No active boosts initially
        this.maxHealth = 100; // Initialize maxHealth
    }

    public int getMoney() {
        return money;
    }

    public int getPotions() {
        return potions;
    }

    public int getStrengthPotions() {
        return strengthPotions;
    }
    public int getMaxHealth() {
    return maxHealth;
}


    public void addMoney(int amount) {
        money += amount;
    }

    public void addPotion(int amount) {
        potions += amount;
    }

    public void addStrengthPotion(int amount) {
        strengthPotions += amount;
    }

    public void heal(int amount) {
        health = Math.min(100, health + amount);

    }

    @Override
    public void attack(Character target) {
        int damageBoost = strengthTurns > 0 ? 5 : 0; // +5 damage boost for strength potion
        int damageDealt = (int) (Math.random() * (damage + damageBoost)) + 1;
        System.out.println(name + " attacks and deals " + damageDealt + " damage!");
        target.takeDamage(damageDealt);

        if (strengthTurns > 0) {
            strengthTurns--; // Decrease duration of the attack boost
        }
    }

    public void useStrengthPotion() {
        if (strengthPotions > 0) {
            System.out.println("You use a Strength Potion! Your attacks are boosted for 3 turns.");
            strengthTurns = 3; // Boost active for 3 turns
            strengthPotions--;
        } else {
            System.out.println("No Strength Potions left!");
        }
    }

    // Display player stats
    public void displayStats() {
        System.out.println("\n--- Player Stats ---");
        System.out.println("Name: " + name);
        System.out.println("Health: " + health);
        System.out.println("Damage: " + damage + (strengthTurns > 0 ? " (Boosted)" : ""));
        System.out.println("Defense: " + defense);
        System.out.println("Gold: " + money);
        System.out.println("Health Potions: " + potions);
        System.out.println("Strength Potions: " + strengthPotions);
        System.out.println("--------------------");
    }
}

//Shop Class
import java.util.Scanner;

public class Shop {
    public void visit(Player player, Scanner scanner) {
    boolean inShop = true;
    while (inShop) {
        player.displayStats();
        System.out.println("Welcome to the shop! What would you like to buy?");
        System.out.println("1. Armor");
        System.out.println("2. Weapons");
        System.out.println("3. Potions");
        System.out.println("4. Exit Shop");
        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        switch (choice) {
            case 1 -> armorShop(player, scanner);
            case 2 -> weaponShop(player, scanner);
            case 3 -> potionShop(player, scanner);
            case 4 -> inShop = false;
            default -> System.out.println("Invalid choice. Please try again.");
        }
    }
}

private void armorShop(Player player, Scanner scanner) {
    System.out.println("Armor Shop:");
    System.out.println("1. Helmet (50 gold)");
    System.out.println("2. Chestplate (70 gold)");
    System.out.println("3. Leggings (60 gold)");
    System.out.println("4. Boots (40 gold)");
    System.out.println("5. Back to Shop");
    System.out.print("Enter your choice: ");
    int choice = scanner.nextInt();
    scanner.nextLine(); // Consume newline
    switch (choice) {
        case 1 -> buyArmor(player, "Helmet", 50, 10);
        case 2 -> buyArmor(player, "Chestplate", 70, 15);
        case 3 -> buyArmor(player, "Leggings", 60, 12);
        case 4 -> buyArmor(player, "Boots", 40, 8);
        case 5 -> {}
        default -> System.out.println("Invalid choice. Please try again.");
    }
}

private void buyArmor(Player player, String name, int cost, int defenseBoost) {
    if (player.getMoney() >= cost) {
        player.defense += defenseBoost;
        player.addMoney(-cost);
        System.out.println("You bought " + name + "! Defense increased.");
    } else {
        System.out.println("Not enough gold.");
    }
}

private void weaponShop(Player player, Scanner scanner) {
    System.out.println("Weapon Shop:");
    System.out.println("1. Short Sword (50 gold)");
    System.out.println("2. Long Sword (70 gold)");
    System.out.println("3. Bow (60 gold)");
    System.out.println("4. Back to Shop");
    System.out.print("Enter your choice: ");
    int choice = scanner.nextInt();
    scanner.nextLine(); // Consume newline
    switch (choice) {
        case 1 -> buyWeapon(player, "Short Sword", 50, 10);
        case 2 -> buyWeapon(player, "Long Sword", 70, 15);
        case 3 -> buyWeapon(player, "Bow", 60, 12);
        case 4 -> {}
        default -> System.out.println("Invalid choice. Please try again.");
    }
}

private void buyWeapon(Player player, String name, int cost, int damageBoost) {
    if (player.getMoney() >= cost) {
        player.damage += damageBoost;
        player.addMoney(-cost);
        System.out.println("You bought " + name + "! Attack damage increased.");
    } else {
        System.out.println("Not enough gold.");
    }
}

private void potionShop(Player player, Scanner scanner) {
    System.out.println("Potion Shop:");
    System.out.println("1. Health Potion (30 gold)");
    System.out.println("2. Strength Potion (40 gold)");
    System.out.println("3. Back to Shop");
    System.out.print("Enter your choice: ");
    int choice = scanner.nextInt();
    scanner.nextLine(); //
}
}

//StoryMode Class
import java.util.Scanner;

public class StoryMode implements GameMode {
    private Player player;
    private Scanner scanner;
    private Shop shop = new Shop();

    public StoryMode(Player player, Scanner scanner) {
        this.player = player;
        this.scanner = scanner;
    }

    @Override
public void startGame() {
    for (int day = 1; day <= 10; day++) {
        System.out.println("\n--- Day " + day + " ---");
        player.displayStats();
        System.out.println("Would you like to complete tasks to earn 50 gold? (yes/no)");
        String taskChoice = scanner.nextLine().trim().toLowerCase(); // Convert to lowercase
        if (taskChoice.equals("yes")) {
            System.out.println("You completed tasks and earned 50 gold!");
            player.addMoney(50);
        }
        shop.visit(player, scanner);
        System.out.println("Would you like to proceed to the next day? (yes/no)");
        String nextDayChoice = scanner.nextLine().trim().toLowerCase(); // Convert to lowercase
        if (!nextDayChoice.equals("yes")) {
            System.out.println("You ended Story Mode early.");
            return;
        }
    }
}
}

//SurvivalMode Class
import java.util.Random;
import java.util.Scanner;

public class SurvivalMode implements GameMode {
    private Player player;
    private Scanner scanner;

    public SurvivalMode(Player player, Scanner scanner) {
        this.player = player;
        this.scanner = scanner;
    }

    @Override
public void startGame() {
    System.out.println("Welcome to Survival Mode, " + player.name + "!");
    while (player.isAlive()) {
        // Generate a random enemy
        Enemy enemy = Enemy.generateRandomEnemy();
        System.out.println("\nAn enemy appears! Name: " + enemy.name + ", Health: " + enemy.health);

        // Show player stats at the start of the battle
        player.displayStats();
        displayHealthBar(player);

        while (enemy.isAlive() && player.isAlive()) {
            // Display enemy health at the start of each turn
            System.out.println("\n--- Enemy Stats ---");
            System.out.println("Name: " + enemy.name);
            System.out.println("Health: " + enemy.health);
            System.out.println("--------------------");

            // Player actions
            System.out.println("Choose your action: 1. Attack 2. Heal 3. Use Strength Potion 4. Visit Shop 5. Run");
            int action = scanner.nextInt();
            switch (action) {
                case 1 -> {
                    player.attack(enemy);
                    // Player attacks the enemy
                    if (enemy.isAlive()) {
                        enemy.attack(player);
                        // Enemy counterattacks if still alive
                    }
                }
                case 2 -> {
                    if (player.getPotions() > 0) {
                        player.heal(30);
                        player.addPotion(-1);
                        System.out.println("You used a health potion! Health restored.");
                    } else {
                        System.out.println("No health potions left!");
                    }
                }
                case 3 -> player.useStrengthPotion();
                case 4 -> {
                    Shop shop = new Shop();
                    shop.visit(player, scanner);
                }
                case 5 -> {
                    System.out.println("You ran away!");
                    return;
                }
                default -> System.out.println("Invalid action.");
            }
            displayHealthBar(player);
        }
        if (player.isAlive()) {
            System.out.println("You defeated the enemy and earned 50 gold!");
            player.addMoney(50);
        }
    }
    System.out.println("You were defeated. Game Over.");
}

private void displayHealthBar(Player player) {
    int healthPercentage = (int) ((player.health / (double) player.getMaxHealth()) * 100);
    int healthBarLength = 20;
    int healthBarFilled = (int) (healthPercentage / 100.0 * healthBarLength);
    StringBuilder healthBar = new StringBuilder();
    for (int i = 0; i < healthBarFilled; i++) {
        healthBar.append("=");
    }
    for (int i = 0; i < healthBarLength - healthBarFilled; i++) {
        healthBar.append("-");
    }
    System.out.println("\n--- Player Health ---");
    System.out.println(player.name + "'s Health: " + player.health + "/" + player.getMaxHealth());
    System.out.println(healthBar);
    System.out.println("--------------------");
}
}>"""
        },
    ]
    return render(request, "projects.html", {"projects_show": projects_show})



def experience(request):
    experience=[
        {"company":"Pan-tea Milktea Shop",
         "position":"Barista"},

    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/Balbalosa PaulPatrick Resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="Balbalosa PaulPatrick Resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
