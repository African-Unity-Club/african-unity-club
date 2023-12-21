# AUTHENTICATION

1- run authenticate microservice

```bash
african-unity-club$ python -m venv .venv
african-unity-club$ . .venv/bin/activate
(.venv) african-unity-club$ pip install -r requirements.txt
(.venv) african-unity-club$ cd backend
(.venv) african-unity-club/backend$ cd auth
(.venv) african-unity-club/backend/auth$ flask --app app run --debug
```

2- signup

```javascript
/* data */
{
    "username": "victor",
    "email": "victor@gmail.com",
    "password":"0000000000"
}
/* response */

[
	{
		"data": {
			"_id": "65843b3fd8ec928eb4aa9fa6",
			"about": "",
			"avatar": "african-unity-club\\uploads\\nouser.png",
			"birth": "",
			"city": "",
			"country": "",
			"created_at": "2023-12-21T13:18:55.545157",
			"email": "victor",
			"first_name": "",
			"last_login": "2023-12-21T13:18:55.954475",
			"last_name": "",
			"password": "$2b$12$wqtw7sx1t0ImZNK0I7dAZOSML44IEmB0r4e7.xN1HiIumNK.gRgYO",
			"phone": "",
			"role": "user",
			"state": "",
			"status": "active",
			"street": "",
			"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU2NzM1Ljk1MzQ4NX0.c3dn2X6oukSKXjKKkhJK5_eFnWWaBal_K5JwhykJnkM",
			"updated_at": "2023-12-21T13:18:55.545157",
			"username": "victor"
		},
		"message": "Success"
	},
	201
]
```

3- signout

```javascript
Authorization --AUC-- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU2NzM1Ljk1MzQ4NX0.c3dn2X6oukSKXjKKkhJK5_eFnWWaBal_K5JwhykJnkM
```

4- signin

```javascript
/*data*/
{
	"username": "victor",
	"password": "0000000000"
}

/*headers*/
Authorization --AUC-- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU2NzM1Ljk1MzQ4NX0.c3dn2X6oukSKXjKKkhJK5_eFnWWaBal_K5JwhykJnkM

/*response*/
{
	"data": {
		"_id": "65843b3fd8ec928eb4aa9fa6",
		"about": "",
		"avatar": "african-unity-club\\uploads\\nouser.png",
		"birth": "",
		"city": "",
		"country": "",
		"created_at": "2023-12-21T13:18:55.545157",
		"email": "victor",
		"first_name": "",
		"last_login": "2023-12-21T13:25:21.109596",
		"last_name": "",
		"password": "$2b$12$wqtw7sx1t0ImZNK0I7dAZOSML44IEmB0r4e7.xN1HiIumNK.gRgYO",
		"phone": "",
		"role": "user",
		"state": "",
		"status": "active",
		"street": "",
		"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU3MTIxLjEwODU5Nn0.Cl88RlrGOlenI2s26Mx5LnlUxeP7axn35lakrF8Ayis",
		"updated_at": "2023-12-21T13:18:55.545157",
		"username": "victor"
	},
	"message": "Success"
}
```

=======================

BACKEND AUTHENTICATE OK

=======================