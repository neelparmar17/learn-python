str1 = "sfsf"
str2 = "dadad"

str3 = """%(str1)s dsds%(str2)s""" % {"str1": str1, "str2": str2}
print(str3)