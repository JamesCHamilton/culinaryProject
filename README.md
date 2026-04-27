# FlavorFusion - Culinary Project Documentation

FlavorFusion is a Django-based web application for managing and discovering recipes. It features a robust authentication system powered by Supabase and a dynamic filtering system.

## Table of Contents
1. [Setup and Installation](#setup-and-installation)
2. [Authentication (Supabase)](#authentication-supabase)
3. [Core Features](#core-features)
4. [Project Structure](#project-structure)
5. [User Data Management](#user-data-management)

---

## Setup and Installation

### 1. Environment Configuration
Create a `.env` file in the root directory with the following variables:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
SECRET_KEY=your_django_secret_key
DEBUG=True
```

### 2. Dependency Installation
Install the required Python packages:
```bash
pip install django supabase python-dotenv dj-database-url
```

### 3. Database Initialization
Run migrations and optionally seed the database with initial categories (Country, Ingredients, Tags):
```bash
python manage.py migrate
python seed_data.py
```
*Note: `seed_data.py` creates recipes without authors. These will not appear on the home page as per the requirement to only show user-created content.*

---

## Authentication (Supabase)

The application uses **Supabase Auth** for user registration and login, integrated with Django's session management.

### Workflow:
1. **Signup**: Users register via the `/signup/` route. The account is created in Supabase, and a corresponding Django `User` object is synchronized in the local database.
2. **Signin**: Users log in via `/signin/`. The application verifies credentials against Supabase and initializes a Django session.
3. **Signout**: Clears the Django session and logs the user out.

### Key Files:
- `recipes/supabase_utils.py`: Contains the client initialization logic.
- `recipes/views.py`: Contains `signup`, `signin`, and `signout` logic.

---

## Core Features

### 1. Home Page & Filtering
The home page (`/`) displays a feed of recipes.
- **Author Requirement**: Only recipes with an assigned `author` (User) are displayed. Seed recipes without authors are hidden from the main feed.
- **Search**: Search by title or instructions.
- **Filters**: Filter by Country, Ingredients, and multiple Dietary Tags.

### 2. Recipe Management
- **Create Recipe**: Authenticated users can add new recipes. The application automatically assigns the logged-in user as the `author`.
- **Favorites**: Users can toggle recipes as favorites.
- **Rating**: Users can rate recipes from 1 to 5 stars.

---

## Project Structure

- `flavorfusion/`: Project configuration and settings.
- `recipes/`: Core application logic.
    - `models.py`: Database schema for Recipes, Ingredients, Countries, etc.
    - `views.py`: Request handling and Auth logic.
    - `supabase_utils.py`: Supabase client helper.
- `templates/`: HTML templates.
    - `base.html`: Main layout with Navigation and Flash Messages.
    - `recipes/`: App-specific templates (home, detail, signup, signin).

---

## User Data Management

All user-generated data is tied to their Django User account:
- **Ownership**: Each `Recipe` has a foreign key to `User`.
- **Favorites**: Stored in the `Favorite` model, linking a `User` to a `Recipe`.
- **Ratings**: Stored in the `Rating` model with a unique constraint per user/recipe pair.

When a user creates an account through Supabase, their data is persisted locally in the Django database, allowing for efficient querying and relationship management while offloading credential security to Supabase.
