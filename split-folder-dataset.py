import os, os.path, shutil, math

# your path
source_path = '/content/data/' # change the value
destination_path = '/content/data-2' # change the value

# percentage of dataset division for train_set, val_set, test_set
train_div = 0.6 # change the value
val_div = 0.2 # change the value
test_div = 0.2 # change the value

print("source path : ",source_path)
print("destination path : ",destination_path,"\n")

# count files
#sum_files = len([name for name in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, name))])
#print(sum_files)

# create directories
path = destination_path+"/train" # your path
os.makedirs(path)
path = destination_path+"/val" # your path
os.makedirs(path)
path = destination_path+"/test" # your path
os.makedirs(path)

# save all of filenames in list, then sort it asc
myList = os.listdir(source_path)
myList.sort()
print("sum of your files : ",len(myList))

print("\nyour division \ntrain_div : ",train_div,"\nval_div : ",val_div,"\ntest_div : ",test_div)
print("percentage of dataset division",train_div+val_div+test_div,"\n")

if (train_div+val_div+test_div != 1.0):
  raise ValueError("Must be 1.0")

# sum of files in each set
lenList = len(myList)
count_train = lenList*train_div
count_val = lenList*val_div
count_test = lenList*test_div

print("lenList : ",lenList)
print("count_train : ",count_train)
print("count_val : ",count_val)
print("count_test : ",count_test)

print("\nMod\n")

mod_count_train = math.ceil(count_train)
mod_count_val = math.floor(count_val)
mod_count_test = math.floor(count_test)
sum_mod = mod_count_train+mod_count_val+mod_count_test

print("count_train : ",mod_count_train)
print("count_val : ",mod_count_val)
print("count_test : ",mod_count_test)
print("sum_mod : ",sum_mod)

print("\nUpdate Mod\n")

if(sum_mod<lenList):
  mod_count_train += lenList - sum_mod
  sum_mod = mod_count_train+mod_count_val+mod_count_test

print("count_train : ",mod_count_train)
print("count_val : ",mod_count_val)
print("count_test : ",mod_count_test)
print("sum_mod : ",sum_mod)

len_train = mod_count_train
len_val = len_train + mod_count_val
len_test = len_val + mod_count_test

print("\nMod len\n")

print("len_train : ",len_train)
print("len_val : ",len_val)
print("len_test : ",len_test)

# moving files
list_train = []
list_val = []
list_test = []

for i in range(len_train):
	list_train.append(myList[i])

for i in range(len_train,len_val):
	list_val.append(myList[i])

for i in range(len_val,len_test):
	list_test.append(myList[i])

print(list_train,"\n sum :",len(list_train))
print(list_val,"\n sum :",len(list_val))
print(list_test,"\n sum :",len(list_test))

for f in list_train:
  shutil.copy(source_path+f, destination_path+'/train') # your path

for f in list_val:
  shutil.copy(source_path+f, destination_path+'/val') # your path

for f in list_test:
  shutil.copy(source_path+f, destination_path+'/test') # your path
