import mimetypes

filename = input("file extention encoder: ")
mime_type, encoding = mimetypes.guess_type(filename)

print(mime_type)  