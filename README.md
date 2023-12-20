
<div align="center">

![](asc.png)

<h1 style="font-size:xxx-large;">
  <font color="aliceblue">
    African Unity Club
  </font>
<h1>

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub contributors](https://img.shields.io/github/contributors/African-Unity-Club/african-unity-club.svg)](https://github.com/African-Unity-Club/african-unity-club/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/African-Unity-Club/african-unity-club.svg)](https://github.com/African-Unity-Club/african-unity-club/issues)
[![GitHub stars](https://img.shields.io/github/stars/African-Unity-Club/african-unity-club.svg)](https://github.com/African-Unity-Club/african-unity-club/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/African-Unity-Club/african-unity-club.svg)](https://github.com/African-Unity-Club/african-unity-club/network)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/African-Unity-Club/african-unity-club.svg)](https://github.com/African-Unity-Club/african-unity-club/pulls)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?url=https://github.com/African-Unity-Club/african-unity-club.git)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Share-blue)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/African-Unity-Club/african-unity-club.git)
[![Facebook](https://img.shields.io/badge/Facebook-Share-blue)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/African-Unity-Club/african-unity-club.git)

</div>

creation of a communication network between African intellectuals throughout the world for the valorisation of the African continent, its diversities, its values, its cultures and its immense unexploited potential by means of sharing, of discovery aiming at knowing its continent its power its history and its place in the future of humanity.

[Project Design](https://www.figma.com/file/xOZSamTWQ1080dHkTV4Bru/African-Student-Club?type=design&node-id=0-1&mode=design&t=GDicutDVTz5uIHg8-0)

![](design.png)

## Run project

there are several microservices communicating via http, so for a local launch you'll need to launch all the microservices individually, and certainly in a particular order depending on dependencies.

which we'll look at later

1- clone

```bash
$ git clone https://github.com/African-Unity-Club/african-unity-club.git
```

2- install requirements and dependencies

```bash
$ cd african-unity-club
```

- in Unix

```bash
african-unity-club$ sudo apt install virtualenv
african-unity-club$ virtualenv .venv
african-unity-club$ . .venv/bin/activate
african-unity-club$ python3 -m pip install -r requirements.txt
```

- in Windows

```bash
african-unity-club$ python -m venv .venv
african-unity-club$ .venv\Scripts\activate
african-unity-club$ python -m pip install -r requirements.txt
```

3- run


## Features

the various functions to be implemented

### Authentication by token

- signup (register)
- otp (email verify)
- signin (login)
- 2 factor authenticate (security)
- signout (logout)
- forgot password (password reset)

### Dashboard

contains global and individual user activity statistics in diagrams, gauges and curves.<br>
it's a complete summary

don't hesitate to add useful features, but also to share them for better coordination

### Profile manager

account management <br>
it contains everything that concerns the user personally 

### Social

- post your experience, life ...

### Culture

- presentation of your culture, traditions, rites and customs
- your country, its archipelago, its riches, its wonders, its special features

### Talents

- your know-how, your ingenuity, your skills

### Stories

- your history, that of your country and your people, its past glory, its suffering, its struggles, its vision, its hopes

### Jobs

- your country's job offers and opportunities, its benevolence towards its African neighbors.

### Community

- community based on values, visions, fraternity, job opportunities, ...

### News

- african news

### Planning task

- planning and automation of one-off or recursive tasks,
meet course planning, ...

### Notifications

- notification system

### Chats

- text messages, short video, audio ...

### Friendship

- creating bonds of friendship and unity

### Settings

- account configurations for personal life respects

## Technologies

- Back end (API RESTful)
  - Flask
  - Django rest framework
  - Nodejs
  - MySQL
  - PostgreSQl
  - Mongodb
  - Redis
  - Sqlite3
  - ...
- Front end
  - HTML/CSS
  - Javascript
  - Tailwind
  - Bootstrap
  - React
  - Redis
  - Sqlite3
  - ...

## environment

- vscode, pycharm, spyder
- insomnia
- pgAdmin
- MongoDBCompass
- docker

## Deployement

```bash
not yet available
```

## How to contibute

see [how to contribute file](CONTRIBUTING.md)
