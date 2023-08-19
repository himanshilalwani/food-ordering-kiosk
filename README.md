# House of Doughnuts Restaurant Management System

Welcome to <b>House of Doughnuts</b> Restaurant Management System, a project built using Python's Tkinter GUI package. This system enables seamless menu viewing, order placement, bill generation, and membership registration for customers. Additionally, it empowers managers with password-protected functionalities to manage the restaurant's offerings efficiently.

## Features
* <b>User Interface: </b> The application leverages Tkinter for an intuitive and visually appealing interface for both customers and managers.
* <b>Menu Exploration: </b> Customers can conveniently explore the enticing menu of House of Doughnuts, reviewing prices before making their selections.
* <b>Effortless Order Placement and Bill Generation: </b> Customers can build their orders by adding desired items and specifying quantities. The system can calculate comprehensive bills, providing customers with accurate cost breakdowns.
* <b>Membership Perks: </b> Customers have the option to register as members, granting them access to special offers.
* <b>Managerial Privileges: </b>  Managers possess password-protected access to critical functionalities:
  *  <b>New Item Creation: </b> Managers can effortlessly introduce new items, which immediately appear on the menu for customer perusal.
  *  <b>Item Details Modification: </b>Managers can update item names and rates to reflect any alterations accurately.
  *  <b>Item Deletion: </b> Managers hold the authority to eliminate items that are no longer available.
* <b>Database Integration: </b> The system utilizes mySQL-connector-python for seamless interaction with the database. The following tables are utilized:
  * <b>ItemsMaster: </b> Stores menu item information, including item number, name, and rate.
  * <b>Bill: </b>Manages bill details, including bill number, date, customer name, description, and total.
  * <b>MemberDetails: </b> Maintains member information, including first name, last name, mobile number (primary key), and address.

## Instructions
* Open a terminal or command prompt.
* Navigate to the src directory.
* Run the code by executing the following command: `python3 MainMenu.py`

## Project Structure
The project is organized into the following files, each contributing to specific functionalities of the application:
* MainMenu.py: This module contains the main menu class, responsible for initializing the application and presenting the user with the main options to either display the menu, place an order, register as a member, or access manager functions.
* ShowMenu.py: This module is responsible for displaying the menu to customers. It provides information about menu items, including their names and rates.
* OrderFood.py: The order food modules handles the order placement process. Customers can select items, specify quantities, and proceed to checkout.
* Manager.py: The manager modules provides password-protected access to managerial functionalities. Managers can add new menu items, modify existing items, and remove items from the menu.
* Register.py: The registration modules allows customers to become members by providing their details.

## Dependencies
The code relies on the following dependencies:
* Tkinter
* mysql-connector-python
* Pandas
* Pillow
  
## Screenshots
Images used are not mine.

<img width="523" alt="Screenshot 2021-08-22 at 6 08 36 PM" src="https://user-images.githubusercontent.com/81231340/130355619-0dcf6b01-4694-4f86-b60f-153a5d65d74c.png">
<img width="524" alt="Screenshot 2021-08-22 at 6 08 46 PM" src="https://user-images.githubusercontent.com/81231340/130355628-0bde7763-4f7f-4e83-9477-1be47c1097a4.png">
<img width="526" alt="Screenshot 2021-08-22 at 6 08 59 PM" src="https://user-images.githubusercontent.com/81231340/130355630-4dcf4ecb-6c70-463f-8980-fb8b6c67d508.png">
<img width="529" alt="Screenshot 2021-08-22 at 6 09 21 PM" src="https://user-images.githubusercontent.com/81231340/130355631-5e5371fa-8390-423d-a008-75cd469eb268.png">
<img width="537" alt="Screenshot 2021-08-22 at 6 09 31 PM" src="https://user-images.githubusercontent.com/81231340/130355633-90d23eb6-39fb-4a2e-a957-ee1f7f79c5f8.png">
<img width="529" alt="Screenshot 2021-08-22 at 6 09 41 PM" src="https://user-images.githubusercontent.com/81231340/130355646-be66a435-b58b-439a-b8f4-141dfa07e773.png">
<img width="581" alt="Screenshot 2021-08-22 at 6 09 50 PM" src="https://user-images.githubusercontent.com/81231340/130355647-3718c8aa-1e28-4358-9965-a5cb83d2f170.png">
<img width="524" alt="Screenshot 2021-08-22 at 6 10 02 PM" src="https://user-images.githubusercontent.com/81231340/130355648-4b02ad5d-91e8-4667-bd12-5a62d1e8b5a0.png">
<img width="769" alt="Screenshot 2021-08-22 at 6 10 11 PM" src="https://user-images.githubusercontent.com/81231340/130355649-01b9f0aa-9899-4776-9666-e43d16ea3d14.png">
