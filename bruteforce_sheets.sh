#!/bin/bash

# Google Sheets URL Bruteforce Script (Bash version)
# Attempts to access Google Sheets URLs with numbers from 0 to 199

BASE_URL="https://docs.google.com/spreadsheets/d/"
START=${1:-0}
END=${2:-199}
DELAY=${3:-0.5}

echo "Google Sheets URL Bruteforcer (Bash)"
echo "Range: $START to $END"
echo "Delay: $DELAY seconds between requests"
echo "=================================================="
echo

# Create results file
RESULTS_FILE="found_sheets_bash.txt"
echo "Found Google Sheets URLs:" > "$RESULTS_FILE"
echo "=========================" >> "$RESULTS_FILE"

FOUND_COUNT=0

for i in $(seq $START $END); do
    URL="${BASE_URL}${i}"
    printf "Trying: %3d -> %s ... " "$i" "$URL"
    
    # Use curl to check the URL
    HTTP_CODE=$(curl -s -o /tmp/response_$i.html -w "%{http_code}" --connect-timeout 10 --max-time 15 "$URL")
    
    if [ "$HTTP_CODE" = "200" ]; then
        # Check if it's not an error page
        if ! grep -q "Sorry, the file you have requested does not exist" /tmp/response_$i.html && \
           ! grep -q "We're sorry, a server error occurred" /tmp/response_$i.html && \
           ! grep -q "Access denied" /tmp/response_$i.html; then
            echo "✓ FOUND!"
            echo "$i: $URL (HTTP $HTTP_CODE)" >> "$RESULTS_FILE"
            mv /tmp/response_$i.html "sheet_${i}_content_bash.html"
            echo "    Content saved to sheet_${i}_content_bash.html"
            ((FOUND_COUNT++))
        else
            echo "✗ Not found"
            rm -f /tmp/response_$i.html
        fi
    else
        echo "✗ HTTP $HTTP_CODE"
        rm -f /tmp/response_$i.html
    fi
    
    # Add delay
    if [ "$DELAY" != "0" ]; then
        sleep "$DELAY"
    fi
done

echo
echo "=================================================="
echo "SUMMARY:"
if [ $FOUND_COUNT -gt 0 ]; then
    echo "Found $FOUND_COUNT accessible sheets."
    echo "Results saved to $RESULTS_FILE"
else
    echo "No accessible sheets found in the range."
fi