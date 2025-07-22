# Django Backend for Song Manager

### 🎵 Song Manager

A full-stack Song Management App built with **Django + Django REST Framework** (backend) and **React** (frontend). This application allows users to manage their favorite songs by performing CRUD (Create, Read, Update, Delete) operations.

---

## 🔧 Tech Stack

### Backend

- **Django** – Web framework for rapid development
- **Django REST Framework** – For building robust APIs
- **SQLite** – Lightweight built-in database for development

### Frontend

- **React** – Component-based frontend framework
- **Axios** – For communicating with backend APIs
- **Emotion / Styled-Components** – CSS-in-JS styling
- **Framer Motion** – For animations and transitions

---

## 🚀 Features

### Backend

- Full RESTful API
- CRUD operations for songs:
  - `title`, `artist`, `album`, `year`
- Data validation and error handling
- SQLite used for local dev (easy setup)

### Frontend

- Responsive React UI for song list management
- Pagination and search filter
- Add, edit, and delete songs from a simple form
- Real-time UI updates without page reloads
- Error handling and loading indicators
- Smooth animations for modals and transitions

---

## 🗂️ API Endpoints

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | `/api/songs/`     | Get all songs          |
| POST   | `/api/songs/`     | Add a new song         |
| PUT    | `/api/songs/:id/` | Update a specific song |
| DELETE | `/api/songs/:id/` | Delete a specific song |

---

## ⚙️ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 💻 Frontend Setup

```bash
cd frontend
npm install
npm start
```

Make sure the backend is running on `http://localhost:8000` so the frontend can connect via API.

---

## 📌 Todo / Improvements

- ✅ Basic song CRUD UI
- ⬜ Authentication and user accounts
- ⬜ Add album artwork upload
- ⬜ Improve mobile responsiveness
- ⬜ Deploy to production (e.g. Vercel + Railway)
