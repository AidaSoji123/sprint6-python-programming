import datetime

# f = open("names","w")
# f.write("This is my first file")
# f.close()

# g = open("names","r")
# r = g.read()
# print(r)
# g.close()

# print(datetime.date.today())
# print(datetime.datetime.now())




def reportt_log(log_date,log_filename,log_bug):
    f = open("log","a")
    string1 = str(log_date) + " " + log_filename + " " + str(log_bug) + "\n"
    f.write(string1)
    f.close()


try:
    print("this is a try block")
    raise Exception('we raised an exception')
    print('this is the code after exception')
except Exception as e:
    print(e)
    reportt_log(datetime.datetime.now(),"index.py",e)
    