import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
import numpy as np

class PixelMatrixApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a label with a fixed size (16x16) and the character "A"
        self.label = Label(text='A', font_size=16, size_hint=(None, None), size=(16, 16))
        layout.add_widget(self.label)

        # Button to trigger matrix generation
        self.label.bind(texture=self.on_texture_ready)
        
        return layout
    
    def on_texture_ready(self, instance, value):
        # Access the texture of the label (it contains pixel data)
        texture = self.label.texture

        # Get the raw image data from the texture
        pixel_data = texture.pixels
        
        # Convert the pixel data to a NumPy array
        # Each pixel has 4 channels (RGBA), but we only need the first one (R channel)
        width, height = texture.size
        pixel_array = np.frombuffer(pixel_data, dtype=np.uint8).reshape((height, width, 4))
        
        # Convert to a binary matrix based on whether the pixel is black or white
        pixel_matrix = np.zeros((height, width), dtype=int)
        
        for i in range(height):
            for j in range(width):
                # Check the red channel to determine if the pixel is part of the character (black) or background (white)
                r, g, b, a = pixel_array[i, j]
                if r == 0 and g == 0 and b == 0:  # If it's black (RGB = 0,0,0), mark as 1
                    pixel_matrix[i, j] = 1
                else:
                    pixel_matrix[i, j] = 0
        
        # Print the pixel matrix (1 for black, 0 for white)
        for row in pixel_matrix:
            print(' '.join(str(val) for val in row))

if __name__ == '__main__':
    PixelMatrixApp().run()
