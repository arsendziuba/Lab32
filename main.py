
var1 = "Привет"


var1_type = type(var1)
print("Тип var1:", var1_type)


is_var1_true = var1 is True
print("Является ли var1 истиной (True)?", is_var1_true)


is_var1_false = var1 is False
print("Является ли var1 ложью (False)?", is_var1_false)


var2 = var1 or True


is_var2_true = var2 is True
print("Является ли var2 истиной (True)?", is_var2_true)


is_var2_false = var2 is False
print("Является ли var2 ложью (False)?", is_var2_false)


print("Значение var1 - %(var1)s" % vars())
print("Значение var2 - %(var2)s" % vars())
