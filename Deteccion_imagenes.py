#Librerias necesarias para la cargar los archivos y usar reconocimiento facial

#Lo unico que deberemos hacer si usamos el codigo es cargar las imagenes que queramos comparar
#Yo he usado imagenes que se encontraban en la carpeta del archivo .py pero tambien podriamos usar la ruta

import cv2
import face_recognition as fr

# cargar imagenes

foto_control = fr.load_image_file('1.jpg')
foto_prueba = fr.load_image_file('1-3.jpg')

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizamos cara control

lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# localizamos cara prueba

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]


# mostrar rectangulo en el contorno de la cara

cv2.rectangle(foto_control,
                (lugar_cara_A[3], lugar_cara_A[0]),
                (lugar_cara_A[1], lugar_cara_A[2]),
                (0, 255, 0),
                2)

cv2.rectangle(foto_prueba,
                (lugar_cara_B[3], lugar_cara_B[0]),
                (lugar_cara_B[1], lugar_cara_B[2]),
                (0, 255, 0),
                2)




#realizar comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B,0.4 )

#medida de comparacion entre fotos
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

#mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (55,30),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (0,255,0),
            2)


# mostrar imagenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# mantener imagenes
cv2.waitKey()
