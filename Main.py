// Main
Application and Manager
Functionality
for APU Cafeteria System

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util. *;

// Main
application


class
    public

    class CafeteriaSystemMain {
    private static Scanner scanner = new Scanner(System.in );
    private static User currentUser = null;

    public static void main(String[] args) {
    System.out.println("=======================================================");
    System.out.println("     Welcome to APU Cafeteria Ordering System");
    System.out.println("=======================================================");


while (true) {
if (currentUser == null) {
showLoginMenu();
} else {
currentUser.displayDashboard();
handleUserInput();
}
}
}

private
static
void
showLoginMenu()
{
System.out.println("\n=== LOGIN MENU ===");
System.out.println("1. Login");
System.out.println("2. Register as Customer");
System.out.println("3. Exit System");
System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());
switch (choice) {
case 1:
    handleLogin();
break;
case
2:
handleCustomerRegistration();
break;
case
3:
System.out.println("Thank you for using APU Cafeteria System!");
System.exit(0);
break;
default:
System.out.println("Invalid choice. Please try again.");
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid input. Please enter a number.");
}
}

private
static
void
handleLogin()
{
    System.out.print("Enter username: ");
String
username = scanner.nextLine().trim();

System.out.print("Enter password: ");
String
password = scanner.nextLine().trim();

User
user = UserFileManager.findUserByUsername(username);

if (user != null & & user.authenticate(password))
{
    currentUser = user;
FileManager.logLoginActivity(username, user.getRole(), true);
System.out.println("Login successful! Welcome, " + user.getUsername());
} else {
    FileManager.logLoginActivity(username, "UNKNOWN", false);
System.out.println("Invalid username or password.");
}
}

private
static
void
handleCustomerRegistration()
{
    CustomerRegistrationManager.registerNewCustomer(scanner);
}

private
static
void
handleUserInput()
{
    System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());

if (currentUser instanceof Manager) {
handleManagerChoice(choice);
} else if (currentUser instanceof Customer) {
handleCustomerChoice(choice);
}
} catch (NumberFormatException e) {
System.out.println("Invalid input. Please enter a number.");
}
}

private
static
void
handleManagerChoice(int
choice) {
switch(choice)
{
    case
1: \
    MenuManager.manageMenuItems(scanner);
break;
case
2:
OrderManager.viewAllOrders();
break;
case
3:
CustomerRegistrationManager.manageCustomerRegistration(scanner);
break;
case
4:
PaymentFeedbackManager.viewPaymentsAndFeedback();
break;
case
5:
ReportGenerator.generateManagerReports(scanner);
break;
case
6:
logout();
break;
default:
System.out.println("Invalid choice. Please try again.");
}
}

private
static
void
handleCustomerChoice(int
choice) {
    Customer
customer = (Customer)
currentUser;
switch(choice)
{
case
1:
CustomerMenuManager.viewMenu();
break;
case
2:
CustomerOrderManager.createNewOrder(scanner, customer);
break;
case
3:
CustomerOrderManager.viewMyOrders(customer);
break;
case
4:
CustomerPaymentManager.makePayment(scanner, customer);
break;
case
5:
CustomerFeedbackManager.provideFeedback(scanner, customer);
break;
case
6:
CustomerProfileManager.updateProfile(scanner, customer);
break;
case
7:
logout();
break;
default:
System.out.println("Invalid choice. Please try again.");
}
}

private
static
void
logout()
{
    System.out.println("Logged out successfully. Thank you, " + currentUser.getUsername() + "!");
currentUser = null;
}

public
static
Scanner
getScanner()
{
return scanner;
}
}

// Manager
functionality - Menu
Management


class MenuManager {

public static void manageMenuItems(Scanner scanner) {


while (true) {
System.out.println("\n=== MENU MANAGEMENT ===");
System.out.println("1. View All Menu Items");
System.out.println("2. Add New Menu Item");
System.out.println("3. Update Menu Item");
System.out.println("4. Delete Menu Item");
System.out.println("5. Search Menu Items");
System.out.println("6. Back to Main Menu");
System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());
switch (choice) {
case 1:
    viewAllMenuItems();
break;
case
2:
addNewMenuItem(scanner);
break;
case
3:
updateMenuItem(scanner);
break;
case
4:
deleteMenuItem(scanner);
break;
case
5:
searchMenuItems(scanner);
break;
case
6:
return;
default:
System.out.println("Invalid choice. Please try again.");
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid input. Please enter a number.");
}
}
}

private
static
void
viewAllMenuItems()
{
    List < MenuItem > items = MenuFileManager.loadAllMenuItems();
if (items.isEmpty())
{
    System.out.println("No menu items found.");
return;
}

System.out.println("\n=== ALL MENU ITEMS ===");
System.out.printf("%-10s %-20s %-15s %-10s %-30s %-8s %-10s%n",
"Item ID", "Name", "Category", "Price", "Description", "Time", "Available");
System.out.println("=".repeat(110));

for (MenuItem item: items)
{
System.out.printf("%-10s %-20s %-15s $%-9.2f %-30s %-8d %-10s%n",
                  item.getItemId(), item.getItemName(), item.getCategory(),
                  item.getPrice(), item.getDescription(), item.getPreparationTime(),
                  item.isAvailable() ? "Yes": "No");
}
}

private
static
void
addNewMenuItem(Scanner
scanner) {
    System.out.println("\n=== ADD NEW MENU ITEM ===");

System.out.print("Enter item name: ");
String
itemName = scanner.nextLine().trim();
if (!ValidationUtils.isNotEmpty(itemName)) {
System.out.println("Item name cannot be empty.");
return;
}

System.out.print("Enter category (Main Course/Beverage/Snack/Dessert): ");
String
category = scanner.nextLine().trim();
if (!ValidationUtils.isNotEmpty(category)) {
System.out.println("Category cannot be empty.");
return;
}

double
price;
try {
System.out.print("Enter price: $");
price = Double.parseDouble(scanner.nextLine().trim());
if (!ValidationUtils.isValidPrice(price)) {
System.out.println("Invalid price. Must be between $0.01 and $1000.00");
return;
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid price format.");
return;
}

System.out.print("Enter description: ");
String
description = scanner.nextLine().trim();

int
prepTime;
try {
System.out.print("Enter preparation time (minutes): ");
prepTime = Integer.parseInt(scanner.nextLine().trim());
if (prepTime < 1 | | prepTime > 120) {
System.out.println("Preparation time must be between 1 and 120 minutes.");
return;
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid preparation time format.");
return;
}

String
itemId = MenuFileManager.generateNextItemId(category);
MenuItem
newItem = new
MenuItem(itemId, itemName, category, price, description, prepTime);

MenuFileManager.saveMenuItem(newItem);
System.out.println("Menu item added successfully with ID: " + itemId);
}

private
static
void
updateMenuItem(Scanner
scanner) {
    System.out.print("Enter item ID to update: ");
String
itemId = scanner.nextLine().trim();

MenuItem
item = MenuFileManager.findMenuItemById(itemId);
if (item == null)
{
System.out.println("Menu item not found.");
return;
}

System.out.println("\nCurrent item details:");
System.out.println(item);

System.out.print("Enter new name (press Enter to keep current): ");
String
newName = scanner.nextLine().trim();
if (!newName.isEmpty()) {
item.setItemName(newName);
}

System.out.print("Enter new price (press Enter to keep current): $");
String
priceStr = scanner.nextLine().trim();
if (!priceStr.isEmpty()) {
try {
double newPrice = Double.parseDouble(priceStr);
if (ValidationUtils.isValidPrice(newPrice)) {
item.setPrice(newPrice);
} else {
System.out.println("Invalid price. Keeping current price.");
}
} catch (NumberFormatException e) {
System.out.println("Invalid price format. Keeping current price.");
}
}

System.out.print("Is item available? (y/n, press Enter to keep current): ");
String
availableStr = scanner.nextLine().trim().toLowerCase();
if (!availableStr.isEmpty()) {
item.setAvailable(availableStr.equals("y") | | availableStr.equals("yes"));
}

if (MenuFileManager.updateMenuItem(item)) {
System.out.println("Menu item updated successfully.");
} else {
System.out.println("Failed to update menu item.");
}
}

private
static
void
deleteMenuItem(Scanner
scanner) {
    System.out.print("Enter item ID to delete: ");
String
itemId = scanner.nextLine().trim();

MenuItem
item = MenuFileManager.findMenuItemById(itemId);
if (item == null)
{
System.out.println("Menu item not found.");
return;
}

System.out.println("Item to delete: " + item);
System.out.print("Are you sure you want to delete this item? (y/n): ");
String
confirm = scanner.nextLine().trim().toLowerCase();

if (confirm.equals("y") | | confirm.equals("yes"))
{
if (MenuFileManager.deleteMenuItem(itemId)) {
System.out.println("Menu item deleted successfully.");
} else {
System.out.println("Failed to delete menu item.");
}
} else {
System.out.println("Deletion cancelled.");
}
}

private
static
void
searchMenuItems(Scanner
scanner) {
    System.out.println("\n=== SEARCH MENU ITEMS ===");
System.out.println("1. Search by category");
System.out.println("2. Search by name");
System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());
switch (choice) {
case 1:
    searchByCategory(scanner);
break;
case
2:
searchByName(scanner);
break;
default:
System.out.println("Invalid choice.");
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid input.");
}
}

private
static
void
searchByCategory(Scanner
scanner) {
    System.out.print("Enter category to search: ");
String
category = scanner.nextLine().trim();

List < MenuItem > items = MenuFileManager.findMenuItemsByCategory(category);
if (items.isEmpty())
{
    System.out.println("No items found in category: " + category);
} else {
    System.out.println("\nItems in category '" + category + "':");
for (MenuItem item: items)
{
System.out.println(item);
}
}
}

private
static
void
searchByName(Scanner
scanner) {
    System.out.print("Enter item name to search: ");
String
searchName = scanner.nextLine().trim().toLowerCase();

List < MenuItem > allItems = MenuFileManager.loadAllMenuItems();
List < MenuItem > matchingItems = new
ArrayList <> ();

for (MenuItem item: allItems)
{
if (item.getItemName().toLowerCase().contains(searchName))
{
matchingItems.add(item);
}
}

if (matchingItems.isEmpty()) {
System.out.println("No items found matching: " + searchName);
} else {
System.out.println("\nItems matching '" + searchName + "':");
for (MenuItem item: matchingItems) {
System.out.println(item);
}
}
}
}

// Manager
functionality - Order
Management


class OrderManager {

public static void viewAllOrders() {
List < Order > orders = OrderFileManager.loadAllOrders();
if (orders.isEmpty()) {
System.out.println("No orders found.");


return;
}

System.out.println("\n=== ALL ORDERS ===");
System.out.printf("%-12s %-15s %-20s %-15s %-10s %-12s %-15s%n",
"Order ID", "Customer ID", "Customer Name", "Order Date", "Amount", "Status", "Payment");
System.out.println("=".repeat(105));

DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

for (Order order: orders)
{
System.out.printf("%-12s %-15s %-20s %-15s $%-9.2f %-12s %-15s%n",
                  order.getOrderId(), order.getCustomerId(), order.getCustomerName(),
                  order.getOrderDate().format(formatter), order.getTotalAmount(),
                  order.getOrderStatus(), order.getPaymentStatus());
}

System.out.println("\nWould you like to view details of a specific order? (y/n)");
Scanner
scanner = CafeteriaSystemMain.getScanner();
String
response = scanner.nextLine().trim().toLowerCase();

if (response.equals("y") | | response.equals("yes"))
{
viewOrderDetails(scanner);
}
}

private
static
void
viewOrderDetails(Scanner
scanner) {
    System.out.print("Enter Order ID: ");
String
orderId = scanner.nextLine().trim();

Order
order = OrderFileManager.findOrderById(orderId);
if (order == null)
{
System.out.println("Order not found.");
return;
}

System.out.println("\n=== ORDER DETAILS ===");
System.out.println("Order ID: " + order.getOrderId());
System.out.println("Customer: " + order.getCustomerName() + " (" + order.getCustomerId() + ")");
System.out.println("Order Date: " + order.getOrderDate().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
System.out.println("Status: " + order.getOrderStatus());
System.out.println("Payment Status: " + order.getPaymentStatus());
System.out.println("Total Amount: $" + String.format("%.2f", order.getTotalAmount()));

if (order.getSpecialNotes() != null & & !order.getSpecialNotes().isEmpty()) {
System.out.println("Special Notes: " + order.getSpecialNotes());
}

System.out.println("\nOrder Items:");
System.out.printf("%-10s %-20s %-8s %-10s %-10s%n", "Item ID", "Item Name", "Qty", "Unit Price", "Total");
System.out.println("=".repeat(65));

for (OrderItem item: order.getOrderItems()) {
System.out.printf("%-10s %-20s %-8d $%-9.2f $%-9.2f%n",
                  item.getItemId(), item.getItemName(), item.getQuantity(),
                  item.getUnitPrice(), item.getTotalPrice());

if (item.getSpecialInstructions() != null & & !item.getSpecialInstructions().isEmpty()) {
System.out.println("    Special Instructions: " + item.getSpecialInstructions());
}
}

// Option
to
update
order
status
System.out.println("\nWould you like to update the order status? (y/n)");
String
updateResponse = scanner.nextLine().trim().toLowerCase();

if (updateResponse.equals("y") | | updateResponse.equals("yes"))
{
updateOrderStatus(scanner, order);
}
}

private
static
void
updateOrderStatus(Scanner
scanner, Order
order) {
    System.out.println("\nCurrent status: " + order.getOrderStatus());
System.out.println("Select new status:");
System.out.println("1. PENDING");
System.out.println("2. CONFIRMED");
System.out.println("3. PREPARING");
System.out.println("4. READY");
System.out.println("5. COMPLETED");
System.out.println("6. CANCELLED");
System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());
String newStatus;

switch (choice) {
case 1: newStatus = "PENDING";
break;
case
2: newStatus = "CONFIRMED";
break;
case
3: newStatus = "PREPARING";
break;
case
4: newStatus = "READY";
break;
case
5: newStatus = "COMPLETED";
break;
case
6: newStatus = "CANCELLED";
break;
default:
System.out.println("Invalid choice.");
return;
}

order.setOrderStatus(newStatus);

// Set
estimated
pickup
time
for preparing orders
if (newStatus.equals("PREPARING")) {
System.out.print("Enter estimated preparation time (minutes): ");
try {
int prepTime = Integer.parseInt(scanner.nextLine().trim());
order.setEstimatedPickupTime(LocalDateTime.now().plusMinutes(prepTime));
} catch (NumberFormatException e) {
System.out.println("Invalid time format. Using default 30 minutes.");
order.setEstimatedPickupTime(LocalDateTime.now().plusMinutes(30));
}
}

if (OrderFileManager.updateOrder(order)) {
System.out.println("Order status updated successfully to: " + newStatus);
} else {
System.out.println("Failed to update order status.");
}

} catch(NumberFormatException
e) {
    System.out.println("Invalid input.");
}
}
}

// Manager
functionality - Customer
Registration
Management


class CustomerRegistrationManager {

public static void manageCustomerRegistration(Scanner scanner) {


while (true) {
System.out.println("\n=== CUSTOMER REGISTRATION MANAGEMENT ===");
System.out.println("1. View All Customers");
System.out.println("2. Register New Customer");
System.out.println("3. Update Customer Information");
System.out.println("4. Deactivate Customer");
System.out.println("5. Search Customers");
System.out.println("6. Back to Main Menu");
System.out.print("Enter your choice: ");

try {
int choice = Integer.parseInt(scanner.nextLine().trim());
switch (choice) {
case 1:
    viewAllCustomers();
break;
case
2:
registerNewCustomer(scanner);
break;
case
3:
updateCustomerInformation(scanner);
break;
case
4:
deactivateCustomer(scanner);
break;
case
5:
searchCustomers(scanner);
break;
case
6:
return;
default:
System.out.println("Invalid choice. Please try again.");
}
} catch(NumberFormatException
e) {
    System.out.println("Invalid input. Please enter a number.");
}
}
}

private
static
void
viewAllCustomers()
{
    List < User > allUsers = UserFileManager.loadAllUsers();
List < Customer > customers = new
ArrayList <> ();

for (User user: allUsers)
{
if (user instanceof Customer)
{
    customers.add((Customer)
user);
}
}

if (customers.isEmpty()) {
System.out.println("No customers found.");
return;
}

System.out.println("\n=== ALL CUSTOMERS ===");
System.out.printf("%-12s %-15s %-25s %-15s %-12s %-8s%n",
"Customer ID", "Username", "Email", "Phone", "Total Spent", "Points");
System.out.println("=".repeat(90));

for (Customer customer: customers)
{
System.out.printf("%-12s %-15s %-25s %-15s $%-11.2f %-8d%n",
                  customer.getUserId(), customer.getUsername(), customer.getEmail(),
                  customer.getPhoneNumber(), customer.getTotalSpent(), customer.getLoyaltyPoints());
}
}

public
static
void
registerNewCustomer(Scanner
scanner) {
    System.out.println("\n=== REGISTER NEW CUSTOMER ===");

System.out.print("Enter username: ");
String
username = scanner.nextLine().trim();
if (!ValidationUtils.isNotEmpty(username)) {
System.out.println("Username cannot be empty.");
return;
}

// Check if username
already
exists
if (UserFileManager.findUserByUsername(username) != null)
{
System.out.println("Username already exists. Please choose a different username.");
return;
}

System.out.print("Enter password: ");
String
password = scanner.nextLine().trim();
if (!ValidationUtils.isValidPassword(password)) {
System.out.println("Password must be at least 6 characters long.");
return;
}

System.out.print("Enter email: ");
String
email = scanner.nextLine().trim();
if (!ValidationUtils.isValidEmail(email)) {
System.out.println("Invalid email format.");
return;
}

System.out.print("Enter phone number: ");
String
phoneNumber = scanner.nextLine().trim();
if (!ValidationUtils.isValidPhoneNumber(phoneNumber)) {
System.out.println("Invalid phone number format.");
return;
}

System.out.print("Enter address: ");
String
address = scanner.nextLine().trim();

String
customerId = UserFileManager.generateNextUserId("CUSTOMER");
Customer
newCustomer = new
Customer(customerId, username, password, email, phoneNumber, address);

UserFileManager.saveUser(newCustomer);
System.out.println("Customer registered successfully with ID: " + customerId);
}

private
static
void
updateCustomerInformation(Scanner
scanner) {
    System.out.print("Enter customer ID or username: ");
String
identifier = scanner.nextLine().trim();

User
user = UserFileManager.findUserById(identifier);
if (user == null)
{
user = UserFileManager.findUserByUsername(identifier);
}

if (user == null | | !(user instanceof Customer)) {
System.out.println("Customer not found.");
return;
}

Customer
customer = (Customer)
user;
System.out.println("\nCurrent customer information:");
System.out.println("ID: " + customer.getUserId());
System.out.println("Username: " + customer.getUsername());
System.out.println("Email: " + customer.getEmail());
System.out.println("Phone: " + customer.getPhoneNumber());
System.out.println("Address: " + customer.getAddress());

System.out.print("Enter new email (press Enter to keep current): ");
String
newEmail = scanner.nextLine().trim();
if (!newEmail.isEmpty() & & ValidationUtils.isValidEmail(newEmail)) {
customer.setEmail(newEmail);
}

System.out.print("Enter new phone number (press Enter to keep current): ");
String
newPhone = scanner.nextLine().trim();
if (!newPhone.isEmpty() & & ValidationUtils.isValidPhoneNumber(newPhone)) {
customer.setPhoneNumber(newPhone);
}

System.out.print("Enter new address (press Enter to keep current): ");
String
newAddress = scanner.nextLine().trim();
if (!newAddress.isEmpty()) {
customer.setAddress(newAddress);
}

if (UserFileManager.updateUser(customer)) {
System.out.println("Customer information updated successfully.");
} else {
System.out.println("Failed to update customer information.");
}
}

private
static
void
deactivateCustomer(Scanner
scanner) {
    System.out.print("Enter customer ID or username to deactivate: ");
String
identifier = scanner.nextLine().trim();

User
user = UserFileManager.findUserById(identifier);
if (user == null)
{
user = UserFileManager.findUserByUsername(identifier);
}

if (user == null | | !(user instanceof Customer)) {
System.out.println("Customer not found.");
return;
}

System.out.println("Customer: " + user.getUsername() + " (" + user.getUserId() + ")");
System.out.print("Are you sure you want to deactivate this customer? (y/n): ");
String
confirm = scanner.nextLine().trim().toLowerCase();

if (confirm.equals("y") | | confirm.equals("yes"))
{
user.setActive(false);
if (UserFileManager.updateUser(user)) {
System.out.println("Customer deactivated successfully.");
} else {
System.out.println("Failed to deactivate customer.");
}
} else {
System.out.println("Deactivation cancelled.");
}
}

private
static
void
searchCustomers(Scanner
scanner) {
    System.out.print("Enter search term (username, email, or phone): ");
String
searchTerm = scanner.nextLine().trim().toLowerCase();

List < User > allUsers = UserFileManager.loadAllUsers();
List < Customer > matchingCustomers = new
ArrayList <> ();

for (User user: allUsers)
{
if (user instanceof Customer) {
Customer customer = (Customer) user;
if (customer.getUsername().toLowerCase().contains(searchTerm) | |
customer.getEmail().toLowerCase().contains(searchTerm) | |
customer.getPhoneNumber().contains(searchTerm)) {
matchingCustomers.add(customer);
}
}
}

if (matchingCustomers.isEmpty()) {
System.out.println("No customers found matching: " + searchTerm);
} else {
System.out.println("\nCustomers matching '" + searchTerm + "':");
System.out.printf("%-12s %-15s %-25s %-15s%n",
                  "Customer ID", "Username", "Email", "Phone");
System.out.println("=".repeat(70));

for (Customer customer: matchingCustomers) {
    System.out.printf("%-12s %-15s %-25s %-15s%n",
                      customer.getUserId(), customer.getUsername(),
                      customer.getEmail(), customer.getPhoneNumber());
}
}
}
}