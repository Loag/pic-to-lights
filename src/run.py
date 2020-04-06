import sys, traceback
from app import run_app, kill_app

def on_start():
    run_app()

def on_end():
    kill_app()

def main():
    try:
        on_start()
    except KeyboardInterrupt:
        on_end()
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
