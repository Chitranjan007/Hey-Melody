import speedtest
import pyttsx3

# Initialize the speedtest-cli
speedtester = speedtest.Speedtest()

# Define the voice assistant
assistant = pyttsx3.init()

def internet_speed_test():
    # Perform the speed test
    download_speed = speedtester.download() / 1024 / 1024
    upload_speed = speedtester.upload() / 1024 / 1024

    # Convert speeds to Mbps
    download_speed_mbps = "{:.2f}".format(download_speed)
    upload_speed_mbps = "{:.2f}".format(upload_speed)

    # Speak the results
    assistant.say(f"My current internet download speed is {download_speed_mbps} Mbps, and upload speed is {upload_speed_mbps} Mbps.")
    assistant.runAndWait()

if __name__ == "__main__":
    internet_speed_test()
