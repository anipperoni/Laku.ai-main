# Laku.ai - AI-Powered Sales Management System

Laku.ai is a modern, AI-powered sales management system designed to help small businesses track sales, manage inventory, and gain insights through an intuitive web interface.

## Features

- 📊 Real-time sales tracking and analytics
- 🔍 AI-powered sales insights and recommendations
- 📱 Responsive design that works on any device
- 🔐 Simple authentication system
- 🛒 Product and inventory management
- 📈 Sales reports and visualizations

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- Node.js 14.x or higher (for frontend assets)
- Google Gemini API key (for AI features)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/laku.ai.git
   cd laku.ai
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://username:password@localhost:5432/your_database
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Initialize the database**
   ```bash
   psql -U postgres -c "CREATE DATABASE your_database;"
   flask db upgrade
   ```

6. **Populate with sample data (optional)**
   ```bash
   psql -U postgres -d your_database -f sample_data.sql
   ```

## Running the Application

1. **Start the development server**
   ```bash
   flask run
   ```

2. **Access the application**
   Open your browser and navigate to: [http://localhost:5000](http://localhost:5000)

## First-Time Login

1. Open the login page at [http://localhost:5000/login](http://localhost:5000/login)
2. Enter any username and password (authentication is simplified for demo purposes)
3. Click "Sign In" to access the dashboard

## Project Structure

```
laku.ai/
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
├── migrations/       # Database migrations
├── .env             # Environment variables
├── app.py           # Main application file
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## API Endpoints

- `GET /` - Main dashboard
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /logout` - Logout user
- `GET /api/sales` - Get sales data (JSON)
- `DELETE /api/sales/<id>` - Delete a sale

## Development

### Running Tests
```bash
pytest
```

### Code Style
This project follows PEP 8 style guide. To check your code:
```bash
flake8 .
```

## Deployment

For production deployment, consider using:
- Gunicorn or uWSGI as the WSGI server
- Nginx as a reverse proxy
- PostgreSQL for the database
- Environment variables for configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact support@laku.ai
