import time

def main():
    while True:
        try:
            # Your main code logic here
            print("The script is running...")
            time.sleep(60)  # Sleep for 60 seconds
        except KeyboardInterrupt:
            print("Script interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(10)  # Wait for a short time before retrying

if __name__ == "__main__":
    main()
