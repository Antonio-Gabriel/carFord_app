# CardFord

An application that attribute a car to some person, the agency have only three brands of car and three colors too.

The system consists to add cars to the persons but never can exists a registered car without a person or owner of the car.

I developed this application using python, flask, alembic and sqlalchemy orm.

Database of system:

<img src="assets/modeling.png" alt="modeling database">

## Start

To start the app first you need to install docker in your machine if don't have and after, run the command bellow:

```bash
docker-compose --verbose build --no-cache
docker-compose up -d

# ubuntu
sudo docker-compose --verbose build --no-cache
sudo docker-compose up -d
```
Rename `.env.example` to `.env` to get the global variables.

The docker will create the container of application and the database automatically, and create a `seed` with some admin that will register or join persons to a car in the platform but it's need of authentication to work.

The authentication used was `JWT`

Some default credentials created after models migrations runs are:

```txt
admin 1
	email: herlanderbento@gmail.com
	password: herlanderbento

admin 2
	email: jorgeneto@gmail.com
	password: jorgeneto
```

if you can see the seed click on the link bellow:

[Migrations to seed admin](src/infra/migrations/versions/a027978e324e_create_migration_seed.py)

## Endpoints

The endpoints available for this application are:

#### POST(Authentication): `http://127.0.0.1:3333/auth`

Payload:
```json
{
	"email": "jorgeneto@gmail.com",
	"password": "jorgeneto"
}

# Response

{
	"msg": "Authentication success",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3IiOnsicGVyc29uX2lkIjoiYzFkODlhYTEtMTcxNS00MjIxLWJlNzMtZTU3MDBlOGZlMzkxIiwiZW1haWwiOiJqb3JnZW5ldG9AZ21haWwuY29tIn0sImV4cCI6MTY2NjU1MzMwNH0.8Ino9GIo5RzxdyJQ_yomJ_1Lb4BVXs1U9gICrn_C04M"
}
```

After, you need to add access_token at header as 
`x-access-token`

<img src="assets/token_header.png" alt="token header"/>

#### GET(Persons): `http://127.0.0.1:3333/persons`

```json
{
	"persons": [
		{
			"email": "herlanderbento@gmail.com",
			"id": "7bf4af59-e712-4a5c-a265-db8ec8077d5f",
			"name": "Herlander Bento"
		},
		{
			"email": "antoniogabriel2k20@gmail.com",
			"id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84",
			"name": "António Campos Gabriel"
		},
		{
			"email": "jorgeneto@gmail.com",
			"id": "c1d89aa1-1715-4221-be73-e5700e8fe391",
			"name": "Jorge Neto"
		}
	]
}
```
#### POST(Create Persons): `http://127.0.0.1:3333/persons/create`

Payload:
```json
{
	"name": "Antonio Gabriel",
	"email": "antoniogabriel2k20@gmail.com"
}

# Response

{
	"person": {
		"email": "antoniogabriel2k20@gmail.com",
		"id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84",
		"name": "Antonio Gabriel"
	}
}
```
#### PUT(Edit Persons): `http://127.0.0.1:3333/persons/update/{person_id: string}`

Payload:
```json

{
	"name": "António Campos Gabriel"
}

# Response

{
	"msg": "person updated",
	"person": {
		"email": "antoniogabriel2k20@gmail.com",
		"id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84",
		"name": "António Campos Gabriel"
	}
}
```
#### GET(Vehicles): `http://127.0.0.1:3333/vehicles`

```json
{
	"vehicles": [
		{
			"color": "yellow",
			"created_at": "Sun, 23 Oct 2022 14:08:49 GMT",
			"id": "e5f3c25d-72ac-45fb-be11-4818ef87e2d4",
			"model": "convertible",
			"person": {
				"email": "antoniogabriel2k20@gmail.com",
				"id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84",
				"name": "António Campos Gabriel"
			},
			"updated_at": "Sun, 23 Oct 2022 14:08:49 GMT"
		}
	]
}
```
#### POST(Add vehicle to person): `http://127.0.0.1:3333/vehicle/join/person`

Payload:
```json
{
	"model": "convertible",
	"color": "yellow",
	"person_id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84"
}

# Response 

{
	"msg": "The vehicle was added to bd5d0337-562c-4c82-8be0-89a40a7d4b84 with success!"
}
```
The validation to check if the model equals `["hatch", "sedan", "convertible"]` and the color equals `["yellow", "blue", "gray"]` has also been developed.

And I allow that the user can only have up to 3 cars.

#### GET(Vehicle by person): `http://127.0.0.1:3333/vehicles/{person_id: string}`

```json
{
	"vehicles": [
		{
			"color": "yellow",
			"created_at": "Sun, 23 Oct 2022 14:08:49 GMT",
			"id": "e5f3c25d-72ac-45fb-be11-4818ef87e2d4",
			"model": "convertible",
			"person": {
				"email": "antoniogabriel2k20@gmail.com",
				"id": "bd5d0337-562c-4c82-8be0-89a40a7d4b84",
				"name": "António Campos Gabriel"
			},
			"updated_at": "Sun, 23 Oct 2022 14:08:49 GMT"
		}
	]
}
```
These are the available end points

## Features

features that already builded are:

- [x] Create a person
- [x] Docker Environment
- [x] Create a seed for administrators
- [x] Authentication and route security
- [x] Create a vehicle attached to a person
- [x] Limited the number of vehicles per person (maximum 3)
- [ ] Swagger documentation

# Credits

António Gabriel 😁
