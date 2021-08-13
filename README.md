IRIS
====

Python implementation of human eye IRIS Segmentation Algorithm based on Daugman's Integro-Differential Operator.

# Data Set
Used data requires permission of provider. Can be [downloaded](http://iris.di.ubi.pt/index_arquivos/Page374.html) after password acquired. There are 3 different ZIP files in UBIRIS.v1 and the used one is consist of 200 x 150 - Grayscale images inside file named 'UBIRIS_200_150_R'.

# Segmentation
Iris contains rich information that is spesific to the person and it is one of the most important biometric approaches that can perform high confidence recognition. There are sill commercial iris recognition systems are using the Daugman algorithm. 

Daugman algorithm:

![daugman](https://user-images.githubusercontent.com/88535469/129375818-18b668a4-230a-45bd-be7a-5317c023a7a7.jpg)

`where I(x,y) is the eye image, r is the radius to search over the image (x,y), G(r) is a Gaussian smoothing function. The algorithm starts to search from the pupil, in order to detect the changes of maximum pixel values (partial derivative).`

In our test images, it is noticed sometimes it might not be easy to detect iris and pupils because eyelids can be almost closed in some cases. To solve this issue, instead of going full circular as it is done in classic algorithm. We can use only the left and right side of the eye in a way that so our partial derivative will not detect wrong shapes as an iris. To do this, we made modifications to regular Bresenham Method and discarded 4 of the rotating lines.

![search_zone](https://user-images.githubusercontent.com/88535469/129375625-668dee33-0039-44c3-80de-6f4b4b530849.png)

To see the difference lets check on worst 20 images(decided by sorting maximum partial derivative values for each image from lowest to highest and taking 20 images with lowest values) from full circle and half circle.

# First image is with full circular search:
![worst_20](https://user-images.githubusercontent.com/88535469/129377967-8e8d4834-ca0c-465e-b2f8-0a6310611153.png)

<br>

# Second image is with half circular search:
![worst_20_2](https://user-images.githubusercontent.com/88535469/129378138-c600edd2-32b5-4078-b9a6-4c0033cb35fb.png)

