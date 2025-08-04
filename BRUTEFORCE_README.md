# Google Sheets URL Bruteforce Scripts

This repository contains scripts to bruteforce Google Sheets URLs with numbers from 0 to 199 (or custom ranges).

## Files

- `bruteforce_sheets.py` - Python version with advanced features
- `bruteforce_sheets.sh` - Bash version using curl
- `requirements.txt` - Python dependencies

## Python Version Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Usage
```bash
# Default: bruteforce from 0 to 199 with 0.5s delay
python3 bruteforce_sheets.py

# Custom range and delay
python3 bruteforce_sheets.py <start> <end> <delay>

# Examples:
python3 bruteforce_sheets.py 0 50 0.3      # Range 0-50, 0.3s delay
python3 bruteforce_sheets.py 100 199 1.0   # Range 100-199, 1s delay
```

### Features
- Timeout handling (10 seconds per request)
- Error detection (filters out "file not found" pages)
- Content saving for successful finds
- Progress tracking with visual indicators
- Results summary and file output
- Keyboard interrupt handling (Ctrl+C)

## Bash Version Usage

### Prerequisites
- `curl` command (usually pre-installed on Linux)

### Basic Usage
```bash
# Default: bruteforce from 0 to 199 with 0.5s delay
./bruteforce_sheets.sh

# Custom range and delay
./bruteforce_sheets.sh <start> <end> <delay>

# Examples:
./bruteforce_sheets.sh 0 50 0.3      # Range 0-50, 0.3s delay
./bruteforce_sheets.sh 100 199 1.0   # Range 100-199, 1s delay
```

## Output Files

### Python Version
- `found_sheets.txt` - List of successfully found URLs
- `sheet_N_content.html` - HTML content of found sheets (where N is the number)

### Bash Version
- `found_sheets_bash.txt` - List of successfully found URLs
- `sheet_N_content_bash.html` - HTML content of found sheets (where N is the number)

## URL Format

The scripts test URLs in the format:
```
https://docs.google.com/spreadsheets/d/{NUMBER}
```

Where `{NUMBER}` is replaced with integers from the specified range.

## Important Notes

⚠️ **Ethical Usage Warning**: This script is for educational purposes only. Make sure you have permission to test the target URLs and comply with Google's Terms of Service and rate limiting policies.

### Rate Limiting
- Both scripts include delays between requests to be respectful to the server
- Default delay is 0.5 seconds, but you can adjust it
- Consider using longer delays for large ranges

### Detection Logic
The scripts consider a URL "found" if:
1. HTTP status code is 200
2. The response doesn't contain common error messages like:
   - "Sorry, the file you have requested does not exist"
   - "We're sorry, a server error occurred"
   - "Access denied"

## Example Output

```
Google Sheets URL Bruteforcer
Range: 0 to 10
Delay: 0.5 seconds between requests
==================================================

Trying:   0 -> https://docs.google.com/spreadsheets/d/0 ... ✗ Not found
Trying:   1 -> https://docs.google.com/spreadsheets/d/1 ... ✗ HTTP 404
Trying:   2 -> https://docs.google.com/spreadsheets/d/2 ... ✓ FOUND!
    Content saved to sheet_2_content.html
...

==================================================
SUMMARY:
Found 1 accessible sheets:
  2: https://docs.google.com/spreadsheets/d/2 (HTTP 200)

Results saved to found_sheets.txt
```

## Troubleshooting

### Python Version
- If you get import errors, install dependencies: `pip install requests`
- For permission errors, run: `chmod +x bruteforce_sheets.py`

### Bash Version
- If curl is not found, install it: `sudo apt-get install curl` (Ubuntu/Debian)
- For permission errors, run: `chmod +x bruteforce_sheets.sh`