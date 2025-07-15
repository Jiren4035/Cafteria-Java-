// File
Management
Classes
for APU Cafeteria System

import java.io. *;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util. *;

// Utility


class for file operations


public


class FileManager {
private static final String DATA_DIRECTORY = "data/";
private static final String USERS_FILE = DATA_DIRECTORY + "users.txt";
private static final String MENU_ITEMS_FILE = DATA_DIRECTORY + "menu_items.txt";
private static final String ORDERS_FILE = DATA_DIRECTORY + "orders.txt";
private static final String ORDER_ITEMS_FILE = DATA_DIRECTORY + "order_items.txt";
private static final String PAYMENTS_FILE = DATA_DIRECTORY + "payments.txt";
private static final String FEEDBACK_FILE = DATA_DIRECTORY + "feedback.txt";
private static final String LOGIN_LOG_FILE = DATA_DIRECTORY + "login_log.txt";

static {
initializeDataDirectory();
}

private static void initializeDataDirectory() {
File directory = new File(DATA_DIRECTORY);
if (!directory.exists()) {
directory.mkdirs();
}

// Create files if they don't exist
createFileIfNotExists(USERS_FILE);
createFileIfNotExists(MENU_ITEMS_FILE);
createFileIfNotExists(ORDERS_FILE);
createFileIfNotExists(ORDER_ITEMS_FILE);
createFileIfNotExists(PAYMENTS_FILE);
createFileIfNotExists(FEEDBACK_FILE);
createFileIfNotExists(LOGIN_LOG_FILE);

// Initialize with default data if files are empty
initializeDefaultData();
}

private static void createFileIfNotExists(String filename) {
File file = new File(filename);


try {
if (!file.exists()) {
file.createNewFile();
}
} catch (IOException e) {
System.err.println("Error creating file: " + filename);
e.printStackTrace();
}
}

private
static
void
initializeDefaultData()
{
// Initialize
default
manager if users
file is empty
if (isFileEmpty(USERS_FILE)) {
Manager defaultManager = new Manager("MGR001", "admin", "admin123", "admin@apu.edu.my", "Cafeteria", "Senior");
UserFileManager.saveUser(defaultManager);

Customer defaultCustomer = new Customer("CUST001", "customer", "cust123", "customer@apu.edu.my", "0123456789", "APU Campus");
UserFileManager.saveUser(defaultCustomer);
}

// Initialize
default
menu
items if menu
file is empty
if (isFileEmpty(MENU_ITEMS_FILE)) {
initializeDefaultMenu();
}
}

private
static
void
initializeDefaultMenu()
{
List < MenuItem > defaultItems = Arrays.asList(
    new
MenuItem("FOOD001", "Nasi Lemak", "Main Course", 8.50, "Traditional Malaysian rice dish", 15),
new
MenuItem("FOOD002", "Chicken Rice", "Main Course", 7.00, "Hainanese chicken rice", 12),
new
MenuItem("FOOD003", "Mee Goreng", "Main Course", 6.50, "Fried noodles with vegetables", 10),
new
MenuItem("DRINK001", "Teh Tarik", "Beverage", 2.50, "Traditional milk tea", 5),
new
MenuItem("DRINK002", "Coffee", "Beverage", 3.00, "Hot coffee", 3),
new
MenuItem("SNACK001", "Curry Puff", "Snack", 2.00, "Pastry with potato filling", 8),
new
MenuItem("DESSERT001", "Ice Kacang", "Dessert", 4.50, "Shaved ice dessert", 7)
);

for (MenuItem item: defaultItems) {
    MenuFileManager.saveMenuItem(item);
}
}

private
static
boolean
isFileEmpty(String
filename) {
File
file = new
File(filename);
return file.length() == 0;
}

// Generic
file
operations
public
static
void
writeToFile(String
filename, String
content, boolean
append) {
try (PrintWriter writer = new PrintWriter(new FileWriter(filename, append))) {
writer.println(content);
} catch (IOException e) {
System.err.println("Error writing to file: " + filename);
e.printStackTrace();
}
}

public
static
List < String > readFromFile(String
filename) {
List < String > lines = new
ArrayList <> ();
try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
String line;
while ((line = reader.readLine()) != null) {
if (!line.trim().isEmpty()) {
lines.add(line);
}
}
} catch(IOException
e) {
System.err.println("Error reading from file: " + filename);
e.printStackTrace();
}
return lines;
}

public
static
void
logLoginActivity(String
username, String
userType, boolean
successful) {
DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String
logEntry = LocalDateTime.now().format(formatter) + "," + username + "," +
userType + "," + (successful ? "SUCCESS": "FAILED");
writeToFile(LOGIN_LOG_FILE, logEntry, true);
}

// File
getters
public
static
String
getUsersFile()
{
return USERS_FILE;}
public
static
String
getMenuItemsFile()
{
return MENU_ITEMS_FILE;}
public
static
String
getOrdersFile()
{
return ORDERS_FILE;}
public
static
String
getOrderItemsFile()
{
return ORDER_ITEMS_FILE;}
public
static
String
getPaymentsFile()
{
return PAYMENTS_FILE;}
public
static
String
getFeedbackFile()
{
return FEEDBACK_FILE;}
public
static
String
getLoginLogFile()
{
return LOGIN_LOG_FILE;}
}

// User
file
management


class UserFileManager {

public static void saveUser(User user) {
FileManager.writeToFile(FileManager.getUsersFile(), user.toFileString(), true);
}

public static List < User > loadAllUsers() {
List < User > users = new ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getUsersFile());

for (String line: lines

) {
    User
user = User.fromFileString(line);
if (user != null)
{
    users.add(user);
}
}
return users;
}

public
static
User
findUserByUsername(String
username) {
List < User > users = loadAllUsers();
return users.stream()
.filter(user -> user.getUsername().equals(username))
.findFirst()
.orElse(null);
}

public
static
User
findUserById(String
userId) {
List < User > users = loadAllUsers();
return users.stream()
.filter(user -> user.getUserId().equals(userId))
.findFirst()
.orElse(null);
}

public
static
boolean
updateUser(User
updatedUser) {
List < User > users = loadAllUsers();
boolean
updated = false;

for (int i = 0; i < users.size(); i++) {
if (users.get(i).getUserId().equals(updatedUser.getUserId())) {
users.set(i, updatedUser);
updated = true;
break;
}
}

if (updated) {
rewriteUsersFile(users);
}

return updated;
}

public
static
boolean
deleteUser(String
userId) {
List < User > users = loadAllUsers();
boolean
removed = users.removeIf(user -> user.getUserId().equals(userId));

if (removed) {
rewriteUsersFile(users);
}

return removed;
}

private
static
void
rewriteUsersFile(List < User > users)
{
try (PrintWriter writer = new PrintWriter(new FileWriter(FileManager.getUsersFile()))) {
for (User user: users) {
    writer.println(user.toFileString());
}
} catch(IOException
e) {
    System.err.println("Error rewriting users file");
e.printStackTrace();
}
}

public
static
String
generateNextUserId(String
role) {
List < User > users = loadAllUsers();
String
prefix = role.equals("MANAGER") ? "MGR": "CUST";
int
maxId = 0;

for (User user: users) {
if (user.getUserId().startsWith(prefix)) {
try {
int id = Integer.parseInt(user.getUserId().substring(prefix.length()));
maxId = Math.max(maxId, id);
} catch (NumberFormatException e) {
// Ignore invalid formats
}
}
}

return prefix + String.format("%03d", maxId + 1);
}
}

// Menu
file
management


class MenuFileManager {

public static void saveMenuItem(MenuItem menuItem) {
FileManager.writeToFile(FileManager.getMenuItemsFile(), menuItem.toFileString(), true);
}

public static List < MenuItem > loadAllMenuItems() {
List < MenuItem > menuItems = new ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getMenuItemsFile());

for (String line: lines

) {
    MenuItem
item = MenuItem.fromFileString(line);
if (item != null)
{
    menuItems.add(item);
}
}
return menuItems;
}

public
static
MenuItem
findMenuItemById(String
itemId) {
List < MenuItem > items = loadAllMenuItems();
return items.stream()
.filter(item -> item.getItemId().equals(itemId))
.findFirst()
.orElse(null);
}

public
static
List < MenuItem > findMenuItemsByCategory(String
category) {
List < MenuItem > items = loadAllMenuItems();
return items.stream()
.filter(item -> item.getCategory().equalsIgnoreCase(category))
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
}

public
static
boolean
updateMenuItem(MenuItem
updatedItem) {
List < MenuItem > items = loadAllMenuItems();
boolean
updated = false;

for (int i = 0; i < items.size(); i++) {
if (items.get(i).getItemId().equals(updatedItem.getItemId())) {
items.set(i, updatedItem);
updated = true;
break;
}
}

if (updated) {
rewriteMenuFile(items);
}

return updated;
}

public
static
boolean
deleteMenuItem(String
itemId) {
List < MenuItem > items = loadAllMenuItems();
boolean
removed = items.removeIf(item -> item.getItemId().equals(itemId));

if (removed) {
rewriteMenuFile(items);
}

return removed;
}

private
static
void
rewriteMenuFile(List < MenuItem > items)
{
try (PrintWriter writer = new PrintWriter(new FileWriter(FileManager.getMenuItemsFile()))) {
for (MenuItem item: items) {
    writer.println(item.toFileString());
}
} catch(IOException
e) {
    System.err.println("Error rewriting menu file");
e.printStackTrace();
}
}

public
static
String
generateNextItemId(String
category) {
List < MenuItem > items = loadAllMenuItems();
String
prefix = category.toUpperCase().substring(0, Math.min(4, category.length()));
int
maxId = 0;

for (MenuItem item: items) {
if (item.getItemId().startsWith(prefix)) {
try {
int id = Integer.parseInt(item.getItemId().substring(prefix.length()));
maxId = Math.max(maxId, id);
} catch (NumberFormatException e) {
// Ignore invalid formats
}
}
}

return prefix + String.format("%03d", maxId + 1);
}
}

// Order
file
management


class OrderFileManager {

public static void saveOrder(Order order) {
FileManager.writeToFile(FileManager.getOrdersFile(), order.toFileString(), true);

// Save order items separately
for (OrderItem item: order.getOrderItems()

) {
    String
orderItemLine = order.getOrderId() + "," + item.toFileString();
FileManager.writeToFile(FileManager.getOrderItemsFile(), orderItemLine, true);
}
}

public
static
List < Order > loadAllOrders()
{
    List < Order > orders = new
ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getOrdersFile());

for (String line: lines)
{
    Order
order = Order.fromFileString(line);
if (order != null)
{
// Load
order
items
order.setOrderItems(loadOrderItems(order.getOrderId()));
orders.add(order);
}
}
return orders;
}

private
static
List < OrderItem > loadOrderItems(String
orderId) {
List < OrderItem > orderItems = new
ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getOrderItemsFile());

for (String line: lines) {
    String[] parts = line.split(",", 2);
if (parts.length >= 2 & & parts[0].equals(orderId)) {
OrderItem item = OrderItem.fromFileString(parts[1]);
if (item != null) {
orderItems.add(item);
}
}
}
return orderItems;
}

public
static
Order
findOrderById(String
orderId) {
List < Order > orders = loadAllOrders();
return orders.stream()
.filter(order -> order.getOrderId().equals(orderId))
.findFirst()
.orElse(null);
}

public
static
List < Order > findOrdersByCustomerId(String
customerId) {
List < Order > orders = loadAllOrders();
return orders.stream()
.filter(order -> order.getCustomerId().equals(customerId))
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
}

public
static
boolean
updateOrder(Order
updatedOrder) {
List < Order > orders = loadAllOrders();
boolean
updated = false;

for (int i = 0; i < orders.size(); i++) {
if (orders.get(i).getOrderId().equals(updatedOrder.getOrderId())) {
orders.set(i, updatedOrder);
updated = true;
break;
}
}

if (updated) {
rewriteOrderFiles(orders);
}

return updated;
}

private
static
void
rewriteOrderFiles(List < Order > orders)
{
try (PrintWriter orderWriter = new PrintWriter(new FileWriter(FileManager.getOrdersFile()));
PrintWriter itemWriter = new PrintWriter(new FileWriter(FileManager.getOrderItemsFile()))) {

for (Order order: orders) {
    orderWriter.println(order.toFileString());

for (OrderItem item: order.getOrderItems()) {
    itemWriter.println(order.getOrderId() + "," + item.toFileString());
}
}
} catch(IOException
e) {
    System.err.println("Error rewriting order files");
e.printStackTrace();
}
}

public
static
String
generateNextOrderId()
{
List < Order > orders = loadAllOrders();
String
prefix = "ORD";
int
maxId = 0;

for (Order order: orders) {
if (order.getOrderId().startsWith(prefix)) {
try {
int id = Integer.parseInt(order.getOrderId().substring(prefix.length()));
maxId = Math.max(maxId, id);
} catch (NumberFormatException e) {
// Ignore invalid formats
}
}
}

return prefix + String.format("%06d", maxId + 1);
}
}

// Payment
file
management


class PaymentFileManager {

public static void savePayment(Payment payment) {
FileManager.writeToFile(FileManager.getPaymentsFile(), payment.toFileString(), true);
}

public static List < Payment > loadAllPayments() {
List < Payment > payments = new ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getPaymentsFile());

for (String line: lines

) {
    Payment
payment = Payment.fromFileString(line);
if (payment != null)
{
    payments.add(payment);
}
}
return payments;
}

public
static
Payment
findPaymentById(String
paymentId) {
List < Payment > payments = loadAllPayments();
return payments.stream()
.filter(payment -> payment.getPaymentId().equals(paymentId))
.findFirst()
.orElse(null);
}

public
static
Payment
findPaymentByOrderId(String
orderId) {
List < Payment > payments = loadAllPayments();
return payments.stream()
.filter(payment -> payment.getOrderId().equals(orderId))
.findFirst()
.orElse(null);
}

public
static
List < Payment > findPaymentsByCustomerId(String
customerId) {
List < Payment > payments = loadAllPayments();
return payments.stream()
.filter(payment -> payment.getCustomerId().equals(customerId))
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
}

public
static
String
generateNextPaymentId()
{
List < Payment > payments = loadAllPayments();
String
prefix = "PAY";
int
maxId = 0;

for (Payment payment: payments) {
if (payment.getPaymentId().startsWith(prefix)) {
try {
int id = Integer.parseInt(payment.getPaymentId().substring(prefix.length()));
maxId = Math.max(maxId, id);
} catch (NumberFormatException e) {
// Ignore invalid formats
}
}
}

return prefix + String.format("%06d", maxId + 1);
}
}

// Feedback
file
management


class FeedbackFileManager {

public static void saveFeedback(Feedback feedback) {
FileManager.writeToFile(FileManager.getFeedbackFile(), feedback.toFileString(), true);
}

public static List < Feedback > loadAllFeedback() {
List < Feedback > feedbackList = new ArrayList <> ();
List < String > lines = FileManager.readFromFile(FileManager.getFeedbackFile());

for (String line: lines

) {
    Feedback
feedback = Feedback.fromFileString(line);
if (feedback != null)
{
    feedbackList.add(feedback);
}
}
return feedbackList;
}

public
static
List < Feedback > findFeedbackByOrderId(String
orderId) {
List < Feedback > feedbackList = loadAllFeedback();
return feedbackList.stream()
.filter(feedback -> feedback.getOrderId().equals(orderId))
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
}

public
static
List < Feedback > findFeedbackByCustomerId(String
customerId) {
List < Feedback > feedbackList = loadAllFeedback();
return feedbackList.stream()
.filter(feedback -> feedback.getCustomerId().equals(customerId))
.collect(ArrayList::new, ArrayList::add, ArrayList::addAll);
}

public
static
String
generateNextFeedbackId()
{
List < Feedback > feedbackList = loadAllFeedback();
String
prefix = "FB";
int
maxId = 0;

for (Feedback feedback: feedbackList) {
if (feedback.getFeedbackId().startsWith(prefix)) {
try {
int id = Integer.parseInt(feedback.getFeedbackId().substring(prefix.length()));
maxId = Math.max(maxId, id);
} catch (NumberFormatException e) {
// Ignore invalid formats
}
}
}

return prefix + String.format("%06d", maxId + 1);
}
}

// Input
validation
utility


class ValidationUtils {

public static boolean isValidEmail(String email) {


return email != null & & email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
}

public
static
boolean
isValidPhoneNumber(String
phoneNumber) {
return phoneNumber != null & & phoneNumber.matches("^[0-9+\\-\\s()]+$") & & phoneNumber.length() >= 10;
}

public
static
boolean
isValidPassword(String
password) {
return password != null & & password.length() >= 6;
}

public
static
boolean
isValidUserId(String
userId) {
return userId != null & & userId.matches("^[A-Z]{3,4}\\d{3,6}$");
}

public
static
boolean
isValidPrice(double
price) {
return price > 0 & & price <= 1000; // reasonable
price
range
}

public
static
boolean
isValidRating(int
rating) {
return rating >= 1 & & rating <= 5;
}

public
static
boolean
isNotEmpty(String
str) {
return str != null & & !str.trim().isEmpty();
}
}