import fitz
from PIL import Image
import io
import math


def to_1280_format(h, w):
    # Return pixel numbers for crop
    return (w * 1280, h * 1280, (w + 1) * 1280, (h + 1) * 1280)


class Convert_pdf:
    def __init__(self, path_pdf):
        self.path_pdf = path_pdf

        self.pdf_list = list(self.path_pdf.glob("**/*.pdf"))

        if not self.pdf_list:
            raise FileNotFoundError("No PDF files found in the specified path.")
        self.doc = fitz.open(self.pdf_list[0])
        self.page = self.doc.load_page(0)
        self.pixmap = self.page.get_pixmap(dpi=300)

    def return_pixmap(self):
        return self.pixmap.tobytes("jpg")

    def return_image(self):
        return Image.open(io.BytesIO(self.pixmap))

    def save_image(self, export_path):
        export_path = export_path / "{0}.jpg".format(self.pdf_list[0].name)
        self.pixmap.save(export_path)
        return export_path


def crop_image(
    path_pdf,
    path_convert_pdf,
    bytes_image,
    hight_pixels: int = 0,
    width_pixels: int = 0,
):
    jpg_list = list(path_pdf.glob("**/*.pdf"))

    img = Image.open(io.BytesIO(bytes_image))
    w, h = img.size

    w_crop_iterations = math.ceil(w / 1280)
    h_crop_iterations = math.ceil(h / 1280)
    for h_multiplication in range(0, h_crop_iterations):
        for w_multiplication in range(0, w_crop_iterations):
            crop_area = to_1280_format(h_multiplication, w_multiplication)

            # Crop image
            img_crop = img.crop(crop_area)

            # Resize to 1280x1280 format
            img_crop.thumbnail((width_pixels, hight_pixels))
            crop_save = path_convert_pdf / "{}_{}_{}.jpg".format(
                jpg_list[0].stem, h_multiplication, w_multiplication
            )
            img_crop.save(crop_save)
