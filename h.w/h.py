import os
import platform

def shutdown():
    """
    This function shuts down the computer.
    """
    # Determine the operating system
    os_name = platform.system()
    
    if os_name == "Windows":
        # Shutdown command for Windows
        os.system("shutdown /s /t 1")
    elif os_name == "Linux":
        # Shutdown command for Linux
        os.system("shutdown -h now")
    elif os_name == "Darwin":  # macOS
        # Shutdown command for macOS
        os.system("shutdown -h now")
    else:
        print("Unsupported operating system.")

# Example usage
if __name__ == "__main__":
    print("Shutting down the computer...")
    shutdown()