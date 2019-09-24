with open("aFileExercise.txt",'w') as tf:
    print(tf)
    print(type(tf))
    tf.write("Write to a text file as i wish to write\n")

with open("aFileExercise.txt",'a') as tf:
    print(tf)
    print(type(tf))
    tf.write("Write to a text file as i wish to write again\n")
