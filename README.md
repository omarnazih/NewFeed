# NewFeed Microservice

This project is a simple microservice using Flask for a social media application with basic entities: User, Post, Comment, Like, Share, and Follow/Friendships.

## Table of Contents

- [Requirements](#requirements)
- [ERD Diagram](#erd-diagram)
- [SQL Implementation](#sql-implementation)
- [Python Microservice with Flask](#python-microservice-with-flask)
- [Usage](#usage)

## Requirements

The main focus of the business is to create a simple newsfeed app with the following entities:

1. User
2. Post
3. Comment
4. Like
5. Share
6. Follow/Friendships

## ERD Diagram

![ERD Diagram Screenshot](newfeed-erd.png)

## SQL Implementation

[script.sql](https://github.com/omarnazih/NewFeed/blob/main/script.sql)

## Python Microservice with Flask

### Usage

Follow these steps to set up and run the microservice:

### Prerequisites

- Python >= 3.8
- Docker installed (for mysql db)
- Git installed

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/omarnazih/NewFeed.git
   cd NewFeed
   ```

2. Create and Activate virtual environment

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install requirements.txt

   ```bash
   pip install -r requirements.txt
   ```

4. Build and run the Docker containers to run mysql db:

   ```bash
   docker-compose up --build
   ```

   This will launch the MySQL db. Ensure that your Docker daemon is running.

5. Run Flask service

   ```bash
   flask run
   ```

6. The microservice should be running at [http://localhost:5000](http://localhost:5000). You can now use the provided endpoints.

7. Swagger Documentation should also be available at [http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui)

8. To stop the containers, press `Ctrl + C` in the terminal where Docker is running, or run:

   ```bash
   docker-compose down
   ```
