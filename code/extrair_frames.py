import cv2
import csv

video='caminho/do/video'

video_cv=cv2.VideoCapture(video)

if not video_cv.isOpened():
    print("Erro ao abrir o video")
    exit()

fps= video_cv.get(cv2.CAP_PROP_FPS)
print(f"FPS do video: {fps}")

csv_file = open("posicoes.csv", mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["frame", "tempo", "x", "y"])  # cabeçalho

frame_number = 0

while True:
    ret, frame = video_cv.read()
    if not ret:
        break

    frame_number += 1
    time = frame_number / fps

    # Mostrar frame (opcional)
    cv2.imshow("Frame", frame)

    # Sai do loop se apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # TODO: Extrair a posição da massa aqui

    # Por enquanto, valores fictícios
    x, y = None, None

    # Salvar no CSV
    csv_writer.writerow([frame_number, time, x, y])

    # (seu código do while aqui)

csv_file.close()
video_cv.release()
cv2.destroyAllWindows()


