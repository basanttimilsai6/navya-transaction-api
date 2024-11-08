# Transaction API

This API allows users to perform various transaction-related operations. It includes authentication, user role management, and access controls for different endpoints.

## Getting Started

These instructions will help you set up and run the project on a local machine for development and testing.

### Prerequisites

- **Python 3.x**
- **Docker** (optional but recommended)
- **Postman** (Recommended)

### Installation

#### 1. Clone the Repository

Clone this repository to your local machine:

<!-- Terminal: -->
    git clone [https://github.com/basanttimilsai6/transaction-api.git](https://github.com/basanttimilsai6/navya-transaction-api.git)
    cd navya-transaction-api
    cd navya
    docker compose build --no-cache
    docker compose up

For Django container access:

    docker exec -it navya-web bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

<!-- Superuser username/password -->
    username=aaa
    password=aaa

    
The API will be available at http://localhost:8080/api/schema/swagger/


<!-- Tests are: -->

1. POST   /api/v1/transactions
2. GET    /api/v1/transactions
3. GET    /api/v1/transactions/:txnid
4. DELETE /api/v1/transactions/:txnid
5. PUT    /api/v1/transactions/:txnid
6. PATCH  /api/v1/transactions/:txnid
7. GET    /api/v1/pdf/transactions/
8. GET    /api/v1/pdf/transactions/:txnid

-> For endpoint 1, take the following inputs in the body :
   1. name
   2. phone
   3. email
   4. amount
   5. transaction_date

   Then save the data along with a unique transaction id prefixed by 'TXNID'. For eg: TXNID0057
   The response for this endpoint should return that transaction id.

-> For endpoint 2, return a response containing list of dictionaries containing  data of all the transactions.

-> For endpoints 3 to 6, implement the functionality as per the HTTP request type of a particular transaction based on transaction id.

-> For endpoint 7 and 8:
   Create a PDF with a template header of any logo you like. Put the logo at the top as static for all pdfs and create a dynamic table to be populated below the logo as per the data.

   - Endpoint 7 should be able to access/download the PDF which contains the data of all transactions in a horizontal table with column names and data.
   
   - Endpoint 8 should be able to access/download the PDF which contains the data of a transaction with specified transaction id in a vertical table with column names and data.


The access to above REST APIs should be handled through JWT Authentication and Authorization

Authorization Rules:

-> There will be two types of Users: Staffs and Managers

-> The Staff user will only be allowed to POST, PATCH, PUT and GET the transactions i.e. Endpoint 1, 2, 3, 5 and 6

-> The Manager user will be allowed all the endpoints

-> The PDF should be generated only after the Manager user approves the data posted by Staff and the transaction status should be updated to approved

-> The Manager can also reject the posted data, in which case the PDF won't be generated and transaction status should be updated to rejected
