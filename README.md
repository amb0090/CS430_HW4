# CS430_HW4

This repo contains the following items:
- kmeans.py
- output from kmeans: kmeans_output.txt
- plot from kmeans: Figure_1.png
- output from easy.py in libsvm: svm_output.txt
- plot from gnuplot in libsvm: train.scale.png

K-Means
- Ensure iris.data is in the same directory as kmeans.py
- Ensure the correct libraries are installed
- Enter the following command to run kmeans.py: python3 kmeans.py


SVM

Formatted data file from kmeans.py was used for libsvm

Commands needed for SVM, assuming libsvm is installed correctly:
- python3 subset.py -s 1 iris_libsvm.txt 120 train test
- python3 easy.py train test > svm_output.txt

