## Functional Requirements

1. Login - Bhagyesh
2. Logout - Bhagyesh
3. Create new account - Bhagyesh
4. Delete account - Tejas
5. Add to cart - Tejas
6. *Add pictures for item - winson
7. Find item - Tejas
8. Change account password - Tejas
9. Add item to seller store - Bhagyesh
10. Buy item - Bhagyesh
11. Remove item from cart - Tejas
12. User Profile - Winson



## Non-functional Requirements

1. *UI interactive interface
2. Usability - Easy to use basic marketplace website
3. Mobile Responsive webpage - website adjusts itself according to the size of the window.
4. Compatibility - works on all kinds of devices which can support chrome.



## Use Cases

1. Login
2. Logout
3. Create New Account
4. Delete Account


5. Find item

- **Summary:**
  1. This featture allows user to find the product by it's name.

- **Pre-condition:**
  1. The user is on the market page 

- **Trigger:** 
  1. The user entered the name of product in search bar and clicked 'search'.

- **Primary Sequence:**
  
  1. User clicks in the search bar.
  2. User searches by name for the product they want.
  3. User clicks on search or clicks enter on the keyboard to initiate the search for the product.

- **Primary Postconditions:**
  1. All the products are shown that match the name of the product user typed in search bar.

- **Alternate Sequence:**
  
  1. User searches for something that is not in stock or misspelled item
	a. Displays a message that there is no available item or the item was misspelled




6. Remove item from cart
- **Pre-condition:**
  1. User should be logged in and on cart page, cart must have at least one product in it.

- **Summary:**
  1. This feature allows user to remove a product from their cart.

- **Trigger:**
  1. The user clicks 'remove from cart' button for the product they want to remove.

- **Primary Sequence:**

  1. User clicks on the 'remove form cart' button for the product they want to remove.
  2. User recieves a flash message saying product have been succesfully removed form the cart.
  3. The product is removed form the users cart database.
  4. The product is not visible on the cart page.

- **Primary Postconditions:**                                     
  1. The product is removed form the users cart database and is not visible on the cart page anymore.





7. Add to cart
- **Pre-condition:**
  1. User should be logged in and on market page.

- **Summary:**
  1. This feature allows user to add products to their cart.

- **Trigger:**
  1. The user finds product they want to buy and clicks add to cart button to the right of the product.

- **Primary Sequence:**

  1. User clicks 'add to cart' button next to the product he wants to buy.
  2. User gets flash message saying product has successfully been added to the cart.
  3. Server recieves the request to add product to the current logged in users cart.
  4. The product is added to the current users cart on the database.
  5. User can see the product on their cart page.

- **Primary Postconditions:**                                     
  1. Server recieves the request to add product to the current logged in users cart.
  2. The product is added to the current users cart on the database.
  3. User can see the product on their cart page.

- **Alternate Sequence:**
  
  1. If the item suddenly becomes out-of-stock (someone bought it just now) and user clicks add.
	a. User gets a flash message 'Item is not available, please refresh the page'. 
	
 




8. User Profile
- **Pre-condition:**
  1. User should already have an account, should be logged into the account.

- **Summary:**
  1. This feature allows user to see his profile and make changes like delete account and change password.

- **Trigger:**
  1. User clicks on my profile button.  

- **Primary Sequence:**

  1. User logs into their account.
  2. User clicks on my profile button.

- **Primary Postconditions:**                                     
  1. User gets navigated to page where he can see his profile information as well as delete account and change password option.

- **Alternate Sequence:**
  
  1. User clicks on 'my profile' button but doesn't yet have a profile.
    a. User is then routed to sign up page.



9. Change account password
- **Pre-condition:**
  1. User must be logged in and on their profile page.

- **Summary:**
  1. This feature allows user to change their account password. 

- **Trigger:**
  1. The user clicks 'change password' button on profile page.

- **Primary Sequence:**

  1. The user clicks 'change password' button on profile page.
  2. Prompt is popped up for user to type old and new password. 
  3. User types current and new password and clicks submit. 
  4. User receives a flash message saying that his password has been changed.
  6. The server recieves the change password request. 
  7. The password is changed on the database for the current logged in user.

- **Primary Postconditions:**                                     
  1. User types current and new password and clicking submit.
  2. The server recieves the change password request. 
  3. The password is changed on the database for the current logged in user. 
  4. User sees a flash message that their password has been changed.

- **Alternate Sequence:**
  1. User inputs incorrect current password.
     a. User sees a flash message saying the old password is incorrect.
  2. User inputs invalid password.
     a. User is prompted to type valid password.




10. Add item to the market
- **Pre-condition:**
  1. User should be logged in.

- **Summary:**
  1. User can add products to the market to sell. 

- **Trigger:**
  1. User clicks on 'sell product' button.

- **Primary Sequence:**

  1. User logs into their account.
  2. User clicks 'sell product'.
  3. User fills the name, price, description of the product.
  4. User clicks submit.
  5. Server recieves the information and stores it in database.
  6. User is redirected to the market page.
  7. The product user entered is visible on market to buy.

- **Primary Postconditions:**                                     
  1. The product is stored on database and visible on market page for users to buy.

- **Alternate Sequence:**
  
  1. User logs into their account.
  2. User clicks 'sell product'.
  3. User keeps the form incomplete (doen't provide name/image/description etc) / does not input enough information
  4. User clicks submit.
  5. Error message is recieved on server side.
  6. User sees a flash message with error.
  7. User is prompted to enter all the required fields.
