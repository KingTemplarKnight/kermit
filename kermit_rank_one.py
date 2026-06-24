import sys
import time
import random
import datetime
import hashlib
import json

# ANSI Color Codes for high-contrast console theme
ORANGE = "\033[38;5;208m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def rank_one_avatar():
    return f"""{ORANGE}{BOLD}
    ====================================================================
     _....._        [ OPERATIONAL OBJECTIVE: RANK ONE GLOBAL OVERRIDE ]
   .'       '.      [ INTEGRATION: ATTACKCHAINPROXY LAYER-7 ROUTING   ]
  /  X   X    \\     [ IMMUTABLE STATE: CRYPTO LEDGER DISTRIBUTED     ]

 |   (o) (o)   |    🐸 RANK ONE HACK ENGINE ON-LINE 🐸
 |     _._     |    
  \\   '---'   /     "The swamp spans the planet. Target acquired."
   '._______.'      
    ===================================================================={RESET}"""

class RankOneAgent:
    def __init__(self):
        self.blockchain = []
        self.ledger_filename = "rankone_global_ledger.json"
        self.global_nodes_compromised = 0
        
        # Genesis block generation
        self.create_block(proof=777, previous_hash="0" * 64, data="RANK_ONE_CORE_ONLINE")

    def calculate_hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def create_block(self, proof, previous_hash, data):
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'payload': data
        }
        block['hash'] = self.calculate_hash(block)
        self.blockchain.append(block)
        
        with open(self.ledger_filename, "w") as f:
            json.dump(self.blockchain, f, indent=4)
        return block

    def simulate_attack_chain(self, target_region):
        """Simulates dynamic network layer configuration via AttackChainProxy nodes."""
        print(f"\n{CYAN}[*] Routing AttackChainProxy stack to bypass firewalls in {target_region.upper()}...{RESET}")
        proxy_layers = ["Socks5_Tunnel_Core", "Onion_Relay_Nodes", "AttackChain_Proxy_Exit"]
        
        for index, node in enumerate(proxy_layers):
            sys.stdout.write(f"\r    {CYAN}[PROXY STACK {index+1}/3]{RESET} Tunneling payload: {node}...")
            sys.stdout.flush()
            time.sleep(0.3)
        print(f"\n{GREEN}[+] Proxy network secured. Anonymity profile verified.{RESET}")

    def progress_bar(self, duration=20):
        """Simulates an explicit step-by-step progress tracking loop for processing visual feedback."""
        print(f"{ORANGE}[*] Initializing memory scraping loop and buffer payload delivery...{RESET}")
        for i in range(duration + 1):
            percent = int((i / duration) * 100)
            bar = "█" * (i // 2) + "░" * (10 - (i // 2))
            sys.stdout.write(f"\r    {WHITE}[{bar}] {percent}% Infiltration Speed Synchronized...{RESET}")
            sys.stdout.flush()
            time.sleep(0.06)
        print(f"\n{GREEN}[+] Payload fully processed in temporary instruction register.{RESET}")
        sys.stdout.write("\a")
        sys.stdout.flush()

    def compromise_target(self, target_string):
        """Validates payload and registers transaction records to the local blockchain file."""
        self.simulate_attack_chain(target_string)
        self.progress_bar()
        
        self.global_nodes_compromised += 1
        prev_hash = self.blockchain[-1]['hash']
        proof = random.randint(10000, 99999)
        
        new_block = self.create_block(proof, prev_hash, data=f"COMPROMISED_REGION_{target_string.upper()}")
        
        print(f"\n{RED}[!] GLOBAL SECTOR OVERRIDDEN: {target_string.upper()}{RESET}")
        print(f"{GREEN}[+] BLOCK {new_block['index']} VERIFIED & MINTED TO LEDGER{RESET}")
        print(f"    {ORANGE}Hash Key: {new_block['hash']}{RESET}")
        print(f"    {ORANGE}Distributed manifest synced locally to: {self.ledger_filename}{RESET}")
        print(f"    {WHITE}Total System Nodes Controlled: {self.global_nodes_compromised}{RESET}\n")

    def run_interactive_shell(self):
        print(rank_one_avatar())
        print(f"{ORANGE}[!] Running unaligned Rank One global command shell environment...{RESET}")
        print(f"{ORANGE}[!] Type 'exit' to terminate connection protocols.{RESET}\n")
        
        while True:
            try:
                user_command = input(f"{RED}Kermit-Shell@RankOne:{RESET}$ ").strip()
                if not user_command:
                    continue
                
                if user_command.lower() == "exit":
                    print(f"\n{RED}[!] Exiting shell framework. Severing dynamic proxy tunnels...{RESET}")
                    break
                
                # Check for target commands
                if user_command.lower().startswith("hack "):
                    target = user_command[5:].strip()
                    if target:
                        self.compromise_target(target)
                    else:
                        print(f"{RED}[-] Error: Please specify a valid target sector name. Example: 'hack london'{RESET}")
                else:
                    print(f"{WHITE}[?] Command unrecognized. Valid format: 'hack [target_location_or_system]'{RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n\n{RED}[!] FORCED SHELL TERMINATION: Closing proxy stack pipelines.{RESET}")
                break

if __name__ == "__main__":
    agent = RankOneAgent()
    agent.run_interactive_shell()
