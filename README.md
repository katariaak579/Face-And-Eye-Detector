# Face-And-Eye-Detector

It is an openCV project that use CascadeClassifier and Haarcascades to detect faces and eyes. 
The XML files of pre-trained classifiers are stored in Haarcascades folder

Haar Cascade Classifier
It is a machine learning based approach where a cascade function is trained from a lot of positive (images with face) and negative images (images without face). The algorithm is proposed by Paul Viola and Michael Jones.

The algorithm has four stages:

1. Haar Feature Selection: Haar features are calculated in the subsections of the input image. The difference between the sum of pixel intensities of adjacent rectangular regions is calculated to differentiate the subsections of the image. A large number of haar-like features are required for getting facial features.
2. Creating an Integral Image: Too much computation will be done when operations are performed on all pixels, so an integral image is used that reduce the computation to only four pixels. This makes the algorithm quite fast.
3. Adaboost: All the computed features are not relevant for the classification purpose. Adaboost is used to classify the relevant features.
4. Cascading Classifiers: Now we can use the relevant features to classify a face from a non-face but algorithm provides another improvement using the concept of cascades of classifiers. Every region of the image is not a facial region so it is not useful to apply all the features on all the regions of the image. Instead of using all the features at a time, group the features into different stages of the classifier.Apply each stage one-by-one to find a facial region. If on any stage the classifier fails, that region will be discarded from further iterations. Only the facial region will pass all the stages of the classifier.
