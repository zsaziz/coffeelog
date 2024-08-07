from datetime import datetime, timezone

def get_current_local_datetime():
    return datetime.now(timezone.utc).astimezone()

def yes_or_no(message: str):
    res = input(message + '\nContinue? [y/N]: ')
    if res.lower() != 'y':
        raise SystemExit('Program was aborted by user.')