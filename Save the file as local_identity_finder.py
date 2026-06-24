import os

def scan_local_files(search_directory, keywords):
    """Scans local text-based files for specific account recovery keywords."""
    print(f"=== STARTING LOCAL SCAN ===")
    print(f"Directory: {search_directory}")
    print(f"Keywords: {', '.join(keywords)}\n")
    
    match_count = 0

    # Walk through all folders and files in the target directory
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            # Only scan text, markdown, or config files to avoid crashing on images/videos
            if file.endswith(('.txt', '.md', '.json', '.cfg', '.ini', '.log')):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            # Check if any of your keywords are in this line
                            for keyword in keywords:
                                if keyword.lower() in line.lower():
                                    print(f"[MATCH FOUND]")
                                    print(f"File: {file_path}")
                                    print(f"Line {line_num}: {line.strip()}")
                                    print("-" * 50)
                                    match_count += 1
                                    break # Move to next line once a keyword matches
                except Exception as e:
                    # Skip files that cannot be opened (e.g., system locked files)
                    continue

    print(f"=== SCAN COMPLETE ===")
    print(f"Total matching references found: {match_count}")

if __name__ == "__main__":
    # 1. Define where you want to search. 
    # Use '.' for the current folder, or put a full path like 'C:\\Users\\YourName\\Documents'
    target_folder = "." 
    
    # 2. Define the words you are hunting for
    search_terms = ["github", "mario", "email", "wallet", "account"]
    
    scan_local_files(target_folder, search_terms)
