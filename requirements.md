## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. Add to cart
6. *Add pictures for items
7. Find item
8. Sort by price
9. Add item to seller store
10. Buy item
11. Remove item from cart
12. User Profile

## Non-functional Requirements

1. non-functional
2. non-functional
3. non-functional
4. non-functional

## Use Cases

1. Find item
- **Pre-condition:**
	The user typed the name of an item in the seatch bar.

- **Trigger:** 
	The user clicked enter or text box with keyword 'search'.

- **Primary Sequence:**
  
  1. User clicks in the textbox.
  2. User searches by name for an item they want.
  3. User clicks on search or clicks enter on the keyboard.

- **Primary Postconditions:**
	The item the user searches up shows up or the item doesn't show up and displays a message for the user.

- **Alternate Sequence:**
  
  1. User searches for something that is not in stock or misspelled item
	a. Displays a message that there is no available item or the item was misspelled


2. Remove item from cart
- **Pre-condition:**
        In the cart menu, the user can remove items that were added to the cart.

- **Trigger:**
        In the cart menu, the user can click remove on the item.

- **Primary Sequence:**

  1. Click on cart.
  2. Brings user to cart menu where there's a list of items the user added to cart.
  3. Next to each item, there is a remove option.
  4. The user can click remove to remove the item from the cart.

- **Primary Postconditions:**                                     
        After the user clicks remove, the item disappears from the cart menu.

- **Alternate Sequence:**
  
  1. If there is no items in the cart.
	a. Displays a message 'No items in cart'
	b. No items mean no remove option.


3. Add to cart
- **Pre-condition:**
        After the user searches for an item and there is an available item, the user can add the item to their cart.

- **Trigger:**
        The user can click on add after finding an item.

- **Primary Sequence:**

  1. User clicks add next to the item.
  2. The item will appear in the cart.

- **Primary Postconditions:**                                     
        The user adds the item into the cart, and the item appears in the cart menu. If item becomes unavailable, the item is not added to cart.

- **Alternate Sequence:**
  
  1. If the item suddenly becomes out-of-stock (someone bought it just now) and user clicks add.
	a. Displays a message 'Item is not available, please refresh the page'. 


4. User Profile
- **Pre-condition:**
        

- **Trigger:**
        

- **Primary Sequence:**

  1. 
  2. 
  3. 

- **Primary Postconditions:**                                     
        

- **Alternate Sequence:**
  
  1. 


5. Sort by price
- **Pre-condition:**
        After searching for an available item, there will be an option to sort by price.

- **Trigger:**
        The user clicks 'sort-by-price'.

- **Primary Sequence:**

  1. User searches for an available item.
  2. Items appear first by recency.
  3. User clicks sort-by-price.
  4. Items get sorted from least to greatest.
  5. User clicks sort-by-price again.
  6. Items are now sorted from greatest to least.

- **Primary Postconditions:**                                     
        After clicking sort-by-price, the items will be sorted from least to most expensive and will alternate if clicked on again.

- **Alternate Sequence:**
  
  1. If there is only one item, sort-by-price will do nothing.


6. Add item to seller store
- **Pre-condition:**
        After login, the user goes to their profile page.

- **Trigger:**
        The user can click on sell-item on their profile page.

- **Primary Sequence:**

  1. After clicking sell-item, the user is asked to type the name of the item.
  2. Add quantity of item.
  3. Then the user is asked to enter a price for the item.
  4. Next, upload a picture of the item.
  5. Finally, click post to post the item on display.

- **Primary Postconditions:**                                     
        The item is displayed onto the marketplace or the item is not displayed.

- **Alternate Sequence:**
  
  1. 
