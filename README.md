# BookIt -- Navigus-assignment-2

BookIt is a Django application integrated with DjangoRest Framework for creating and booking slots for appointments.

## Deployed in Heroku

[BookIt Heroku Application](https://bookit-navigus-assignment2.herokuapp.com/)

## Url pattern for API End-points

1. Slot creation  - [https://bookit-navigus-assignment2.herokuapp.com/api/post/](https://bookit-navigus-assignment2.herokuapp.com/api/post/)
1. View all slots - [https://bookit-navigus-assignment2.herokuapp.com/api/list/](https://bookit-navigus-assignment2.herokuapp.com/api/list/)
1. Slot Booking   - ```https://bookit-navigus-assignment2.herokuapp.com/api/book/slot id/```
1. Slot Remove   -  ```https://bookit-navigus-assignment2.herokuapp.com/api/remove/slot id/```

Postman API Collecion : [Link](https://documenter.getpostman.com/view/12165569/T1DqfGCo)

## Sample User data 

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
1. Landing page

![index](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/1.PNG?alt=media&token=e8d07171-84e1-4b7d-8ef2-099e53b7c9df)

1. Logged In page

![logged in](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/2.PNG?alt=media&token=bf5136e6-3553-4265-9bfb-878f5f128a3d)

1. Create slot API

![create slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/3.PNG?alt=media&token=654e1181-e5f7-42fd-9731-f823177fa81d)

1. Slot view API

![slot view api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/4.PNG?alt=media&token=fa495ba8-ef63-4fac-970a-fd96f63dd191)

1. Book slot API

![book slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/5.PNG?alt=media&token=ffe60a93-1171-4eb8-9e7b-b57cf08051c6)

1.Remove slot API

![book slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/6.PNG?alt=media&token=ad1849b9-ef4c-4305-ad8f-0c43d2ba3248)

1.Unauthorized access to api

![unauth api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/7.PNG?alt=media&token=fb7bae2c-f0aa-4e1d-b0e9-aeaa3318b150)

1.Django admin slot model

![admin page slot model](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/8.PNG?alt=media&token=9ae7e719-ba30-4419-b37d-f383eed9bd85)

