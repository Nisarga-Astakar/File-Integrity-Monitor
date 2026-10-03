# File Integrity Monitoring & Tamper Detection System

A Python-based cybersecurity tool that uses **SHA-256 hashing** to establish a trusted file baseline and detect file modifications, deletions, and newly added files.

The system also generates timestamped security logs and provides an integrity scan summary.

## Overview

File Integrity Monitoring (FIM) is a defensive security technique used to identify unauthorized or unexpected changes to important files.

This project creates a known-good baseline of protected files using SHA-256 hashes. During a later integrity scan, the current file hashes are compared with the stored baseline.

If a file has been modified, deleted, or newly added, the system generates a security alert.

## Features

- SHA-256 file hashing
- Trusted file baseline creation
- Modified file detection
- Deleted file detection
- New file detection
- Timestamped security event logging
- Alert severity levels
- Integrity scan summary
- Recursive scanning of protected directories
- JSON-based baseline storage
- Command-line interface

## Technologies Used

- **Python 3**
- **SHA-256**
- **JSON**
- **Python pathlib**
- **Python hashlib**
- **Python datetime**
- **Git & GitHub**

## How It Works

```text
                    Protected Files
                          |
                          v
                  Calculate SHA-256
                          |
                          v
                  Create Baseline
                          |
                          v
                    baseline.json
                          |
                          |
                  Later Integrity Scan
                          |
                          v
                  Calculate New Hashes
                          |
                          v
                  Compare with Baseline
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
          Unchanged    Modified    Deleted
              |           |           |
              |           +-----------+
              |                   |
              v                   v
             OK                 ALERT
                                  |
                                  v
                           Security Log
                                  |
                                  v
                           Scan Summary
```

## Detection Logic

### 1. Unchanged File

If the current SHA-256 hash matches the baseline hash:

```text
Baseline Hash == Current Hash
```

The file is considered unchanged.

Example:

```text
[OK] FILE UNCHANGED: protected_files\sample.txt
```

### 2. Modified File

If the current SHA-256 hash differs from the baseline:

```text
Baseline Hash != Current Hash
```

The system generates an alert.

Example:

```text
[ALERT] FILE MODIFIED: protected_files\sample.txt
```

### 3. Deleted File

If a file exists in the baseline but cannot be found during the current scan:

```text
[ALERT] FILE DELETED: protected_files\sample.txt
```

### 4. New File

If a file exists during the current scan but was not present in the baseline:

```text
[ALERT] NEW FILE DETECTED: protected_files\unauthorized.txt
```

## Project Structure

```text
File-Integrity-Monitor/
│
├── main.py
├── README.md
├── .gitignore
│
├── protected_files/
│   └── .gitkeep
│
└── logs/
    └── security.log
```

The `baseline.json` file and security logs are generated locally at runtime and are excluded from the GitHub repository using `.gitignore`.

## Installation

### Prerequisites

- Python 3.x
- Git
- Windows, Linux, or macOS

Check your Python installation:

```bash
python --version
```

Clone the repository:

```bash
git clone https://github.com/Nisarga-Astakar/File-Integrity-Monitor.git
```

Move into the project directory:

```bash
cd File-Integrity-Monitor
```

## Usage

Run the program:

```bash
python main.py
```

The program displays:

```text
===== FILE INTEGRITY MONITOR =====

1. Create Baseline
2. Check Integrity

Enter your choice:
```

### Create a Baseline

Select:

```text
1
```

Example:

```text
[+] Baseline created successfully.
[+] Files recorded: 1
```

### Check File Integrity

Select:

```text
2
```

Example:

```text
===== INTEGRITY SCAN =====

[OK] FILE UNCHANGED: protected_files\sample.txt

===== SECURITY SUMMARY =====
Files Scanned   : 1
Unchanged       : 1
Modified        : 0
Deleted         : 0
New Files       : 0
Total Alerts    : 0
============================
```

## Security Event Logging

Security events are stored in:

```text
logs/security.log
```

Example:

```text
2026-10-03 10:29:33 | INFO | Integrity scan started
2026-10-03 10:29:33 | OK | FILE UNCHANGED | protected_files\sample.txt
2026-10-03 10:31:17 | INFO | Integrity scan started
2026-10-03 10:31:17 | ALERT | FILE MODIFIED | protected_files\sample.txt
```

The log provides:

- Timestamp
- Event severity
- Event type
- Affected file

## Testing

The system was tested using multiple file-integrity scenarios.

| Test | Action | Expected Result |
|---|---|---|
| 1 | Scan unchanged file | `FILE UNCHANGED` |
| 2 | Modify protected file | `FILE MODIFIED` |
| 3 | Delete protected file | `FILE DELETED` |
| 4 | Add new file | `NEW FILE DETECTED` |

### Example Modified File Test

A protected file was modified after creating the trusted baseline.

The system detected:

```text
[ALERT] FILE MODIFIED: protected_files\sample.txt
```

The security summary reported:

```text
Files Scanned   : 1
Unchanged       : 0
Modified        : 1
Deleted         : 0
New Files       : 0
Total Alerts    : 1
```

## Security Concepts Demonstrated

This project demonstrates practical knowledge of:

- File Integrity Monitoring
- Cryptographic hashing
- SHA-256
- Baseline verification
- Tamper detection
- Security event logging
- Alert generation
- Defensive security
- Basic SOC monitoring concepts
- Python automation

## Limitations

This is an educational and portfolio project rather than a production-grade enterprise FIM solution.

Current limitations include:

- Integrity checks are manually initiated from the command line.
- The system does not identify which user made a file change.
- The system does not distinguish authorized changes from unauthorized changes.
- The baseline is stored locally in a JSON file.
- The system does not currently send alerts to a SIEM or security monitoring platform.
- SHA-256 detects content changes but does not identify the person responsible for the change.

## Future Improvements

Possible future enhancements include:

- Real-time file monitoring
- Windows/Linux event-log integration
- User attribution
- Email or notification alerts
- Web-based security dashboard
- SIEM integration
- Secure baseline storage
- Configuration file for protected directories
- Alert filtering and severity classification

## Learning Outcomes

Through this project, I practiced:

- Python programming
- Cryptographic hashing
- File-system operations
- JSON data handling
- Security event logging
- Git version control
- GitHub project management
- Basic defensive cybersecurity concepts

## Author

**Nisarga Astakar**

Cybersecurity Engineering Student

GitHub:  
https://github.com/Nisarga-Astakar