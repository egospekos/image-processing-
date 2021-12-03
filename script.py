
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFile
import PIL
import numpy
from numpy import *
import skimage
from skimage.transform import rescale, resize, downscale_local_mean, rotate, swirl
from skimage import data, io, filters
from skimage.exposure import rescale_intensity
from skimage import data, io
import matplotlib.pyplot as plt
import matplotlib






#######################
## F U N C T I O N S ##
#######################

images_width = 300
images_height = 300
image_1_name = "Load"
image_2_name = "Save"
histogram_1_name = "Histogram"
histogram_2_name = "Thresholding"
enchantment_1_name = "Meijering"
enchantment_2_name = "Laplace"
enchantment_3_name = "Gaus"
enchantment_4_name = "Hessian"
enchantment_5_name = "Difference of gaussians"
enchantment_6_name = "Prewitt"
enchantment_7_name = "Unsharp Mask"
enchantment_8_name = "Hysteresis threshold"
enchantment_9_name = "Sobel"
enchantment_10_name = "Scharr"
spatial_1_name = "Rescaling"
spatial_2_name = "Cropping"
spatial_3_name = "Rotation"
spatial_4_name = "Swirling"
spatial_5_name = "Resizing"
density_1_name = "Density"
morphological_1_name = "Blacktophat"
morphological_2_name = "Whitetophat"
morphological_3_name = "Erosion"
morphological_4_name = "Skeletonize"
morphological_5_name = "Dilaton"
morphological_6_name = "Closing"
morphological_7_name = "Opening"
morphological_8_name = "Medial_axis"
morphological_9_name = "Watershed"
morphological_10_name = "Thin"


# image funcs


def image_1():
    # image load
    global right_image,left_image,previous_image

    selected_image = filedialog.askopenfile()
    temp_image = Image.open(selected_image.name)

    
    right_image = temp_image
    left_image = temp_image
    previous_image = temp_image
   
    _image = temp_image.resize((images_width, images_height), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    image_label_left.configure(image=_image)
    image_label_left.image = _image
    image_label_left.place(x=95, rely=0)
    image_label_right.configure(image=_image)
    image_label_right.image = _image
    image_label_right.place(x=475, rely=0)
    
    logEnd(image_1_name + " (" + selected_image.name + ")")


def image_2():
    # image save
    logStart(image_2_name)

    
    image_path = filedialog.asksaveasfilename()

    right_image.save(image_path, "JPEG", quality=80, optimize=True, progressive=True)

    logEnd(image_2_name)


# enchantment funcs

def enchantment_1():
    # meijering
    logStart(enchantment_1_name)

    image = numpy.asarray(right_image, numpy.uint8)

    updated_image = skimage.filters.meijering(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)

    logEnd(enchantment_1_name)


def enchantment_2():
    # Laplace
    logStart(enchantment_2_name)

    image = numpy.asarray(right_image, numpy.uint8)

    updated_image = skimage.filters.laplace(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)

    logEnd(enchantment_2_name)


def enchantment_3():
    # Gaus
    logStart(enchantment_3_name)
    image = numpy.asarray(right_image, numpy.uint8)

    updated_image = skimage.filters.gaussian(image, sigma=1)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(enchantment_3_name)


def enchantment_4():
    # Hessian
    logStart(enchantment_4_name)
    image = numpy.asarray(right_image, numpy.uint8)

    updated_image = skimage.filters.hessian(image, sigmas=1)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(enchantment_4_name)


def enchantment_5():
    # difference_of_gaussians
    logStart(enchantment_5_name)

    image = numpy.asarray(right_image, numpy.uint8)
    updated_image = skimage.filters.difference_of_gaussians(image, low_sigma=1)
    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))
    reloadImage(updated_image)

    logEnd(enchantment_5_name)


def enchantment_6():
    # Prewitt
    logStart(enchantment_6_name)
    image = numpy.asarray(right_image, numpy.uint8)

    updated_image = skimage.filters.prewitt(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))
    reloadImage(updated_image)
    logEnd(enchantment_6_name)


def enchantment_7():
    # Unsharp Mask
    logStart(enchantment_7_name)

    image = numpy.asarray(right_image, numpy.uint8)

    # image = skimage.color.rgb2gray(image)

    updated_image = filters.unsharp_mask(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(enchantment_7_name)


def enchantment_8():
    # hysteresis_threshold
    logStart(enchantment_8_name)

    image = numpy.asarray(right_image, numpy.uint8)
    updated_image = skimage.filters.apply_hysteresis_threshold(image, 1.5, 2.5)
    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))
    reloadImage(updated_image)

    logEnd(enchantment_8_name)


def enchantment_9():
    # Sobel
    logStart(enchantment_9_name)

    image = numpy.asarray(right_image, numpy.uint8)
    updated_image = skimage.filters.sobel(image)
    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))
    reloadImage(updated_image)

    logEnd(enchantment_9_name)


def enchantment_10():
    # Scharr
    logStart(enchantment_10_name)

    image = numpy.asarray(right_image, numpy.uint8)
    updated_image = skimage.filters.scharr(image)
    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))
    reloadImage(updated_image)

    logEnd(enchantment_10_name)


# histogram funcs
def histogram_1():
    logStart(histogram_1_name)
    

    image = numpy.asarray(right_image, numpy.uint8)

    image = numpy.asarray(image, numpy.uint8)

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 8))

    for c, c_color in enumerate(('red', 'green', 'blue')):
        img_hist, bins = skimage.exposure.histogram(image[..., c], source_range='dtype')
        axes[c].plot(bins, img_hist)
        axes[c].set_ylabel(c_color)

    fig.canvas.draw()
    updated_image = PIL.Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())

    reloadImage(updated_image)

    logEnd(histogram_1_name)


def histogram_2():
    # threshold
    logStart(histogram_2_name)

    image = numpy.asarray(right_image, numpy.uint8)
    I_eq = skimage.exposure.equalize_hist(image)
    I_eq = Image.fromarray((I_eq * 255).astype(numpy.uint8))
    reloadImage(I_eq)

    logEnd(histogram_2_name)


# spatial funcs
def spatial_1():
    # rescaling
    logStart(spatial_1_name)

    def inner():
        image = numpy.asarray(right_image, numpy.uint8)
        image_array = numpy.array(image)

        rescaled_image = rescale(image_array, float(parameter_entry_1.get()), anti_aliasing=False)

        rescaled_image = Image.fromarray((rescaled_image * 255).astype(numpy.uint8))
        reloadImage(rescaled_image)
        parameter_entry_1.pack_forget()
        parameter_button.pack_forget()
        logEnd(spatial_1_name)

    parameter_button.configure(text="Rescale value", command=inner)

    parameter_entry_1.pack()

    parameter_button.pack()


def spatial_2():
    # Cropping
    logStart(spatial_2_name)

    def inner():
        image = numpy.asarray(right_image, numpy.uint8)
        cropped_image = image[int(parameter_entry_1.get()):int(parameter_entry_2.get()),
                        int(parameter_entry_3.get()):int(parameter_entry_4.get())]
        cropped_image = Image.fromarray(cropped_image)
        reloadImage(cropped_image)
        parameter_entry_1.pack_forget()
        parameter_entry_2.pack_forget()
        parameter_entry_3.pack_forget()
        parameter_entry_4.pack_forget()
        parameter_button.pack_forget()
        logEnd(spatial_2_name)

    parameter_button.configure(text="Order: y1,y2,x1,x2", command=inner)

    parameter_entry_1.pack()
    parameter_entry_2.pack()
    parameter_entry_3.pack()
    parameter_entry_4.pack()
    parameter_button.pack()


def spatial_3():
    # rotation
    logStart(spatial_3_name)

    def inner():
        image = numpy.asarray(right_image, numpy.uint8)

        rotated_image = rotate(image, int(parameter_entry_1.get()), resize=False)

        rotated_image = Image.fromarray((rotated_image * 255).astype(numpy.uint8))

        reloadImage(rotated_image)
        parameter_entry_1.pack_forget()
        parameter_button.pack_forget()
        logEnd(spatial_3_name)
        

    parameter_button.configure(text="Rotation value: ", command=inner)

    parameter_entry_1.pack()

    parameter_button.pack()


def spatial_4():
    # Swirling
    logStart(spatial_4_name)

    def inner():
        image = numpy.asarray(right_image, numpy.uint8)

        swirled = swirl(image, rotation=int(parameter_entry_1.get()),
                        strength=int(parameter_entry_2.get()),
                        radius=int(parameter_entry_3.get()))

        img = Image.fromarray((swirled * 255).astype(numpy.uint8))

        reloadImage(img)
        parameter_entry_1.pack_forget()
        parameter_entry_2.pack_forget()
        parameter_entry_3.pack_forget()

        parameter_button.pack_forget()
        logEnd(spatial_4_name)

    parameter_button.configure(text="Rotation,Strength,Radius", command=inner)

    parameter_entry_1.pack()
    parameter_entry_2.pack()
    parameter_entry_3.pack()

    parameter_button.pack()


def spatial_5():
    # Resizing
    def inner():
        logStart(spatial_5_name)
        image = numpy.asarray(right_image, numpy.uint8)
        

        resized_image = resize(image, (image.shape[0] // int(parameter_entry_1.get()),
                                       image.shape[1] // int(parameter_entry_2.get())),
                               anti_aliasing=True)
        resized_image = Image.fromarray((resized_image * 255).astype(numpy.uint8))

        reloadImage(resized_image)
        parameter_entry_1.pack_forget()
        parameter_entry_2.pack_forget()

        parameter_button.pack_forget()
        logEnd(spatial_5_name)

    parameter_button.configure(text="X Value,Y Value", command=inner)

    parameter_entry_1.pack()
    parameter_entry_2.pack()

    parameter_button.pack()


# density funcs
def density_1():
    # density
    logStart(density_1_name)

    def inner():
        image = numpy.asarray(right_image, numpy.uint8)
        updated_image = rescale_intensity(image, in_range=(int(parameter_entry_1.get()), int(parameter_entry_2.get())))

        updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

        reloadImage(updated_image)
        parameter_entry_1.pack_forget()
        parameter_entry_2.pack_forget()
        parameter_button.pack_forget()
        logEnd(density_1_name)

    parameter_button.configure(text="Min Value,Max Value", command=inner)

    parameter_entry_1.pack()
    parameter_entry_2.pack()

    parameter_button.pack()


# morphological funcs
def morphological_1():
    # blacktophat
    logStart(morphological_1_name)
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.black_tophat(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_1_name)


def morphological_2():
    # Whitetophat
    logStart(morphological_2_name)
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.white_tophat(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_2_name)


def morphological_3():
    logStart(morphological_3_name)
    # Erosion
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.erosion(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_3_name)


def morphological_4():
    logStart(morphological_4_name)
    # Skeletonize
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.skeletonize(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_4_name)


def morphological_5():
    logStart(morphological_5_name)
    # Dilation
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.dilation(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_5_name)


def morphological_6():
    logStart(morphological_6_name)
    # Closing
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.closing(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_6_name)


def morphological_7():
    logStart(morphological_7_name)
    # Opening
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.opening(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_7_name)


def morphological_8():
    logStart(morphological_8_name)
    # Medial_axis
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.medial_axis(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_8_name)


def morphological_9():
    logStart(morphological_9_name)
    # Watershed
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.watershed(image)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_9_name)


def morphological_10():
    logStart(morphological_10_name)
    # Thin
    image = numpy.asarray(right_image, numpy.uint8)

    image = skimage.color.rgb2gray(image)

    updated_image = skimage.morphology.thin(image, 128)

    updated_image = Image.fromarray((updated_image * 255).astype(numpy.uint8))

    reloadImage(updated_image)
    logEnd(morphological_10_name)


def logStart(option_name):
    global previous_image
    global right_image
    global left_image
    log = option_name + " is being processing..."
    print(log)
    previous_image = right_image
    right_image = left_image
    log_text_label.configure(text=log)


def logEnd(option_name):
    log = option_name + " has been done."
    print(log)
    log_text_label.configure(text=log)


def reloadImage(_image, reloadBoth=False):
    global right_image
    right_image = _image
    # resize
    _image = _image.resize((images_width, images_height), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    image_label_right.configure(image=_image)
    image_label_right.image = _image
    image_label_right.place(x=475, rely=0)
    if reloadBoth:
        image_label_left.configure(image=_image)
        image_label_left.image = _image
        image_label_left.place(x=95, rely=0)


def undo_image():
    reloadImage(previous_image)
    log_text_label.configure(text="Undo")
    print("Undo")


def log_cleaner():
    log_text_label.configure(text="")


def exit():
    master.destroy()


#################################
## U S E R * I N T E R F A C E ##
#################################

master = Tk()
master.title("Görüntü İşleme")
canvas = Canvas(master, height=500, width=900)
master.resizable(False, False)
canvas.pack()

frame_image_viewer = Frame(master, bg='#00d8e6')
frame_image_viewer.place(x=0, y=0, relwidth=1, relheight=1)
image_label_left = Label(frame_image_viewer)
image_label_left.place(x=20, y=0)
image_label_right = Label(frame_image_viewer)
image_label_right.place(x=290, y=0)
log_text_label = Label(frame_image_viewer, text="Programımıza hoş geldiniz...")
log_text_label.config(font=("Courier", 10))

log_text_label.place(x=90, y=400)

## parameter entries
parameter_entry_1 = Entry(master)
parameter_entry_2 = Entry(master)
parameter_entry_3 = Entry(master)
parameter_entry_4 = Entry(master)
parameter_button = Button(master, text="Boş")

# menu
_menu = Menu(master)
master.config(menu=_menu)

# menu submenus
image_menu = Menu(_menu)
_menu.add_cascade(label='Image', menu=image_menu)

enchantment_menu = Menu(_menu)
_menu.add_cascade(label='Enchantment', menu=enchantment_menu)

histogram_menu = Menu(_menu)
_menu.add_cascade(label='Histogram', menu=histogram_menu)

spatial_menu = Menu(_menu)
_menu.add_cascade(label='Spatial Transform', menu=spatial_menu)

density_menu = Menu(_menu)
_menu.add_cascade(label='Density Conversion', menu=density_menu)

morphological_menu = Menu(_menu)
_menu.add_cascade(label='Morphological', menu=morphological_menu)

system_menu = Menu(_menu)
_menu.add_cascade(label='System', menu=system_menu)

# opening

temp_image = Image.fromarray(data.camera())
right_image = temp_image
left_image = temp_image
previous_image = temp_image
print("It's working!")
print(right_image)
reloadImage(right_image, True)

# image submenu
image_menu.add_command(label=image_1_name, command=image_1)
image_menu.add_command(label=image_2_name, command=image_2)

# histogram submenu
histogram_menu.add_command(label=histogram_1_name, command=histogram_1)
histogram_menu.add_command(label=histogram_2_name, command=histogram_2)

# enchantment submenu
enchantment_menu.add_command(label=enchantment_1_name, command=enchantment_1)
enchantment_menu.add_command(label=enchantment_2_name, command=enchantment_2)
enchantment_menu.add_command(label=enchantment_3_name, command=enchantment_3)
enchantment_menu.add_command(label=enchantment_4_name, command=enchantment_4)
enchantment_menu.add_command(label=enchantment_5_name, command=enchantment_5)
enchantment_menu.add_command(label=enchantment_6_name, command=enchantment_6)
enchantment_menu.add_command(label=enchantment_7_name, command=enchantment_7)
enchantment_menu.add_command(label=enchantment_8_name, command=enchantment_8)
enchantment_menu.add_command(label=enchantment_9_name, command=enchantment_9)
enchantment_menu.add_command(label=enchantment_10_name, command=enchantment_10)

# spatial submenu
spatial_menu.add_command(label=spatial_1_name, command=spatial_1)
spatial_menu.add_command(label=spatial_2_name, command=spatial_2)
spatial_menu.add_command(label=spatial_3_name, command=spatial_3)
spatial_menu.add_command(label=spatial_4_name, command=spatial_4)
spatial_menu.add_command(label=spatial_5_name, command=spatial_5)

# density submenu
density_menu.add_command(label=density_1_name, command=density_1)

# morphological submenu
morphological_menu.add_command(label=morphological_1_name, command=morphological_1)
morphological_menu.add_command(label=morphological_2_name, command=morphological_2)
morphological_menu.add_command(label=morphological_3_name, command=morphological_3)
morphological_menu.add_command(label=morphological_4_name, command=morphological_4)
morphological_menu.add_command(label=morphological_5_name, command=morphological_5)
morphological_menu.add_command(label=morphological_6_name, command=morphological_6)
morphological_menu.add_command(label=morphological_7_name, command=morphological_7)
morphological_menu.add_command(label=morphological_8_name, command=morphological_8)
morphological_menu.add_command(label=morphological_9_name, command=morphological_9)
morphological_menu.add_command(label=morphological_10_name, command=morphological_10)

# system alt submenu
system_menu.add_command(label="Undo", command=undo_image)
system_menu.add_command(label="Clear log", command=log_cleaner)
system_menu.add_command(label="Exit", command=exit)

master.mainloop()