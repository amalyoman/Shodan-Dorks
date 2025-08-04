#!/usr/bin/env python3
"""
Google Sheets URL Bruteforce Script
Attempts to access Google Sheets URLs with numbers from 0 to 199
"""

import requests
import time
import sys
from urllib.parse import quote

def bruteforce_sheets(start=0, end=199, delay=0.5):
    """
    Bruteforce Google Sheets URLs with numbers from start to end
    
    Args:
        start (int): Starting number (default: 0)
        end (int): Ending number (default: 199)
        delay (float): Delay between requests in seconds (default: 0.5)
    """
    base_url = "https://docs.google.com/spreadsheets/d/{}"
    found_urls = []
    
    print(f"Starting bruteforce from {start} to {end}")
    print("=" * 50)
    
    for i in range(start, end + 1):
        # Try the number as is
        url = base_url.format(i)
        
        try:
            print(f"Trying: {i:3d} -> {url}", end=" ... ")
            
            # Make request with timeout
            response = requests.get(url, timeout=10, allow_redirects=True)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Check if it's not a "File not found" or error page
                if "Sorry, the file you have requested does not exist" not in response.text and \
                   "We're sorry, a server error occurred" not in response.text and \
                   "Access denied" not in response.text:
                    print("✓ FOUND!")
                    found_urls.append((i, url, response.status_code))
                    
                    # Save content for successful finds
                    with open(f"sheet_{i}_content.html", "w", encoding="utf-8") as f:
                        f.write(response.text)
                    print(f"    Content saved to sheet_{i}_content.html")
                else:
                    print("✗ Not found")
            else:
                print(f"✗ HTTP {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"✗ Error: {str(e)[:50]}...")
        except Exception as e:
            print(f"✗ Unexpected error: {str(e)[:50]}...")
        
        # Add delay to be respectful to the server
        if delay > 0:
            time.sleep(delay)
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    if found_urls:
        print(f"Found {len(found_urls)} accessible sheets:")
        for num, url, status in found_urls:
            print(f"  {num}: {url} (HTTP {status})")
    else:
        print("No accessible sheets found in the range.")
    
    return found_urls

def main():
    """Main function with command line argument support"""
    start = 0
    end = 199
    delay = 0.5
    
    # Simple command line argument parsing
    if len(sys.argv) > 1:
        try:
            start = int(sys.argv[1])
        except ValueError:
            print("Invalid start number. Using default: 0")
    
    if len(sys.argv) > 2:
        try:
            end = int(sys.argv[2])
        except ValueError:
            print("Invalid end number. Using default: 199")
    
    if len(sys.argv) > 3:
        try:
            delay = float(sys.argv[3])
        except ValueError:
            print("Invalid delay. Using default: 0.5")
    
    print("Google Sheets URL Bruteforcer")
    print(f"Range: {start} to {end}")
    print(f"Delay: {delay} seconds between requests")
    print("\nPress Ctrl+C to stop at any time")
    print()
    
    try:
        found_urls = bruteforce_sheets(start, end, delay)
        
        # Save results to file
        if found_urls:
            with open("found_sheets.txt", "w") as f:
                f.write("Found Google Sheets URLs:\n")
                f.write("=" * 30 + "\n")
                for num, url, status in found_urls:
                    f.write(f"{num}: {url} (HTTP {status})\n")
            print(f"\nResults saved to found_sheets.txt")
        
    except KeyboardInterrupt:
        print("\n\nBruteforce stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()