import os
import sys
import time
import json
import datetime
import urllib.request
import urllib.error

# ANSI Color Codes for scannability
ORANGE = "\033[38;5;208m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def display_harvester_banner():
    print(f"{CYAN}{BOLD}====================================================")
    print("        REAL-WORLD LIVE GEO-IP HARVESTER CORE        ")
    print(f"        TIMESTAMP: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"===================================================={RESET}\n")

class LiveIPHarvester:
    def __init__(self):
        self.input_filename = "target_ips.txt"
        self.output_filename = "global_resolved_ips.json"

    def read_local_ip_file(self):
        """Reads target IP addresses securely from a local physical text file."""
        if not os.path.exists(self.input_filename):
            # Automated fallback setup if the user hasn't generated the file yet
            print(f"{ORANGE}[!] File '{self.input_filename}' not found. Generating default sample stack...{RESET}")
            with open(self.input_filename, "w") as f:
                f.write("8.8.8.8\n1.1.1.1\n185.228.168.10\n")
        
        with open(self.input_filename, "r") as f:
            # Strip whitespace and isolate non-empty layout lines
            ips = [line.strip() for line in f if line.strip()]
        return ips

    def lookup_live_geoip(self, ip_address):
        """Dispatches real network requests to resolve geolocation metadata securely without an API key."""
        # Utilizing ip-api.com standard REST format wrapper
        url = f"http://ip-api.com{ip_address}?fields=status,message,country,regionName,city,lat,lon,isp"
        
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'ZeroCool-IP-Harvester-v8.0')
        
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    return json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return {"status": "fail", "message": str(e)}

    def run_harvesting_pipeline(self):
        display_harvester_banner()
        
        # 1. Pull the data payload directly from your computer storage drive
        target_ips = self.read_local_ip_file()
        print(f"{ORANGE}[*] Identified {len(target_ips)} targets to trace across network layers...{RESET}\n")
        time.sleep(0.5)

        resolved_manifest = []

        # 2. Loop through each target, tunneling onto live geolocation API endpoints
        for index, ip in enumerate(target_ips, 1):
            print(f"{WHITE}[Target #{index}/{len(target_ips)}] Querying live coordinates for: {ip}{RESET}")
            
            # API query execution step
            raw_geo = self.lookup_live_geoip(ip)
            
            if raw_geo.get("status") == "success":
                country = raw_geo.get("country", "Unknown")
                city = raw_geo.get("city", "Unknown")
                lat = raw_geo.get("lat", 0.0)
                lon = raw_geo.get("lon", 0.0)
                isp = raw_geo.get("isp", "Unknown")
                
                print(f"  {GREEN}[+] Resolved: {city}, {country}{RESET}")
                print(f"  {GREEN}[+] Routing Coordinates: [{lat}, {lon}] | ISP Provider: {isp}{RESET}\n")
                
                resolved_manifest.append({
                    "ip": ip,
                    "location": f"{city}, {country}",
                    "coordinates": f"{lat}, {lon}",
                    "network_provider": isp,
                    "mapped_at": str(datetime.datetime.now())
                })
            else:
                print(f"  {RED}[-] Query Failure for {ip}: {raw_geo.get('message', 'Unknown Error')}{RESET}\n")
            
            # Critical endpoint throttle safety pause (ip-api requires keeping queries under 45 per min)
            time.sleep(1.5)

        # 3. Permanently write the verified production data back onto physical media
        with open(self.output_filename, "w") as f:
            json.dump(resolved_manifest, f, indent=4)

        print(f"{CYAN}====================================================")
        print("         REAL-WORLD MAPPING PIPELINE COMPCOMPLETE   ")
        print(f"  Structured geographic database committed to: ./{self.output_filename}")
        print(f"===================================================={RESET}")
        sys.stdout.write("\a") # Sound system complete notification bell
        sys.stdout.flush()

if __name__ == "__main__":
    harvester = LiveIPHarvester()
    harvester.run_harvesting_pipeline()
