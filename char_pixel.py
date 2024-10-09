from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class PixelMatrixApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Generate the pixel matrix for the letter "A"
        pixel_matrix = self.generate_pixel_matrix('ॐ')

        # Print the pixel matrix
        for row in pixel_matrix:
            print(' '.join(str(val) for val in row))

        return layout

    def generate_pixel_matrix(self, char, size=(16, 16)):
        # Create a blank image with a white background
        image = Image.new('L', size, color=255)  # 'L' mode for grayscale

        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", 16)  # You may need to provide a valid font path
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font

        # Draw the character on the image
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), char, font=font, fill=0)  # Fill with black color

        # Convert image to a NumPy array
        pixel_array = np.array(image)

        # Convert to a binary matrix: 1 for black, 0 for white
        pixel_matrix = (pixel_array < 128).astype(int)

        return pixel_matrix

if __name__ == '__main__':
    PixelMatrixApp().run()
