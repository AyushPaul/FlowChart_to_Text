import easyocr
import cv2
import matplotlib.pyplot as plt
import os
import openai
reader = easyocr.Reader(['en'], gpu=False)
image = cv2.imread('example.png')
result = reader.readtext('example.png')


openai.api_key = "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"

#print(result[0][1])
Total = []

prompt = ""

for i in range(len(result)):
    prompt+=(result[i][1]+" ")

#print(prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Can you create a High Level Design Document for the following endpoints :" + " " + prompt,
  max_tokens=1500,
  temperature=0
)

print(response["choices"][3])


for (bbox, text, prob) in result:
    Total.append(text)
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    cv2.rectangle(image, tl, br, (0, 255, 0), 1)
    cv2.putText(image, text, (tl[0], tl[1] - 2),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0),1)
plt.rcParams['figure.figsize'] = (16,16)
plt.imshow(image)
plt.show()
#print(Total[0])