import image, cmd
class CanvasShelle(cmd.Cmd):
   def convertBlackWhite(self, arg):
        grayscale_image = image.EmptyImage(arg.getWidth(), arg.getHeight())

        for col in range(input_image.getWidth()):
            for row in range(input_image.getHeight()):
                p = input_image.getPixel(col, row)

                red = p.getRed()
                green = p.getGreen()
                blue = p.getBlue()

                avg = (red + green + blue) / 3.0

                newpixel = image.Pixel(avg, avg, avg)
                grayscale_image.setPixel(col, row, newpixel)

        blackwhite_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
        for col in range(input_image.getWidth()):
            for row in range(input_image.getHeight()):
                p = grayscale_image.getPixel(col, row)
                red = p.getRed()
                if red > 140:
                    val = 255
                else:
                    val = 0

                newpixel = image.Pixel(val, val, val)
                blackwhite_image.setPixel(col, row, newpixel)
        return blackwhite_image

