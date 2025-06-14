
try:
    file_name=open('sample.txt','r')
    reading=file_name.read()
    print(reading)
    file_name.close()

except FileNotFoundError:
    print("Sorry,the file your are trying to read doesnot exist.")
