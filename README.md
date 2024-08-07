# CoffeeLog

## Overview

CoffeeLog is a journaling application to track details about the coffee you drink, and provide aggregated data and metrics.

## Details

### Authentication

`User` is defined as a Flask model class, inheriting SQLAlchemy from `FlaskApp` as the underlying database model.

**User Database Attributes**

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| Email | String | Yes | A user’s email address, used as the primary key |
| Password | Hashed string | Yes | Encrypted using Flask-Bcrypt method generate_password_hash - https://flask-bcrypt.readthedocs.io/en/1.0.1/#flask_bcrypt.Bcrypt.generate_password_hash |
| CreatedTime | Datetime | Yes | Automatically created during User registration |
| AdminAccess | Boolean | No | Access flag for admin control, defaults to FALSE. Note: can be changed to store as ENUM if more granularity is required |

A User’s password is encrypted using `Flask-Bcrypt` extension with method `generate_password_hash` . Further parameters can be passed during hashing as needed, namely

1. (**required**) `password`: The password to be hashed
2. `rounds`: The optional number of rounds.
3. `prefix`: The algorithm version to use.

Password validation is similarly done using another `Flask-Bcrypt` method called `check_password_hash`. This method will return a boolean value, returning True if the provided password matches the saved password hash.

Example

```python
from flask_app import bcrypt, db

username = "zoon"
password = "somepassword"

# Saving
hashed_password = bcrypt.generate_password_hash(password)

# Validation
def validate_password(raw_password):
	return bcrypt.check_password_hash(hashed_password, password)

# store username and hashed_password to json
```

Basic requirements:

1. Username and password are inputted via webpage from html forms
2. Login info is passed to backend python handler
3. Handler verifies if username and password are valid for login, or username does not already exist for registration.
4. User is redirected to home page after login or registration

### Database

**Tech** - Local SQL database for development. Google SQL Server database for Prod

**Database Name** - `coffeelog-coffeedrink-metadata`

[**Database Attributes**](https://www.notion.so/CoffeeLog-a85ea1b4728246d882816c12817bc87f?pvs=21)

| Name | Type | Required | Notes | Examples |
| --- | --- | --- | --- | --- |
| BrewId | String | Yes |  | See https://www.notion.so/CoffeeLog-a85ea1b4728246d882816c12817bc87f?pvs=21 |
| UserId | String | Yes | Automatically set using user’s email | UserId = zoon for Email = zoon@gmail.com |
| DrinkName | String | Yes | User provided custom name | Drip, Latte, Cold Brew |
| QuantityInFluidOz | Number (int) | Yes |  | 12, 16, 20 |
| MilkOptions | String | No |  | Whole milk, half n half, oat milk |
| Additives | List<String> | No |  | [Vanilla syrup, cinnamon] |
| CoffeeBeans | Map | No |  | See CoffeeBeans table |
| Cafe | String | No |  | Victorola Cafe |
| CreatedTime | Datetime | Yes | Automatically set during record creation |  |
| DrinkTime | Datetime | Yes | User provided date and time when drink was consumed. Defaults to CreatedTime  |  |

**BrewId**

1. Primary unique key for each record in database
2. Auto-generated for each record with format `<UserId>-<CreatedTime>`
    1. UserId - Prefix of a user’s email (everything before `@`) e.g. UserId = `zoon` for Email = `zoon@gmail.com`
    2. EntryTimestamp - timestamp in millisec when record was created, `1723070889572`
    3. e.g. `zsaziz-1723070889572`

[**CoffeeBeans Attributes**](https://www.notion.so/CoffeeLog-a85ea1b4728246d882816c12817bc87f?pvs=21)

| Name | Type | Required | Notes | Examples |
| --- | --- | --- | --- | --- |
| Producer | String | Yes |  | Caffe Vita, Onda Origins, Victorola Cafe |
| CountryOfOrigin | String | Yes |  | Brazil, Guatemala, Colombia |
| Name | String | No |  | Fiore Espresso, Midnight Drip |
| RoastLevel | Number (int), [1,10] | No | Single select from list of numbers [1,10] | 1-Lightest, 5-Medium, 10-Darkest |
| FlavorNotes | List<String> | No |  | [Caramel, Nutmeg, Cinnamon], [Raspberry] |
| RoastDate | Date | No |  | 2024-04-15 |

## Future Goals/Ideas

|  | Feature | Notes |
| --- | --- | --- |
| 1. | Send users prompts/”horoscopes” based on coffee data | Example “you started everyday this week with the same type of drink (latte) - sunshine is upon you or you may die a horrible death” |