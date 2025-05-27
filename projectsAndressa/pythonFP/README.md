  # PLAYING WWITH IMAGES
    #### Video Demo:  https://youtu.be/Lx5ng5Y8jyo
    #### Description:
    The idea in this project is to submit an image and generate three more images with different filters, as well you can see the analysis of these images in the analysis.csv file.

    The first thing this code does is a validation if the file submitted is a JPG file or not, in case is not, the program displays a message and finished the interaction.
    After it the program validate if the file exists, in case not, a message is displayed and the program is finished.

    After the validation, the program takes the original image and generates new images applying gray, sharp, and edge filters using the Pillow library. These images are saved and can be seen in the image folder. There is a verification in the functions to generate these images to confirm that the images were created; if not, a message is displayed in the prompt.

    To do the image analysis the numpy library was used. Every image name is saved in a array and, using a for loop, any image is analised in brightness, brightness_range, color average and image size.

    This analysis is saved in a .csv file using the function related to csv library.

    The new images and the .csv file with all the analysis can be downloaded from the projects folder.

    ####Step 1:
        Submit a JPG image in the image folder.

    ####Step 2:
        Execute the program and type the image name submitted in the first step.

    ####Step 3:
        Enjoy the results.
