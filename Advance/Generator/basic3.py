def menu_card():
        print("1") 
        yield("Idly")
        print("1") 
 
        yield("Dosa")
        print("1") 
 
        yield("Poori")
        print("1") 
 
        yield("Vada")
        print("1") 
 
object=menu_card()
 
print("Next item is:",next(object))
 
print("Next item is:",next(object))
 
print("Next item is:",next(object))
 
print("Next item is:",next(object))
 
print("Next item is:",next(object))
