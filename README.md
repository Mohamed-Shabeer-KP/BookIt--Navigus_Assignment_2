# BookIt -- Navigus-assignment-2

BookIt is a Django application integrated with DjangoRest Framework for creating and booking slots for appointments.

## Deployed in Heroku

[BookIt Heroku Application](https://bookit-navigus-assignment2.herokuapp.com/).

## Sample data 


For [login](https://bookit-navigus-assignment2.herokuapp.com/login/) in BookIt application.,
```json
{
  "Email": "sam@gmail.com",
  "Password": "sam123"
}
```
For [login](https://bookit-navigus-assignment2.herokuapp.com/api-auth/login/?next=/api/list/) in BookIt API endpoints,
```json
{
  "Username": "sam",
  "Password": "sam123"
}
```
For [Django Admin](https://bookit-navigus-assignment2.herokuapp.com/admin/) page,
```json
{
  "Username": "administrator",
  "Password": "admin"
}
```


## Flow and Bonus points
1. User registration at [link](https://bookit-navigus-assignment2.herokuapp.com/register/).
1. User login and authentication [link](https://bookit-navigus-assignment2.herokuapp.com/login/).
1. User can access API from the UI after login or through API Endpoints.
   1. Create slot  
   1. Book slot 
   1. Update slot  
   1. Remove slot (only owner of a slot can remove the slot).
1. Bonus Points
   1. Unit cases added for API 
        1. single user test
        1. single slot test
        1. single get list test
## Sample Images
![index](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/1.PNG?alt=media&token=e8d07171-84e1-4b7d-8ef2-099e53b7c9df)
