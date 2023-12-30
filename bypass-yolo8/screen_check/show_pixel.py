from PIL import Image, ImageTk, ImageDraw
import tkinter as tk


class ImageWithGridApp:
    def __init__(self, master, image_path):
        self.master = master
        self.master.title("Image with Grid and Hover Coordinates")
        # Load the original image
        self.original_image = Image.open(image_path)
        self.width, self.height = self.original_image.size
        # Set the grid spacing
        self.grid_spacing = 30
        # Create a copy of the original image to draw on
        self.image = self.original_image.copy()
        self.draw = ImageDraw.Draw(self.image)
        # Create a Tkinter PhotoImage from the image with grid
        self.tk_image = ImageTk.PhotoImage(self.image)
        # Create a Canvas to display the image
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack()
        # Display the image with grid on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        # Bind the motion event to update hover coordinates
        self.canvas.bind("<Motion>", self.update_hover_coordinates)

    def update_hover_coordinates(self, event):
        x, y = event.x, event.y
        grid_x = (x // self.grid_spacing) * self.grid_spacing
        grid_y = (y // self.grid_spacing) * self.grid_spacing
        self.master.title(f"Hover Coordinates: ({x}, {y}) | Grid Coordinates: ({grid_x}, {grid_y})")


if __name__ == "__main__":
    image_path = "./todo/14.PNG"
    root = tk.Tk()
    app = ImageWithGridApp(root, image_path)
    root.mainloop()
