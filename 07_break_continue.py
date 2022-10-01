def continuar():
    for contador in range(100):
        if contador % 2 != 0:
            continue
        print(contador)

def pausar():
    for i in range(100):
        print(i)
        if i == 50:
            break

if __name__ == '__main__':
    continuar()
    pausar()