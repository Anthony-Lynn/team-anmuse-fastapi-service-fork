# Day4 Business Requirements:

## Create_product endpoint
   - Given the POST /products endpoint is defined
   - When I submit a request using the Product Pydantic schema
   - Then it's saved in postgres using the Product SQLAlchemy model and returns the saved product object using a response_model with 201 status code

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

## Update Products
   - Given that I have a product and the PUT /products is defined
   - When I submit the request at the products given id with the given body:
   {
      "name": str,
      "unit": str,
      "cost_per_unit": float,
      "price_per_unit": float,
      "quantity_in_stock": float
   }
   - Then it updates the product at that id and returns the updated product with a 200 status code

## Delete Products
   - Given I have a product and the DELETE /products endpoint is defined
   - When calling the request with the given id
   - Then it removes the product at that id and returns a 204 status code

## Update Rasies Error On Missing ID
   - Given we have a PUT /products endpoint defined
   - When calling the endpoint with a missing id
   - Then we raise a HTTPException with 404 status code with a no product found message

## Remove Rasies Error On Missing ID
   - Given we have a DELETE /products endpoint defined
   - When calling the endpoint with a missing id
   - Then we raise a HTTPException with 404 status code with a no product found message

## Update Reject Invalid Data
   - Given we have a PUT /products endpoint defined
   - When calling the endpoint with an invalid request body
   - Then we raise a HTTPException with 422 status code with its relative message

## Document API Requests
   - Given we have an API documenation with a list of endpoints
   - When someone call an endpoint listed on the API
   - Then they should get the relative response based on the request endpoint documentation
