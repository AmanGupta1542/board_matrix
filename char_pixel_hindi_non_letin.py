from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class PixelMatrixApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Generate the pixel matrix for the symbol ॐ (or any other non-Latin character)
        pixel_matrix = self.generate_pixel_matrix('ॐ', font_path="languages/hindi_Devanagari/NotoSansDevanagari-Regular.ttf")

        # Print the pixel matrix
        for row in pixel_matrix:
            print(' '.join(str(val) for val in row))

        return layout

    def generate_pixel_matrix(self, char, size=(16, 16), font_path="languages/hindi_Devanagari/NotoSansDevanagari-Regular.ttf"):
        # Create a blank image with a white background
        image = Image.new('L', size, color=255)  # 'L' mode for grayscale

        # Load the appropriate font
        try:
            font = ImageFont.truetype(font_path, 16)  # Provide the valid path to the font
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font (but might not work for non-Latin scripts)

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
