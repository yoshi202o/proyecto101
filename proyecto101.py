import random 
  
# Toma una variable para almacenar la respuesta y seguir tirando el dado
response = "y"
   
while response == "y": 
      
    # Gnenera un número al azar 
    # entre 1 y 6 (incluyendo 
    # 1 y 6) 
    no = random.randint(1,6) 

    # condiciones para verificar el valor del número  
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
      print("[-----]") 
      print("[     ]") 
      print("[0 0 0]") 
      print("[     ]") 
      print("[-----]") 
    if no == 4: 
      print("[-----]") 
      print("[0   0]") 
      print("[     ]") 
      print("[0   0]") 
      print("[-----]") 
    if no == 5: 
      print("[-----]") 
      print("[0   0]") 
      print("[  0  ]") 
      print("[0   0]") 
      print("[-----]") 

    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[    ]") 
        print("[0 0 0]") 
        print("[-----]") 
        
      
  
    
          
    # Pídele al usuario que ingrese una respuesta      
    response=input("presiona y para girar otra vez y n para salir:") 
    print("\n") 