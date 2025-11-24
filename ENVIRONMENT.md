Environment setup for Butter And Bliss (Bakery)

This project uses Python and Django. The files added here help you create a reproducible virtual environment and install project dependencies.

Quick steps (Windows PowerShell)

1. From project root (where `manage.py` is):

    .\scripts\setup_env.ps1

   If PowerShell blocks script execution, run (as admin) `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` then run the script.

2. Activate the venv (if the script didn't activate automatically):

    . .venv\Scripts\Activate.ps1

3. Run the dev server:

    python manage.py runserver

Quick steps (macOS / Linux / WSL)

1. From project root:

    bash scripts/setup_env.sh

2. If not active, activate the venv:

    source .venv/bin/activate

3. Run the dev server:

    python manage.py runserver

Notes

- The script creates a virtual environment in `.venv` and installs Python packages listed in `requirements.txt`.
- `requirements.txt` currently pins `Django==5.2.8` and `Pillow` (for ImageField support). Add other packages if your project requires them.
- Place licensed static assets in `Bakery/static/images/` and user-uploaded media in `media/`.
- Copy `.env.example` to `.env` and fill in a secure `SECRET_KEY` and any other environment-specific values.

Production

- When deploying with `DEBUG=False`, run `python manage.py collectstatic` and configure your web server (nginx etc.) to serve `/static/` and `/media/`.
- Do not commit `.env` or any secret keys into version control.
