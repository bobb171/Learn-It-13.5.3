# ==============================================================================
# LEARN IT v13.5.2: THE ENGINE WAREHOUSE
# REQUIREMENTS & INSTALLATION GUIDE (FOR TERMINAL)
# ==============================================================================
"""
COMMANDS TO INITIALIZE THE SYSTEM:
1. pip install kivy
2. pip install kivy[base] kivy_examples
3. pip install buildozer (For APK Generation)
4. pip install pillow (For UI Images/Icons)
"""

class GlobalData:
    def __init__(self):
        # THE LIBRARY MANIFEST (v13.5.2)
        self.requirements = ["kivy", "kivy[base]", "sqlite3", "pillow"]
        
        # --- NIGERIA ACADEMIC BANK (1986 - 2026) ---
        self.biology_notes = [
            "1. Intro: Biology is the study of life...",
            "2. MR NIGER D: Movement, Respiration, Nutrition..."
        ]
        
        # --- UK ACADEMIC BANK (GCSE/A-LEVEL) ---
        self.uk_math = ["Algebra", "Geometry", "Calculus"]

        # --- ADMIN SETTINGS ---
        self.admin_key = "qwerty"
        self.vip_key = "5000"
