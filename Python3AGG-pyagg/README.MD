PORT OF PY AGG TO UBUNTU LINUX 16.04

The main features of PyAgg include:

A coordinate aware image. No need for the intricacies of affine matrix transformations, just define the coordinates that make up each corner of your image once, and watch it follow as you resize, crop, rotate, move, and paste the image. Zoom in and out of you coordinate system by bounding box, factor, or units, and lock the aspect ratio to avoid distortions.
Oneliners to easily draw and style high quality graphical elements including polygons with holes, lines with or without smooth curves, pie slices, and point symbols like circles, squares, and triangles with an optional flattening factor.
Style your drawing sizes and distances in several types of units, including pixels, percentages, cm, mm, inches, and font points, by specifying the real world size of your image.
Smart support for text writing, including text anchoring, and automatic detection of available fonts.
Instantly view your image in a Tkinter pop up window, or prepare it for use in a Tkinter application.
There is also support for common domain specific data visualization:

Partial support for geographical plotting, including a lat-long coordinate system, and automatic drawing of GeoJSON features.
Easily plot statistical data on graphs with a syntax and functionality that is aimed more for data analysts and laymen than computer scientists, including linegraph, scatterplot, histogram, etc, although these are still a work in progress.
Platforms



You can get around these limitations by compiling aggdraw on your own, in which case PyAgg should work on any machine that you compile for.

Dependencies

PIL/Pillow (used for image loading, saving, and manipulation. Also used for text-rendering, which means if you compile PIL/Pillow on your own make sure FreeType support is enabled)

Example Usage

Begin by importing the pyagg module:

import pyagg
To begin drawing, create your canvas instance and define its coordinate system, in this case based on percentages to easily draw using relative positions. In our case we give our image the size of an A4 paper, and specify that all further drawing in real world units should use 96 pixels per inch:

canvas = pyagg.Canvas("210mm", "297mm", background=(222,222,222), ppi=96)
canvas.percent_space()
Next, draw some graphical elements:

canvas.draw_line([10,10, 50,90, 90,10],
                 smooth=True,
                 fillcolor=(222,0,0),
                 fillsize="2cm")

canvas.draw_triangle((50,50),fillsize="30px", fillcolor=(0,0,0, 111))
And some text:

canvas.draw_text((50,50),"PyAgg is for drawing!",
                textanchor="center",
                textfont="Segoe UI",
                textsize=42)
Once you are done, view or save your image:

canvas.save("test.png")
canvas.view()
More Information:

The above was just a very small example of what you can do with PyAgg. But until I get around to making the full tutorial just check out the API documentation below.

Credits:

Karim Bahgat (2016)

