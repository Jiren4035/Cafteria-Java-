// Core
Classes
for APU Cafeteria Ordering System

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

// Abstract
User


class demonstrating inheritance and encapsulation


public
abstract


class User {
protected String userId;
protected String username;
protected String password;
protected String email;
protected String role;
protected LocalDateTime registrationDate;
protected boolean isActive;

// Constructor
public User(String userId, String username, String password, String email, String role) {
this.userId = userId;
this.username = username;
this.password = password;
this.email = email;
this.role = role;
this.registrationDate = LocalDateTime.now();
this.isActive = true;
}

// Default constructor
public User() {}

// Getters and Setters (Encapsulation)
public String getUserId() {


return userId;}
public
void
setUserId(String
userId) {this.userId = userId;}

public
String
getUsername()
{
return username;}
public
void
setUsername(String
username) {this.username = username;}

public
String
getPassword()
{
return password;}
public
void
setPassword(String
password) {this.password = password;}

public
String
getEmail()
{
return email;}
public
void
setEmail(String
email) {this.email = email;}

public
String
getRole()
{
return role;}
public
void
setRole(String
role) {this.role = role;}

public
LocalDateTime
getRegistrationDate()
{
return registrationDate;}
public
void
setRegistrationDate(LocalDateTime
registrationDate) {this.registrationDate = registrationDate;}

public
boolean
isActive()
{
return isActive;}
public
void
setActive(boolean
active) {isActive = active;}

// Abstract
method
for polymorphism
public abstract void displayDashboard();

// Common method for authentication
public boolean authenticate(String inputPassword) {
return this.password.equals(inputPassword) & & this.isActive;
}

// Convert
to
string
for file storage
public String toFileString() {
DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
return userId + "," + username + "," + password + "," + email + "," +
role + "," + registrationDate.format(formatter) + "," + isActive;
}

// Create
user
from file string

public
static
User
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 7) {
String role = parts[4];
if ("MANAGER".equals(role)) {
Manager manager = new Manager();
manager.populateFromArray(parts);
return manager;
} else if ("CUSTOMER".equals(role)) {
Customer
customer = new
Customer();
customer.populateFromArray(parts);
return customer;
}
}
return null;
}

protected
void
populateFromArray(String[]
parts) {
this.userId = parts[0];
this.username = parts[1];
this.password = parts[2];
this.email = parts[3];
this.role = parts[4];
this.registrationDate = LocalDateTime.parse(parts[5], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
this.isActive = Boolean.parseBoolean(parts[6]);
}
}

// Manager


class extending User


class Manager extends User {
private String department;
private String managerLevel;

public Manager() {
super();
}

public Manager(String userId, String username, String password, String email,
String department, String managerLevel) {
super(userId, username, password, email, "MANAGER");
this.department = department;
this.managerLevel = managerLevel;
}

// Getters and Setters
public String getDepartment() {


return department;}
public
void
setDepartment(String
department) {this.department = department;}

public
String
getManagerLevel()
{
return managerLevel;}
public
void
setManagerLevel(String
managerLevel) {this.managerLevel = managerLevel;}

@Override


public
void
displayDashboard()
{
System.out.println("\n=== MANAGER DASHBOARD ===");
System.out.println("Welcome, " + username + " (" + managerLevel + " Manager)");
System.out.println("Department: " + department);
System.out.println("1. Manage Menu Items");
System.out.println("2. View All Orders");
System.out.println("3. Manage Customer Registration");
System.out.println("4. View Payments & Feedback");
System.out.println("5. Generate Reports");
System.out.println("6. Logout");
}

@Override


public
String
toFileString()
{
return super.toFileString() + "," + (department != null ? department: "") + "," +
(managerLevel != null ? managerLevel: "");
}

@Override


protected
void
populateFromArray(String[]
parts) {
super.populateFromArray(parts);
if (parts.length > 7) {
this.department = parts[7];
}
if (parts.length > 8) {
this.managerLevel = parts[8];
}
}
}

// Customer


class extending User


class Customer extends User {
private String phoneNumber;
private String address;
private double totalSpent;
private int loyaltyPoints;

public Customer() {
super();
}

public Customer(String userId, String username, String password, String email,
String phoneNumber, String address) {
super(userId, username, password, email, "CUSTOMER");
this.phoneNumber = phoneNumber;
this.address = address;
this.totalSpent = 0.0;
this.loyaltyPoints = 0;
}

// Getters and Setters
public String getPhoneNumber() {


return phoneNumber;}
public
void
setPhoneNumber(String
phoneNumber) {this.phoneNumber = phoneNumber;}

public
String
getAddress()
{
return address;}
public
void
setAddress(String
address) {this.address = address;}

public
double
getTotalSpent()
{
return totalSpent;}
public
void
setTotalSpent(double
totalSpent) {this.totalSpent = totalSpent;}

public
int
getLoyaltyPoints()
{
return loyaltyPoints;}
public
void
setLoyaltyPoints(int
loyaltyPoints) {this.loyaltyPoints = loyaltyPoints;}

public
void
addSpending(double
amount) {
this.totalSpent += amount;
this.loyaltyPoints += (int)(amount / 10); // 1
point
per $10
spent
}

@Override


public
void
displayDashboard()
{
System.out.println("\n=== CUSTOMER DASHBOARD ===");
System.out.println("Welcome, " + username + "!");
System.out.println("Loyalty Points: " + loyaltyPoints);
System.out.println("Total Spent: $" + String.format("%.2f", totalSpent));
System.out.println("1. View Menu");
System.out.println("2. Create New Order");
System.out.println("3. View My Orders");
System.out.println("4. Make Payment");
System.out.println("5. Provide Feedback");
System.out.println("6. Update Profile");
System.out.println("7. Logout");
}

@Override


public
String
toFileString()
{
return super.toFileString() + "," + (phoneNumber != null ? phoneNumber: "") + "," +
(address != null ? address: "") + "," + totalSpent + "," + loyaltyPoints;
}

@Override


protected
void
populateFromArray(String[]
parts) {
super.populateFromArray(parts);
if (parts.length > 7) {
this.phoneNumber = parts[7];
}
if (parts.length > 8) {
this.address = parts[8];
}
if (parts.length > 9) {
this.totalSpent = Double.parseDouble(parts[9]);
}
if (parts.length > 10) {
this.loyaltyPoints = Integer.parseInt(parts[10]);
}
}
}

// MenuItem


class
    class MenuItem {
    private String itemId;
    private String itemName;
    private String category;
    private double price;
    private String description;
    private boolean isAvailable;
    private int preparationTime; // in minutes

    public MenuItem() {}

    public MenuItem(String itemId, String itemName, String category, double price,
    String description, int preparationTime) {
    this.itemId = itemId;
    this.itemName = itemName;
    this.category = category;
    this.price = price;
    this.description = description;
    this.preparationTime = preparationTime;
    this.isAvailable = true;
    }

    // Getters and Setters
    public String getItemId() {

    return itemId;}
    public
    void
    setItemId(String
    itemId) {this.itemId = itemId;}

    public
    String
    getItemName()
    {
    return itemName;}
    public
    void
    setItemName(String
    itemName) {this.itemName = itemName;}

    public
    String
    getCategory()
    {
    return category;}
    public
    void
    setCategory(String
    category) {this.category = category;}

    public
    double
    getPrice()
    {
    return price;}
    public
    void
    setPrice(double
    price) {this.price = price;}

    public
    String
    getDescription()
    {
    return description;}
    public
    void
    setDescription(String
    description) {this.description = description;}

    public
    boolean
    isAvailable()
    {
    return isAvailable;}
    public
    void
    setAvailable(boolean
    available) {isAvailable = available;}

    public
    int
    getPreparationTime()
    {
    return preparationTime;}
    public
    void
    setPreparationTime(int
    preparationTime) {this.preparationTime = preparationTime;}

    public
    String
    toFileString()
    {


return itemId + "," + itemName + "," + category + "," + price + "," +
description + "," + isAvailable + "," + preparationTime;
}

public
static
MenuItem
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 7) {
MenuItem item = new MenuItem();
item.itemId = parts[0];
item.itemName = parts[1];
item.category = parts[2];
item.price = Double.parseDouble(parts[3]);
item.description = parts[4];
item.isAvailable = Boolean.parseBoolean(parts[5]);
item.preparationTime = Integer.parseInt(parts[6]);
return item;
}
return null;
}

@Override


public
String
toString()
{
return String.format("%-10s %-20s %-15s $%-8.2f %-30s %d min",
                     itemId, itemName, category, price, description, preparationTime);
}
}

// OrderItem


class
    class OrderItem {
    private String itemId;
    private String itemName;
    private int quantity;
    private double unitPrice;
    private double totalPrice;
    private String specialInstructions;

    public OrderItem() {}

    public OrderItem(String itemId, String itemName, int quantity, double unitPrice) {
    this.itemId = itemId;
    this.itemName = itemName;
    this.quantity = quantity;
    this.unitPrice = unitPrice;
    this.totalPrice = quantity * unitPrice;
    this.specialInstructions = "";
    }

    // Getters and Setters
    public String getItemId() {

    return itemId;}
    public
    void
    setItemId(String
    itemId) {this.itemId = itemId;}

    public
    String
    getItemName()
    {
    return itemName;}
    public
    void
    setItemName(String
    itemName) {this.itemName = itemName;}

    public
    int
    getQuantity()
    {
    return quantity;}
    public
    void
    setQuantity(int
    quantity) {


this.quantity = quantity;
this.totalPrice = quantity * unitPrice;
}

public
double
getUnitPrice()
{
return unitPrice;}
public
void
setUnitPrice(double
unitPrice) {
this.unitPrice = unitPrice;
this.totalPrice = quantity * unitPrice;
}

public
double
getTotalPrice()
{
return totalPrice;}

public
String
getSpecialInstructions()
{
return specialInstructions;}
public
void
setSpecialInstructions(String
specialInstructions) {
this.specialInstructions = specialInstructions;
}

public
String
toFileString()
{
return itemId + "," + itemName + "," + quantity + "," + unitPrice + "," +
totalPrice + "," + (specialInstructions != null ? specialInstructions: "");
}

public
static
OrderItem
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 5) {
OrderItem item = new OrderItem();
item.itemId = parts[0];
item.itemName = parts[1];
item.quantity = Integer.parseInt(parts[2]);
item.unitPrice = Double.parseDouble(parts[3]);
item.totalPrice = Double.parseDouble(parts[4]);
if (parts.length > 5) {
item.specialInstructions = parts[5];
}
return item;
}
return null;
}
}

// Order


class
    class Order {
    private String orderId;
    private String customerId;
    private String customerName;
    private LocalDateTime orderDate;
    private List < OrderItem > orderItems;
    private double totalAmount;
    private String orderStatus; // PENDING, CONFIRMED, PREPARING, READY, COMPLETED, CANCELLED
    private String paymentStatus; // UNPAID, PAID, REFUNDED
    private LocalDateTime estimatedPickupTime;
    private String specialNotes;

    public Order() {
    this.orderItems = new ArrayList <> ();
    this.orderDate = LocalDateTime.now();
    this.orderStatus = "PENDING";
    this.paymentStatus = "UNPAID";
    }

    public Order(String orderId, String customerId, String customerName) {
    this();
    this.orderId = orderId;
    this.customerId = customerId;
    this.customerName = customerName;
    }

    // Getters and Setters
    public String getOrderId() {

    return orderId;}
    public
    void
    setOrderId(String
    orderId) {this.orderId = orderId;}

    public
    String
    getCustomerId()
    {
    return customerId;}
    public
    void
    setCustomerId(String
    customerId) {this.customerId = customerId;}

    public
    String
    getCustomerName()
    {
    return customerName;}
    public
    void
    setCustomerName(String
    customerName) {this.customerName = customerName;}

    public
    LocalDateTime
    getOrderDate()
    {
    return orderDate;}
    public
    void
    setOrderDate(LocalDateTime
    orderDate) {this.orderDate = orderDate;}

    public
    List < OrderItem > getOrderItems()
    {
    return orderItems;}
    public
    void
    setOrderItems(List < OrderItem > orderItems)
    {


this.orderItems = orderItems;
calculateTotalAmount();
}

public
double
getTotalAmount()
{
return totalAmount;}

public
String
getOrderStatus()
{
return orderStatus;}
public
void
setOrderStatus(String
orderStatus) {this.orderStatus = orderStatus;}

public
String
getPaymentStatus()
{
return paymentStatus;}
public
void
setPaymentStatus(String
paymentStatus) {this.paymentStatus = paymentStatus;}

public
LocalDateTime
getEstimatedPickupTime()
{
return estimatedPickupTime;}
public
void
setEstimatedPickupTime(LocalDateTime
estimatedPickupTime) {
this.estimatedPickupTime = estimatedPickupTime;
}

public
String
getSpecialNotes()
{
return specialNotes;}
public
void
setSpecialNotes(String
specialNotes) {this.specialNotes = specialNotes;}

// Methods
public
void
addOrderItem(OrderItem
item) {
orderItems.add(item);
calculateTotalAmount();
}

public
void
removeOrderItem(String
itemId) {
orderItems.removeIf(item -> item.getItemId().equals(itemId));
calculateTotalAmount();
}

private
void
calculateTotalAmount()
{
totalAmount = orderItems.stream()
.mapToDouble(OrderItem::getTotalPrice)
.sum();
}

public
String
toFileString()
{
DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
StringBuilder
sb = new
StringBuilder();
sb.append(orderId).append(",")
.append(customerId).append(",")
.append(customerName).append(",")
.append(orderDate.format(formatter)).append(",")
.append(totalAmount).append(",")
.append(orderStatus).append(",")
.append(paymentStatus).append(",");

if (estimatedPickupTime != null) {
sb.append(estimatedPickupTime.format(formatter));
}
sb.append(",").append(specialNotes != null ? specialNotes: "");

return sb.toString();
}

public
static
Order
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 7) {
Order order = new Order();
order.orderId = parts[0];
order.customerId = parts[1];
order.customerName = parts[2];
order.orderDate = LocalDateTime.parse(parts[3], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
order.totalAmount = Double.parseDouble(parts[4]);
order.orderStatus = parts[5];
order.paymentStatus = parts[6];

if (parts.length > 7 & & !parts[7].isEmpty()) {
order.estimatedPickupTime = LocalDateTime.parse(parts[7], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
}
if (parts.length > 8) {
order.specialNotes = parts[8];
}

return order;
}
return null;
}
}

// Payment


class
    class Payment {
    private String paymentId;
    private String orderId;
    private String customerId;
    private double amount;
    private String paymentMethod; // CASH, CARD, DIGITAL_WALLET
    private LocalDateTime paymentDate;
    private String paymentStatus; // SUCCESS, FAILED, PENDING, REFUNDED
    private String transactionReference;

    public Payment() {
    this.paymentDate = LocalDateTime.now();
    this.paymentStatus = "PENDING";
    }

    public Payment(String paymentId, String orderId, String customerId, double amount, String paymentMethod) {
    this();
    this.paymentId = paymentId;
    this.orderId = orderId;
    this.customerId = customerId;
    this.amount = amount;
    this.paymentMethod = paymentMethod;
    }

    // Getters and Setters
    public String getPaymentId() {

    return paymentId;}
    public
    void
    setPaymentId(String
    paymentId) {this.paymentId = paymentId;}

    public
    String
    getOrderId()
    {
    return orderId;}
    public
    void
    setOrderId(String
    orderId) {this.orderId = orderId;}

    public
    String
    getCustomerId()
    {
    return customerId;}
    public
    void
    setCustomerId(String
    customerId) {this.customerId = customerId;}

    public
    double
    getAmount()
    {
    return amount;}
    public
    void
    setAmount(double
    amount) {this.amount = amount;}

    public
    String
    getPaymentMethod()
    {
    return paymentMethod;}
    public
    void
    setPaymentMethod(String
    paymentMethod) {this.paymentMethod = paymentMethod;}

    public
    LocalDateTime
    getPaymentDate()
    {
    return paymentDate;}
    public
    void
    setPaymentDate(LocalDateTime
    paymentDate) {this.paymentDate = paymentDate;}

    public
    String
    getPaymentStatus()
    {
    return paymentStatus;}
    public
    void
    setPaymentStatus(String
    paymentStatus) {this.paymentStatus = paymentStatus;}

    public
    String
    getTransactionReference()
    {
    return transactionReference;}
    public
    void
    setTransactionReference(String
    transactionReference) {


this.transactionReference = transactionReference;
}

public
String
toFileString()
{
DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
return paymentId + "," + orderId + "," + customerId + "," + amount + "," +
paymentMethod + "," + paymentDate.format(formatter) + "," + paymentStatus + "," +
(transactionReference != null ? transactionReference: "");
}

public
static
Payment
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 7) {
Payment payment = new Payment();
payment.paymentId = parts[0];
payment.orderId = parts[1];
payment.customerId = parts[2];
payment.amount = Double.parseDouble(parts[3]);
payment.paymentMethod = parts[4];
payment.paymentDate = LocalDateTime.parse(parts[5], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
payment.paymentStatus = parts[6];
if (parts.length > 7) {
payment.transactionReference = parts[7];
}
return payment;
}
return null;
}
}

// Feedback


class
    class Feedback {
    private String feedbackId;
    private String orderId;
    private String customerId;
    private String customerName;
    private int rating; // 1-5 stars
    private String comments;
    private String category; // FOOD_QUALITY, SERVICE, DELIVERY_TIME, OVERALL
    private LocalDateTime feedbackDate;
    private boolean isAnonymous;

    public Feedback() {
    this.feedbackDate = LocalDateTime.now();
    this.isAnonymous = false;
    }

    public Feedback(String feedbackId, String orderId, String customerId, String customerName) {
    this();
    this.feedbackId = feedbackId;
    this.orderId = orderId;
    this.customerId = customerId;
    this.customerName = customerName;
    }

    // Getters and Setters
    public String getFeedbackId() {

    return feedbackId;}
    public
    void
    setFeedbackId(String
    feedbackId) {this.feedbackId = feedbackId;}

    public
    String
    getOrderId()
    {
    return orderId;}
    public
    void
    setOrderId(String
    orderId) {this.orderId = orderId;}

    public
    String
    getCustomerId()
    {
    return customerId;}
    public
    void
    setCustomerId(String
    customerId) {this.customerId = customerId;}

    public
    String
    getCustomerName()
    {
    return customerName;}
    public
    void
    setCustomerName(String
    customerName) {this.customerName = customerName;}

    public
    int
    getRating()
    {
    return rating;}
    public
    void
    setRating(int
    rating) {this.rating = rating;}

    public
    String
    getComments()
    {
    return comments;}
    public
    void
    setComments(String
    comments) {this.comments = comments;}

    public
    String
    getCategory()
    {
    return category;}
    public
    void
    setCategory(String
    category) {this.category = category;}

    public
    LocalDateTime
    getFeedbackDate()
    {
    return feedbackDate;}
    public
    void
    setFeedbackDate(LocalDateTime
    feedbackDate) {this.feedbackDate = feedbackDate;}

    public
    boolean
    isAnonymous()
    {
    return isAnonymous;}
    public
    void
    setAnonymous(boolean
    anonymous) {isAnonymous = anonymous;}

    public
    String
    toFileString()
    {


DateTimeFormatter
formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
return feedbackId + "," + orderId + "," + customerId + "," +
(isAnonymous ? "Anonymous": customerName) + "," + rating + "," +
(comments != null ? comments: "") + "," + category + "," +
feedbackDate.format(formatter) + "," + isAnonymous;
}

public
static
Feedback
fromFileString(String
line) {
String[]
parts = line.split(",");
if (parts.length >= 8) {
Feedback feedback = new Feedback();
feedback.feedbackId = parts[0];
feedback.orderId = parts[1];
feedback.customerId = parts[2];
feedback.customerName = parts[3];
feedback.rating = Integer.parseInt(parts[4]);
feedback.comments = parts[5];
feedback.category = parts[6];
feedback.feedbackDate = LocalDateTime.parse(parts[7], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
if (parts.length > 8) {
feedback.isAnonymous = Boolean.parseBoolean(parts[8]);
}
return feedback;
}
return null;
}
}