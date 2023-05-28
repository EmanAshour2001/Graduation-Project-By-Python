#this_file_created_by_Taimaa_ELkahlout

import cv2
img = cv2.imread('8iAb9k4aT.jpg')
plt.imshow(img)
plt.show()

img = cv2.imread('154006829.jpg')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

resize = tf.image.resize(img, (256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()

np.expand_dims(resize,0)
np.expand_dims(resize,0).shape
yhat = model.predict(np.expand_dims(resize/255, 0))
#here you shout but 0.4 so I will change it
if yhat > 0.4: 
    print(f'Predicted class is Sad')
else:
    print(f'Predicted class is Happy')
