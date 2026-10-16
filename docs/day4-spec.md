# Day4 Business Requirements:

## Create_product endpoint 
   As a developer, I want 
   - Given the POST /products endpoint is defined
   - When I submit a request using the Product Pydantic schema
   - Then it's saved in postgres using the Product SQLAlchemy model and returns the saved product object using a response_model with 201 staus code

## Get /product returns products saved in database
   - Given at least one product has been submitted via POST /products
   - When I call GET /products
   - Then the response includes a list of products submitted so far in our database with a 200 status code


## Get product by id endpoint
   
   -  Given the GET/products/{id} endpoint is defined
   -  when I submit GET/products/7 
   -  Then it returns a product with a id of 7 if it exists with 200 status code

## Non-existant product

   -  Given the GET/products/{id} endpoint is defined
   -  when I submit GET/products/Non-existant-ID
   -  Then it returns a 404 status code with {"message" : "Not found"}

## Get product list

   -  Given the GET/products endpoint is defined
   -  when I submit GET/products
   -  Then it returns the list of products with a 200 status code

## Control API responses
   
   - Given that response models are defined
   - When I submit requests to product endpoints
   - Then it returns the appropriate data with response model defined on the endpoint 