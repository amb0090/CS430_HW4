# CS430_HW4

This repo contains the following items:
- kmeans.py
- centroids output from kmeans: kmeans_output.txt
- formatted data from kmeans: iris_libsvm.txt
- plot from kmeans: Figure_1.png
- output from easy.py in libsvm: svm_output.txt
- plot from gnuplot in libsvm: train.scale.png

K-Means
- Ensure iris.data is in the same directory as kmeans.py
- Ensure the correct libraries are installed
- Enter the following command to run kmeans.py: python3 kmeans.py


SVM

Ensure libsvm is installed and set up correctly

Formatted data file from kmeans.py was used for libsvm: iris_libsvm.txt

Move iris_libsvm.txt to libsvm-master/libsvm-master/tools

Commands needed for SVM, assuming libsvm is installed correctly:
- python3 libsvm-master/libsvm-master/tools subset.py -s 1 iris_libsvm.txt 120 train test
- python3 libsvm-master/libsvm-master/tools easy.py train test > svm_output.txt

