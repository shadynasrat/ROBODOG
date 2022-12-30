from legged_gym.pyPS4Controller.controller import Controller
import threading

"""
MIN, MAX: -32767, 32767
"""
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.x = 0
        self.y = 0
        self.hx = 0
        self.hy = 0

    def on_L3_up(self, value):
        self.x = - 2 * value / 32767

        print("on_L3_up: {}".format(self.x))

    def on_L3_down(self, value):
        self.x = - 2 * value / 32767
        print("on_L3_down: {}".format(self.x))

    def on_L3_left(self, value):
        self.y = 2 * value / 32767
        print("on_L3_left: {}".format(self.y))

    def on_L3_right(self, value):
        self.y = 2 * value / 32767
        print("on_L3_right: {}".format(self.y))

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        self.y = 0 
        print("on_L3_y_at_rest")

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        self.x = 0
        print("on_L3_x_at_rest")
    


    def on_R3_up(self, value):
        self.hx = - value/32767
        print("on_R3_up: {}".format(self.hx))

    def on_R3_down(self, value):
        self.hx = - value/32767
        print("on_R3_down: {}".format(self.hx))

    def on_R3_left(self, value):
        self.hy = value/32767
        print("on_R3_left: {}".format(self.hy))

    def on_R3_right(self, value):
        self.hy = value/32767
        print("on_R3_right: {}".format(self.hy))

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        self.hx = 0 
        print("on_R3_y_at_rest")

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        self.hy = 0 
        print("on_R3_x_at_rest")








    
    def on_x_press(self):
        print("on_x_press")

    def on_x_release(self):
        print("on_x_release")

    def on_triangle_press(self):
        print("on_triangle_press")

    def on_triangle_release(self):
        print("on_triangle_release")

    def on_circle_press(self):
        print("on_circle_press")

    def on_circle_release(self):
        print("on_circle_release")

    def on_square_press(self):
        print("on_square_press")

    def on_square_release(self):
        print("on_square_release")

    def on_L1_press(self):
        print("on_L1_press")

    def on_L1_release(self):
        print("on_L1_release")

    def on_L2_press(self, value):
        print("on_L2_press: {}".format(value))

    def on_L2_release(self):
        print("on_L2_release")

    def on_R1_press(self):
        print("on_R1_press")

    def on_R1_release(self):
        print("on_R1_release")

    def on_R2_press(self, value):
        print("on_R2_press: {}".format(value))

    def on_R2_release(self):
        print("on_R2_release")

    def on_up_arrow_press(self):
        print("on_up_arrow_press")

    def on_up_down_arrow_release(self):
        print("on_up_down_arrow_release")

    def on_down_arrow_press(self):
        print("on_down_arrow_press")

    def on_left_arrow_press(self):
        print("on_left_arrow_press")

    def on_left_right_arrow_release(self):
        print("on_left_right_arrow_release")

    def on_right_arrow_press(self):
        print("on_right_arrow_press")

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_L3_press")

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_L3_release")

    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        print("on_R3_press")

    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        print("on_R3_release")

    def on_options_press(self):
        print("on_options_press")

    def on_options_release(self):
        print("on_options_release")

    def on_share_press(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_share_press")

    def on_share_release(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_share_release")

    def on_playstation_button_press(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_playstation_button_press")

    def on_playstation_button_release(self):
        """this event is only detected when connecting without ds4drv"""
        print("on_playstation_button_release")
    
controller = MyController(interface="/dev/input/js1", connecting_using_ds4drv=False)
thread = threading.Thread(target=controller.listen, args=(1200,))
thread.setDaemon(True)
thread.start()
print("another thread")
