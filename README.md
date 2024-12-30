# Waqar Raza's Portfolio Website

This is a personal portfolio website built using Flask. The site showcases profile information, an about section, and a contact form that allows users to send messages. The messages are stored in a SQLite database, and admins can view, delete, and reply to messages.

## Features
- **Home Page**: Displays profile information and links to contact and about pages.
- **Contact Form**: Users can send messages by filling out a form.
- **Message Management**: Admins can:
  - View all messages.
  - Delete specific messages.
  - Reply to messages, with threaded replies visible on the message page.
- **About Page**: Provides details about Waqar Raza's interests, skills, and contact information.
- **Bootstrap Integration**: Responsive and clean design using Bootstrap 5.

## Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap)
- **Templates**: Jinja2

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/portfolio-website.git
   cd portfolio-website
   ```
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the Database**:
   ```bash
   flask shell
   from app import db
   db.create_all()
   exit()
   ```
5. **Run the Application**:
   ```bash
   flask run
   ```
   Visit `http://127.0.0.1:5000/` in your browser.

## Project Structure
```
portfolio-website/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── message.html
│   └── reply.html
│
├── static/
│   └── style.css
│
├── app.py
├── secret_key.py
├── requirements.txt
└── README.md
```

## How It Works
- **Contact Form**: Users submit a form which stores their information in the `data.db` file.
- **Message Replies**: Admins can reply to messages, creating a parent-child relationship in the database.
- **Flash Messages**: Feedback messages are displayed for actions like successful replies or errors.

## Requirements
- Flask
- Flask-SQLAlchemy
- Bootstrap 5

## Future Improvements
- Add pagination to the contact list.
- Implement admin authentication for message management.
- Deploy the site using services like Heroku or Render.

## Author
**Waqar Raza**  
Email: [waqarraza970@gmail.com](mailto:waqarraza970@gmail.com)  
GitHub: [Waqar885](https://github.com/Waqar885)  
LinkedIn: [Waqar Raza](https://www.linkedin.com/in/waqar-raza-0631882a6/)
