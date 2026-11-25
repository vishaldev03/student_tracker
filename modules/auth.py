import os
import getpass
from dotenv import load_dotenv

load_dotenv()

def admin_login():
    """verify admin credentials before allowing access to the main menu."""
    stored_user = os.getenv("ADMIN_USER", "admin")
    stored_pass = os.getenv("ADMIN_PASS", "123")

    attempts = 3
    print("\n====================================================")
    print("                   🔏 ADMIN LOGIN                     ")
    print("=======================================================")

    while attempts > 0:
        username = input("Enter Username:").strip()
        # getpass password ko terminal mein hide rakhna hai
        password = getpass.getpass("Enter password:").strip()

        if username == stored_user and password == stored_pass:
            print("\n✅ login successful ! welcome, admin.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Invalid credentials ! {attempts} attempt(s) remaining.\n")
            else:
                print("\n🚫 maximum login attempts exceeded. Exiting program ...")
                return False
