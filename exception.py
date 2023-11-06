# try:
#     with open('sample.txt','r') as file:
#         content=file.read()
#         print(content)
# except FileNotFoundError:
#     print('The specified is not found')
# except Exception as e:
#     print('An error occured: ',str(e))



# '''read and write'''

try:
    with open('sample.txt','r') as file:
        content=file.read()
    with open('output.txt','w') as output_file:
        output_file.write(content)
    print('file content has been copied to the output file')
except FileNotFoundError:
    print('The specified is not found')
except Exception as e:
    print('An error occured: ',str(e))