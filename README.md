# Django Kamal Demo

A Django project setup for deployment with [Kamal](https://kamal-deploy.org/).

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (or pip)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-kamal-demo
   ```

2. Install dependencies:
   ```
   uv pip install -e .
   ```

### Environment Configuration

This project uses `django-environ` to configure settings via environment variables. To set up your local environment:

1. Copy the example environment file:
   ```
   cp .env.example .env
   ```

2. Edit the `.env` file with your specific configuration values.

Available environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Django debug mode | `False` |
| `SECRET_KEY` | Django secret key | A default insecure key (for development only) |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `[]` |
| `DATABASE_URL` | Database connection URL | SQLite (`db.sqlite3` in project root) |

Example `.env` file:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

For production, set these variables in your environment or deployment configuration instead of using a `.env` file.

## Development

Run the development server:
```
python manage.py runserver
```

## Deployment with Kamal

This project is configured for deployment with Kamal. See the `config/deploy.yml` file for deployment configuration.

To deploy:
```
kamal setup
kamal deploy
```

Make sure to configure your production environment variables through Kamal's environment variable management.