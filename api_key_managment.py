import os
import sys

def setup_api_key():
    
    #Set up OpenAI API key with other fallback options.
    
    api_key = None
    
    # Check command-line argument
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
        print("API key provided via command line.")
    
    # ELSE check environment variable
    elif os.environ.get("OPENAI_API_KEY"):
        api_key = os.environ.get("OPENAI_API_KEY")
        print("API key found in environment variables.")
    
    # ELSE use a prompt
    else:
        api_key = input("Please enter your OpenAI API key: ")
    
    # Store as environment variable
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        print("API key set successfully!")
        return True
    else:
        print("API key not set.")
        return False

def get_api_key():
    
    #Returns the key if found, None otherwise.
    
    return os.environ.get("OPENAI_API_KEY")

def verify_api_key():
    
    #Verify that the API key is set and accessible.
    
    key = get_api_key()
    if key:
        print(f" API key is set (length: {len(key)} characters)")
        return True
    else:
        print("No API key found")
        return False

#setup when imported
if __name__ == "__main__":
    setup_api_key()
else:
    #verify
    verify_api_key()