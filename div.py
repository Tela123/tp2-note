# try:
    # 3/0 
    # ZeroDivisionError
    # print('hello world')
    # print(b)
    # NameError
    # int ('abc') 
    # ValueError
# abc+1
# 1+uo
    # TypeError
# except:
    # print('Erreur, division par zero')
# finally:
#      print('Erreur, division par zero')

# pour traiter plusieurs erreurs a la fois

try:
    int('abc')
    3/0
except ValueError:
    print('Erreur de valeur')
except ZeroDivisionError:
    print('Impossible de diviser par zero')
# creer une Exception personnalisee, elle doit toujours heriter de la classe mere Exception
# class monException(Exception):
#     pass