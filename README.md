# Fyle-Assignment

### REST service that can fetch bank details, using the data given in the API’s query parameters.

### Essential Features
- GET API to fetch a bank details, given branch IFSC code
- GET API to fetch all details of branches, given bank name and a city 
- Each API supports limit & offset parameters
- APIs authenticated using a JWT key, with validity of access and refresh token = 5 days (customizable)

### Add-ons
- In this particular scenario as the bank details don't generally change in a short period of time , as well as for every authenticated       user (from the same system) the results happens to be same so the best approach to prevent db calls again and again is caching the         results once a user sends a get request and then serving the next requests with the cached results to prevent db calls and response         time. Default django db is used for caching , for a period of 2 minutes(customizable).

## Valid Urls
- GET- /bankDetail?ifsc_code=x
- GET- /branches?bank_name=x&city=y&offset=2&limit=10
- POST- /api/token/ 
- POST- /api/token/refresh/
