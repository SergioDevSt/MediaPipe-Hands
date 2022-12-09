#Importlibraries
import cv2
import mediapipe as mp
import json
import os

#Function to get images path
def load_images(folder):
	images = []
	for filename in os.listdir(folder):
		img = os.path.join(folder,filename)
		if img is not None:
			images.append(img)
	return images

#WIP for better approach
#Change this where you want to save the DB data	
DB_path= os.getcwd() + "/BD/hands.json"
#Change this where you want to save the DB data	

#Change this where you store all img			
IMG_path= os.getcwd() + "/Images/Normal"
#Change this where you store all img			

#Save dir of img in a array to loop through 
Image_Files = []
Image_Files = load_images(IMG_path)

# Basics imports to work with hands (more info: https://google.github.io/mediapipe/solutions/hands.html )
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


#Parameters to analize hands in image view docs.
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
		#Loop through all img 
        for idx, file in enumerate(Image_Files):
           # Read an image, flip it around y-axis for correct handedness output (see
           # above).
           image = cv2.flip(cv2.imread(file), 1)
           # Convert the BGR image to RGB before processing.
           results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
           
           #This save all coordinates in the json file like a python dictionarie
           if results.multi_hand_landmarks:
			   #WIP 
              for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):  
                  Mano = [{
				   "Imagen" : file,
				   "Landmarks" : {
					   mp_hands.HandLandmark(0).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(0).value].z ,
					   },
					   mp_hands.HandLandmark(1).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(1).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(1).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(1).value].z ,
					   },
					   mp_hands.HandLandmark(2).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(2).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(2).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(2).value].z ,
					   },
					   mp_hands.HandLandmark(3).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(3).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(3).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(3).value].z ,
					   },
					   mp_hands.HandLandmark(4).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(4).value].z ,
					   },
					   mp_hands.HandLandmark(5).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(5).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(5).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(5).value].z ,
					   },
					   mp_hands.HandLandmark(6).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(6).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(6).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(6).value].z ,
					   },
					   mp_hands.HandLandmark(7).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(7).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(7).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(7).value].z ,
					   },
					   mp_hands.HandLandmark(8).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(8).value].z ,
					   },
					   mp_hands.HandLandmark(9).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(9).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(9).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(9).value].z ,
					   },
					   mp_hands.HandLandmark(10).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(10).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(10).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(10).value].z ,
					   },
					   mp_hands.HandLandmark(11).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(11).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(11).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(11).value].z ,
					   },
					   mp_hands.HandLandmark(12).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(12).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(12).value].z ,
					   },
					   mp_hands.HandLandmark(13).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(13).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(13).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(13).value].z ,
					   },
					   mp_hands.HandLandmark(14).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(14).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(14).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(14).value].z ,
					   },
					   mp_hands.HandLandmark(15).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(15).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(15).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(15).value].z ,
					   },
					   mp_hands.HandLandmark(16).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(16).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(16).value].z ,
					   },
					   mp_hands.HandLandmark(17).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(17).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(17).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(17).value].z ,
					   },
					   mp_hands.HandLandmark(18).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(18).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(18).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(18).value].z ,
					   },
					   mp_hands.HandLandmark(19).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(19).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(19).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(19).value].z ,
					   },
					   mp_hands.HandLandmark(20).name: {
						   "x" : hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x ,
						   "y" : hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y ,
						   "z" : hand_landmarks.landmark[mp_hands.HandLandmark(20).value].z ,
					   },
					} 
				}]
				
			  #Format all the data to save it in a json file
              with open(DB_path, "a") as outfile: #Change this to add,overwrite, etc.
                   json.dump(Mano, outfile,indent=4)
				   
              data = json.dumps(Mano,indent =4)
              #print(data) 
			  
			  #Draw the landmarks 
              mp_drawing.draw_landmarks(
					image,
					hand_landmarks,
					mp_hands.HAND_CONNECTIONS,
					mp_drawing_styles.get_default_hand_landmarks_style(),
					mp_drawing_styles.get_default_hand_connections_style())
			# Display image
           cv2.imshow('MediaPipe Hands', image)
           if cv2.waitKey(0) & 0xFF == ord('q'):
              continue

