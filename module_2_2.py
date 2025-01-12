first, second, third = int(input()), int(input()), int(input())
if first == second and first == third: # все 3 равны
	print(3)
elif first == second or first == third or second == third: # какие-либо 2 равны
	print(2)
else:
	print(0)