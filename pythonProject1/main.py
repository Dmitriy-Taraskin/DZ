import my_package
from modules.module1 import function_from_module1
from modules.module2 import function_from_module2


from my_package.my_package1.file1 import function_from_my_package1_file1
from my_package.my_package1.file2 import function_from_my_package1_file2
from my_package.my_package1.my_package2.file1 import function_from_my_package2_file1
from my_package.my_package1.my_package2.file2 import function_from_my_package2_file2
from my_package.my_package1.my_package2.my_package3.file1 import function_from_my_package3_file1
from my_package.my_package1.my_package2.my_package3.file2 import function_from_my_package3_file2
if my_package.pack== "__main__":
    # Вызываем функции из модулей
    function_from_module1()
    function_from_module2()



    # Вызываем функции из пакетов
    
    function_from_my_package1_file1()
    function_from_my_package1_file2()
    function_from_my_package2_file1()
    function_from_my_package2_file2()
    function_from_my_package3_file1()
    function_from_my_package3_file2()