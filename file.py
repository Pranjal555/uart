import serial
import time

# Define the serial port and baud rate
serial_port = '/dev/ttyUSB1'  # Change this to the correct UART port
baud_rate = 115200

try:
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Connected to {serial_port} at {baud_rate} baud")

    while True:
        # Send "Hello" over UART
        ser.write(b"Hello\n")
        print("Sent: Hello")

        # Read incoming data (if any)
        received_data = ser.readline()
        if received_data:
            print(f"Received: {received_data.decode().strip()}")

        # Wait for 1 second before sending again
        time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    # Close the serial port when done
    ser.close()
