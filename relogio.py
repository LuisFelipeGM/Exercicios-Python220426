from time import sleep

a = int(input("Que horas deseja colocar o alarme?"))
b = int(input("Que minuto deseja colocar o alarme?"))
c = int(input("Que segundo deseja colocar o alarme?"))
continuar = input("Deseja começar?")
h = 0
while continuar == "sim":
    while h < 24:
        m = 0

        while m < 60:
            s = 0

            while s < 60:
                print(f"{h:02}:{m:02}:{s:02}")
                sleep(0.1)
                if (h == a and m == b and s == c):
                    print ("ALARME")
                    break
                s += 1

            if (h == a and m == b):
                    break
            m += 1

        if (h == a):
                    break
        h += 1
    continuar = input("Deseja continuar?")
    if(continuar != "sim"):
        break
    