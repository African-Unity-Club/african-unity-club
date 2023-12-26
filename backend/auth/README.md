# AUTHENTICATION

## Sign Up

1- *data*

- usernane (required)
- email (required)
- password (required)

2- *create user*

3- *token*

4- *login*

## Sign In

1- *data*

- username or email (required)
- password (required)

2- *2 factor check exist and verify*

- code (if 2 factor enable)

3- *token*

4- *login*

## Sign Out


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

endpoint = /signup

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
			"_id": "658aac4a1ce44e0b3b7a0a52",
			"about": "",
			"avatar": "african-unity-club\\uploads\\nouser.png",
			"birth": "",
			"city": "",
			"country": "",
			"created_at": "2023-12-26T10:34:50.846299",
			"email": "victor",
			"first_name": "",
			"last_login": "",
			"last_name": "",
			"password": "$2b$12$7Cc7nXD18SOJpq5Icps5/eaoNY8Buk6NfdKJbpseuiXchgomo3OVC",
			"phone": "",
			"role": "user",
			"state": "",
			"status": "pending",
			"street": "",
			"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4YWFjNGExY2U0NGUwYjNiN2EwYTUyIiwiZXhwIjoxNzA2MTc4ODkxLjIxNDQ2MX0.WG5HIIziJcNVVjB1ytAW2RblmUXRCUooKrgnyiS0wic",
			"updated_at": "2023-12-26T10:34:50.846299",
			"username": "victor"
		},
		"message": "Success"
	},
	200
]

```

3- signout

```javascript

endpoint = /signout

Authorization --AUC-- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU2NzM1Ljk1MzQ4NX0.c3dn2X6oukSKXjKKkhJK5_eFnWWaBal_K5JwhykJnkM

/* resposne */
{
	"data": {},
	"message": "Success"
}
```

4- signin

```javascript

endpoint = /signin

/*data*/
{
	"username": "victor",
	"password": "0000000000"
}

/*headers*/
Authorization --AUC-- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4NDNiM2ZkOGVjOTI4ZWI0YWE5ZmE2IiwiZXhwIjoxNzA1NzU2NzM1Ljk1MzQ4NX0.c3dn2X6oukSKXjKKkhJK5_eFnWWaBal_K5JwhykJnkM

/*response*/
[
	{
		"data": {
			"_id": "658aac4a1ce44e0b3b7a0a52",
			"about": "",
			"avatar": "african-unity-club\\uploads\\nouser.png",
			"birth": "",
			"city": "",
			"country": "",
			"created_at": "2023-12-26T10:34:50.846299",
			"email": "victor",
			"first_name": "",
			"last_login": "2023-12-26T10:38:24.529209",
			"last_name": "",
			"password": "$2b$12$7Cc7nXD18SOJpq5Icps5/eaoNY8Buk6NfdKJbpseuiXchgomo3OVC",
			"phone": "",
			"role": "user",
			"state": "",
			"status": "inactive",
			"street": "",
			"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjU4YWFjNGExY2U0NGUwYjNiN2EwYTUyIiwiZXhwIjoxNzA2MTc5NTEyLjY0NDUxNX0.agNWv1QxmsgSsc9O9oEHXWApCLzxvnwVAPGqyLkgHqw",
			"updated_at": "2023-12-26T10:34:50.846299",
			"username": "victor"
		},
		"message": "Success"
	},
	200
]
```

=======================

BACKEND AUTHENTICATE OK

=======================
