
def print_colored_background(text, r, g, b):
    '''
        print_colored_background Uses ANSI color codes to print colors to the console.

        NOTE: it seems like it takes a few iterations before the colors show up for some reason.
    '''
    height = 5
    background_color = f"\033[48;2;{r};{g};{b}m"
    reset = "\033[0m"
    row = background_color + "\n"
    print("\n")
    print(text)
    print(f"\tr:{r}\n\tg:{g}\n\tb:{b}")

    for _ in range(height):
        print(row)
    print(reset)

def intensity_to_rgb(color_intensity, r=0, g=0, b=0):
    scaled_intensity = int((color_intensity / 100) * 255)
    return r * scaled_intensity, g * scaled_intensity, b * scaled_intensity

class ConsoleStrategy:
    def __init__(self):
        print("console strategy has been initialized")

    def duty_cycle(self, channel, value):
        self.current_duty_cycle = value
        self.current_channel = channel
        self.render_color()

    def render_color(self):
        color_intensity = int((self.current_duty_cycle / 0xFFFF) * 100)
        if color_intensity > 0 and self.current_channel % 3 == 0:
            r, g, b = intensity_to_rgb(color_intensity, g=1)
            print_colored_background(f"\tintensity: {color_intensity}%", r, g, b)
        if color_intensity > 0 and self.current_channel % 3 == 1:
            r, g, b = intensity_to_rgb(color_intensity, r=1)
            print_colored_background(f"\tintensity: {color_intensity}%", r, g, b)
        if color_intensity > 0 and self.current_channel % 3 == 2:
            r, g, b = intensity_to_rgb(color_intensity, b=1)
            print_colored_background(f"\tintensity: {color_intensity}%", r, g, b)
