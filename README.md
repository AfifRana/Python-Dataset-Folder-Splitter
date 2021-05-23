# Python-Dataset-Folder-Splitter
For splitting dataset folder e.g. train set, validation set, test set. Especially for dataset with large amount of files, such as images.
You can run the splitter on your computer or your cloud machine such as Google Colab. Make sure python is installed on your machine.

Steps :
1. Open the files.
2. Edit your source path and destination path.
3. Edit your percentage division for train set, val set, test set.

Example Log

```
sum of your files :  11504

your division 
train_div :  0.6 
val_div :  0.2 
test_div :  0.2
percentage of dataset division 1.0 

lenList :  11504
count_train :  6902.4
count_val :  2300.8
count_test :  2300.8

Mod

count_train :  6903
count_val :  2300
count_test :  2300
sum_mod :  11503

Update Mod

count_train :  6904
count_val :  2300
count_test :  2300
sum_mod :  11504

Mod len

len_train :  6904
len_val :  9204
len_test :  11504
['000060e3121c7305.jpg', '000060e3121c7305.txt', '00022a6311159428.jpg', '00022a6311159428.txt', '0002af997ecdfcf4.jpg', '0002af997ecdfcf4.txt', '000396ae942e8778.jpg',..] 
 sum : 6904
['9260601f2ae0eb0b.jpg', '9260601f2ae0eb0b.txt', '9263f9cf3daf4092.jpg', '9263f9cf3daf4092.txt', '927f79fc81c8a79d.jpg', '927f79fc81c8a79d.txt', '929e0fee04c47378.jpg',..] 
 sum : 2300
['c9b95e3eba578668.jpg', 'c9b95e3eba578668.txt', 'c9c441a2585e0f64.jpg', 'c9c441a2585e0f64.txt', 'c9d2bbaa830c6323.jpg', 'c9d2bbaa830c6323.txt', 'c9e2a281a6bf7a73.jpg',..] 
 sum : 2300
 ```
