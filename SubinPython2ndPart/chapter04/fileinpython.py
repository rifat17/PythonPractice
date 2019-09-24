with open("aTextFile.txt",'w') as tf:
    print(tf)
    print(type(tf))
    tf.write("Write to a text file as i wish to write\n")
