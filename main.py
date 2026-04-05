# ==============================================================================
# LEARN IT v13.5.3: THE GLOBAL INTEGRATOR
# Executing 100 Features & 31,500 Data Rows
# ==============================================================================

# THE MAGIC IMPORTS (Connecting your 25 Parts)
import layout
import nursery
import primary
import junior
import senior
import features

class LearnItApp:
    def __init__(self):
        self.version = "13.5.3"
        self.admin_code = "LEARNIT_VIP_2026"
        self.user_status = "DEMO"

    def boot(self):
        # 1. Start with the Layout (Part 1)
        layout.show_splash_screen()
        
        print(f"\n[SYSTEM]: Initializing Learn It v{self.version}...")
        
        # 2. Check for Godly VIP/Admin Access
        code = input("\nENTER VIP/ADMIN CODE: ")
        
        if code == self.admin_code:
            self.user_status = "GODLY_VIP"
            print("👑 VIP STATUS ACTIVATED. ALL 100 FEATURES UNLOCKED.")
            self.run_full_system()
        else:
            print("📱 DEMO MODE ACTIVATED. 50 FEATURES UNLOCKED.")
            self.run_demo_system()

    def run_full_system(self):
        """Executes everything from Part 2 to Part 25."""
        print("\n--- LOADING ALL MODULES ---")
        nursery.load_data()     # Part 2
        primary.load_data()     # Parts 3-6
        junior.load_data()      # Parts 7-11
        senior.load_data()      # Parts 12-18
        
        # Running the 100 VIP Features (Parts 18-25)
        features.execute_vip_matrix()
        
        # Open the Admin Panel (10 On-Panel / 5 Off-Panel Commands)
        features.open_admin_console()

    def run_demo_system(self):
        """Executes only the first 50 features."""
        nursery.load_demo()
        features.execute_demo_matrix()

# --- THE START BUTTON ---
if __name__ == "__main__":
    app = LearnItApp()
    app.boot()
