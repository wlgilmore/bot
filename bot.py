import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor pins as output
motor1_pin_forward = 4
motor1_pin_backward = 18
motor2_pin_forward = 17
motor2_pin_backward = 27

GPIO.setup(motor1_pin_forward, GPIO.OUT)
GPIO.setup(motor1_pin_backward, GPIO.OUT)
GPIO.setup(motor2_pin_forward, GPIO.OUT)
GPIO.setup(motor2_pin_backward, GPIO.OUT)

# Set up PWM for motor speed control
motor1_pwm = GPIO.PWM(motor1_pin_forward, 100)
motor2_pwm = GPIO.PWM(motor2_pin_forward, 100)

# Start PWM with 0% duty cycle
motor1_pwm.start(0)
motor2_pwm.start(0)

def move_forward(speed):
    # Set motor 1 to move forward at specified speed
    motor1_pwm.ChangeDutyCycle(speed)
    GPIO.output(motor1_pin_backward, False)
    GPIO.output(motor1_pin_forward, True)
    # Set motor 2 to move forward at specified speed
    motor2_pwm.ChangeDutyCycle(speed)
    GPIO.output(motor2_pin_backward, False)
    GPIO.output(motor2_pin_forward, True)

def move_backward(speed):
    # Set motor 1 to move backward at specified speed
    motor1_pwm.ChangeDutyCycle(speed)
    GPIO.output(motor1_pin_forward, False)
    GPIO.output(motor1_pin_backward, True)
    # Set motor 2 to move backward at specified speed
    motor2_pwm.ChangeDutyCycle(speed)
    GPIO.output(motor2_pin_forward, False)
    GPIO.output(motor2_pin_backward, True)

def stop():
    # Stop both motors
    motor1_pwm.ChangeDutyCycle(0)
    GPIO.output(motor1_pin_forward, False)
    GPIO.output(motor1_pin_backward, False)
    motor2_pwm.ChangeDutyCycle(0)
    GPIO.output(motor2_pin_forward, False)
    GPIO.output(motor2_pin_backward, False)

# Example usage
move_forward(50)
time.sleep(2)
stop()
