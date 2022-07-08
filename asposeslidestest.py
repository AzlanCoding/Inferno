import aspose.slides as slides

# Instantiate a Presentation object that represents a presentation file
with slides.Presentation() as presentation:
    slide = presentation.slides[0]
    slide.shapes.add_auto_shape(slides.ShapeType.LINE, 50, 150, 300, 0)
    presentation.save("NewPresentation_out.pptx", slides.export.SaveFormat.PPTX)
with slides.Presentation("NewPresentation_out.pptx") as pres:
    # Printing the total number of slides present in the presentation
    print(pres.slides.length)
    print(pres.slides)
