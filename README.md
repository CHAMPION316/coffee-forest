# Coffee Forrest &#9749;

A coffee website where you can order luxury coffee from all over South America and Africa. 

# Table of contents

- [Background](#background)
- [Mission Statement](#mission-statement)
- [Target Audience](#target-audience)
- [Stakeholder Interviews](#stakeholder-interviews)
- [Marketing](#marketing)
- [Structure](#structure)
- [Testing](#4-testing)
- [Improvements](#5-improvements)
- [Deployment](#6-deployment)
- [Credits](#7-credits)

# Background 

Coffee Forest is a fictional website that sales expensive coffee from all over the continents of South America and Africa. This coffee goes through a (rigorous process) in order to be made. The process of course is fictional 😂 as you will find out in their descriptions but resembles some authenticity to how the real life process is somehwat created. For the sake of fiction people are highly interested in this kind of coffee and how it tastes. 

# Mission Statement

To create an e-commerce application that will enable Coffee Forest to increase their customer base for their high-end online business. 

# Target Audience

The customers that use Coffee Forest are mostly those that love to drink coffee and want to expand their taste of coffee from the flavors they already know. The audience in this case are a small target willing to pay a premium in order to receive the best tasting coffee the market has to offer anywhere in the world.

# Stakeholder Interviews

## User Persona
Interviews were carried out with the owners of Coffee Forest, customers that already use the current service and customers who visited the website who were curious about the product. 

Ages between 18-23 were less likely to use the service but a growth among college graduates starting at 24-30 who found jobs upon graduation has given us an inline in purchases. What this is saying is that we are touching base with the younger crowd who have already grown a like for coffee and want to explore upon what more there is out there when it comes to purity and taste. 

&nbsp;

| Name | Age | Uses the Service | Coffee Ordered per Month
| -- | -- | -- | --
| Elon Musk | 50 | Owner | N/A
| Royer Segura | 33 | Owner | N/A
| Hideo Kojima | 58 | Yes | 4
| Phil Spencer | 73 | Yes | 6
| Benny Benassi | 54 | Yes | 3
| Zack Snyder | 56 | Yes | 3
| Devante Adams | 29 | No | N/A
| Hunter Renfrow | 26 | No | N/A
| Travon Walker | 21 | No | N/A
| Din Djarin | 27 | No | N/A

&nbsp;

## User Goals
From the resulting interviews, the user goals have been defined:

1. Create, update and delete coffee selection
1. Create orders and secure purchases
1. Select product by price/category
1. Login and out functionality
1. View company contact details
1. Search through products
1. Reset shopping cart 

&nbsp;

## User Stories

| ID | User Category | User wants to... | So they can... |
|--|--|--|--|
| 01 | Store Owner | Add products | Add new items to the store
| 02 | Store Owner | Edit and update a product | Change the price or any details of a product
| 03 | Store Owner | Delete products | Remove them from the store
| 04 | Store Owner | View all purchases | See the customers details after making a purchase
| 05 | Store Owner | See the number of open orders | Plan their schedule and staff numbers
| 06 | Shopper | View a list of all the products | Choose products to purchase
| 07 | Shopper | See individual product details | Have a detailed explanation of the product
| 08 | Shopper | Have contact information available | Make contact with the store if there is a problem
| 09 | Shopper | Easily select coffee for purchase | Keep shopping time fluid 
| 10 | Shopper | See the items selected for purchase | Keep track of my selections
| 11 | Shopper | See a running total of shopping basket | Keep track of their spending
| 12 | Shopper | Select multiple quantities of the same product | Order two of the same product
| 13 | Shopper | Filter the products | Narrow down the products to the ones wanted
| 14 | Shopper | See the number of search results | See the number of results of the search
| 15 | Site User | Easily register for an account | view an individual profile
| 16 | Site User | Easily login and logout | Access personal information
| 17 | Site User | Recover a password if required | Recover access to their account if required
| 18 | Site User | Have payment information saved | Speed up use for regular customers

&nbsp;

## Requirements and Expectations

| Requirement | Expectation
| -- | --
| Visually appealing and well laid out | Colours to be complimentary, text to be clear. Navigation to be logical and simple
| Responsive design (Mobile first) | The screen size to not affect the look of the application 
| Secure payment method | Card details to be secure
| CRUD functionality for products | Easily maintain the store's products
| Search and filter products | Easily refine the product to the user's needs

&nbsp;

## Strategy
### Strategy Outline
The items are graded in a 0 - 5 system in both importance and feasibility as per the grading system below.

&nbsp;

| | Score - 0 | Score - 3 | Score - 5 |
|--|--|--| -- |
| Importance | Unwise use of time to address | Efforts should be made to accommodate these | Efforts MUST be made to address these
| Feasibility | Unwise use of time to address| Efforts should be made to accommodate these | Efforts MUST be made to address these

&nbsp;

The outcome is calculated by combining the scores from the *Importance* and *Feasibility* ratings. This then gives a final strategy rating of what items and where to focus on.

| | Score - 0 | Score - 5 | Score - 10 |
|--|--|--| -- |
| Item Description | Not viable | Efforts should be made | Efforts MUST be made

&nbsp;

### Strategy Description

| User story ID | Importance Score | Feasibility Score | Outcome |
| --------------- | ----------| -----------| ---------- |
| 1 | 5 | 5 | 10 |
| 2 | 5 | 5 | 10 |
| 3 | 5 | 5 | 10 |
| 4 | 5 | 2 | 7 |
| 5 | 3 | 3 | 6 |
| 6 | 5 | 5 | 10 |
| 7 | 5 | 5 | 10 |
| 8 | 5 | 5 | 10 |
| 9 | 5 | 5 | 10 |
| 10 | 5 | 5 | 10 |
| 11 | 5 | 5 | 10 |
| 12 | 5 | 5 | 10 |
| 13 | 5 | 5 | 10 |
| 14 | 5 | 5 | 10 |
| 15 | 5 | 5 | 10 |
| 16 | 5 | 5 | 10 |
| 17 | 5 | 5 | 10 |
| 18 | 5 | 5 | 10 |


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Marketing

At the time of this writing social media pages will be created in order to push the marketing of the website. 
These social platforms include: 
* **Twitter**
* **Facebook**
* **Instagram**

# Wireframes
[Home Page](docs/wireframes/Main_Pages.png)

[Product List](docs/wireframes/Product__Pages.png)

[Single Product](docs/wireframes/Single_Product_Page.png)

[Dropdown List](docs/wireframes/Dropdown_Pages.png)

[Register Page](docs/wireframes/Register_Pages.png)

[Signin Page](docs/wireframes/Signin_page.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Design Choices

### Fonts

* Content - Standard **Sans serif**
* Headings - [Josefin](https://fonts.google.com/specimen/Josefin+Sans?query=josefin "Josefin")

### Colours

One of the main colours I wanted to have on my page was white considering how popular it is among many websites. From there I want colours that make people feel good when visiting a page.

The final decision was the following.

&nbsp;
![Colour Palette](docs/designs/the-coffee-colors.png)

&nbsp;

The colours will be used as described in the table below

| Hex Value | Root variable name |
| -- | -- |
| #FFFFFF | white |
| #C1D1C1 | light-green |
| #DEE0DD | light-grey |

&nbsp;

# Structure
## App Flow

### Guest User

![Guest User](docs/structure/guest-user-flow.png)

\
&nbsp;

### Authenticated User

![Authenticated User](docs/structure/authenticated-user-flow.png)

\
&nbsp;

### Admin

![Admin User](docs/structure/admin-user-flow.png)

## Data Schema

### Products

![Products Data Schema](docs/structure/product-chart.jpg)

\
&nbsp;

### Orders
![Orders Data Schema](docs/structure/order-chart.jpg)

## Models

### Category

| Name | Key | Type | Other Details
| -- | -- | -- | --
| name || CharField | max_length=254
| friendly_name || CharField | max_length=254

\
&nbsp;

### Product

| Name | Key | Type | Other Details
| -- | -- | -- | --
| category | FK (Category) || null=True, blank=True, on_delete=models.SET_NULL
| sku || CharField | max_length=254, null=True, blank=True
| name || CharField | max_length=254
| description || TextField |
| gram_sizes || Boolean | default=False, null=True, blank=True
| price || DecimalField | max_digits=6, decimal_places=2
| rating || DecimalField | max_digits=6, decimal_places=2, null=True, blank=True
| image_url || URLField | max_length=1024, null=True, blank=True
| image || ImageField | null=True, blank=True

\
&nbsp;

### Order

| Name | Key | Type | Other Details
| -- | -- | -- | --
| order_number || CharField | max_length=32, null=False, editable=False
| full_name || CharField | max_length=50, null=False, blank=False
| email | Key | Charfield | max_length=100, null=False, blank=False
| phone_number || CharField | max_length=10, null=False, blank=False
| country || CharField | max_length=40, null=False, blank=False
| postcode | Key | Charfield | max_length=10, null=True, blank=True
| town_or_city || CharField | max_length=32, null=False, blank=False
| street_address || CharField | max_length=100, null=False, blank=False
| county | Key | Charfield | max_length=80, null=True, blank=True
| date || DateTimeField | auto_now_add=True
| delivery_cost || DecimalField | max_digits=6, decimal_places=2, null=False, default=0
| orde_total | Key | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
| grand_total || DecimalField | max_digits=10, decimal_places=2, null=False, default=0

\
&nbsp;

### OrderLineItemgit

| Name | Key | Type | Other Details
| -- | -- | -- | --
| order | FK (Order) | | 
| product | FK (Product) | CharField | max_length=254, unique=True
| product_size | | SlugField | max_length=254, unique=True
| quantity |  |  CloudinaryField | 'image', default='placeholder, null=True, blank=True
| description | | TextField |
| lineitem_total |  | DecimalField | max_digits=6, decimal_places=2

### 1.2 UX

I decided to go with the color palette found on this image [COLORS](docs/img/color_palette.jpg) which was generated using [coolors](https://coolors.co/). This was possible using the home page image that I found on [pexels](https://www.pexels.com/photo/assorted-decors-with-brown-rack-inside-store-683039/). From there I based the rest of the page on these 5 colors. 

### 1.3 User Stories 

- As a user, I expect to navigate the website with ease of use.
- As a user, I expect to find products as seamless as possible.
- As a user, I expect to put the products I want in a basket. 
- As a user, I expect to type in keywords in the search bar to find specific products. 
- As a user, I expect to checkout after finding all the products I need.
- As a user, I expect have a login system in order to view my shopping history. 


##  2 Features 

### 2.1 Existing Features

All of my pages consist of the same navigation menu bar or hamburger icon for mobile devices. This format allows the user to understand where everything is located at all times for simplicity. The dropdown/menu will have options for 2 separate continents South America and Africa with countries within the continents. There you will have an existing choice of coffee products you can choose from. The option to add these items to your shopping bag is included as well. The items have a description a rating and a tag for their country of origin. 
