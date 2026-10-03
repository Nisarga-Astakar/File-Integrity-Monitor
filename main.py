import hashlib
import json
from pathlib import Path
from datetime import datetime


# ==============================
# CONFIGURATION
# ==============================

PROTECTED_FOLDER = Path("protected_files")
BASELINE_FILE = Path("baseline.json")
LOG_FOLDER = Path("logs")
LOG_FILE = LOG_FOLDER / "security.log"


# ==============================
# LOGGING FUNCTION
# ==============================

def write_log(level, event, file_path=""):
    """Write a security event to the log file."""

    LOG_FOLDER.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_path:
        log_entry = f"{timestamp} | {level} | {event} | {file_path}"
    else:
        log_entry = f"{timestamp} | {level} | {event}"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")


# ==============================
# HASH FUNCTION
# ==============================

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# ==============================
# CREATE BASELINE
# ==============================

def create_baseline():

    baseline = {}

    for file_path in PROTECTED_FOLDER.rglob("*"):

        if file_path.is_file():

            baseline[str(file_path)] = calculate_hash(file_path)

    with open(BASELINE_FILE, "w") as file:
        json.dump(baseline, file, indent=4)

    print("\n[+] Baseline created successfully.")
    print(f"[+] Files recorded: {len(baseline)}")

    write_log(
        "INFO",
        f"Baseline created - {len(baseline)} files"
    )


# ==============================
# LOAD BASELINE
# ==============================

def load_baseline():

    if not BASELINE_FILE.exists():

        print("[!] Baseline does not exist.")

        write_log(
            "WARNING",
            "Baseline file not found"
        )

        return {}

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)


# ==============================
# INTEGRITY CHECK
# ==============================

def check_integrity():

    baseline = load_baseline()

    current_files = {}

    # Security counters
    unchanged_count = 0
    modified_count = 0
    deleted_count = 0
    new_count = 0

    print("\n===== INTEGRITY SCAN =====\n")

    write_log(
        "INFO",
        "Integrity scan started"
    )

    # Scan current files
    for file_path in PROTECTED_FOLDER.rglob("*"):

        if file_path.is_file():
            current_files[str(file_path)] = calculate_hash(file_path)

    # Check files from baseline
    for file_path, old_hash in baseline.items():

        # Deleted file
        if file_path not in current_files:

            print(f"[ALERT] FILE DELETED: {file_path}")

            deleted_count += 1

            write_log(
                "ALERT",
                "FILE DELETED",
                file_path
            )

        # Modified file
        elif current_files[file_path] != old_hash:

            print(f"[ALERT] FILE MODIFIED: {file_path}")

            modified_count += 1

            write_log(
                "ALERT",
                "FILE MODIFIED",
                file_path
            )

        # Unchanged file
        else:

            print(f"[OK] FILE UNCHANGED: {file_path}")

            unchanged_count += 1

            write_log(
                "OK",
                "FILE UNCHANGED",
                file_path
            )

    # Detect new files
    for file_path in current_files:

        if file_path not in baseline:

            print(f"[ALERT] NEW FILE DETECTED: {file_path}")

            new_count += 1

            write_log(
                "ALERT",
                "NEW FILE DETECTED",
                file_path
            )

    # Calculate total
    total_alerts = (
        modified_count
        + deleted_count
        + new_count
    )

    # Display summary
    print("\n===== SECURITY SUMMARY =====")

    print(f"Files Scanned   : {len(current_files)}")
    print(f"Unchanged       : {unchanged_count}")
    print(f"Modified        : {modified_count}")
    print(f"Deleted         : {deleted_count}")
    print(f"New Files       : {new_count}")
    print(f"Total Alerts    : {total_alerts}")

    print("============================")

    write_log(
        "INFO",
        f"Scan completed - {total_alerts} alert(s)"
    )

# ==============================
# MAIN MENU
# ==============================

if __name__ == "__main__":

    print("===== FILE INTEGRITY MONITOR =====")

    choice = input(
        "\n1. Create Baseline"
        "\n2. Check Integrity"
        "\n\nEnter your choice: "
    )


    if choice == "1":

        create_baseline()


    elif choice == "2":

        check_integrity()


    else:

        print("[!] Invalid choice")

        write_log(
            "WARNING",
            "Invalid menu selection"
        )