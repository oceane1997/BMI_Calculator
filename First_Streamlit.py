import streamlit as st
from streamlit.elements.lib.layout_utils import Height

st.title('Hello OCEANE')
st.header("This is a header")
st.write("This is the second line")
st.subheader("Hello YOU")
st.text("This is the third line")
st.markdown("###This is a markdown")
st.success("This is the success message")
st.warning("This is the warning message")
st.error("This is the error message")
st.info("This is the info message")
exp = ZeroDivisionError("Trying to divide by Zero" )
st.exception(exp)
from PIL import Image
img = Image.open("streamlit.png")
st.title("Affichage d'une image 📷")

try:
    img = Image.open("streamlit.png")
    st.image(img, caption="Mon logo préféré 💖", width=200)
except FileNotFoundError:
    st.error("L’image ‘streamlit.png’ n’a pas été trouvée. Vérifie que le fichier est dans le même dossier que ce script.")

# Case à cocher
if st.checkbox("Show/Hide") :
    st.text("Showing the widget")

#Bouton radio
status = st.radio("Select Gender : ",("Male","Female"))
if status == "Male" :
    st.success("Male")
else :
    st.success("Female")

### Bande déroulante (election)
Hobby = st.selectbox("Hobby", ["Sport","Lecture","Camping","Gaming"])
st.write("Your Hobby is : ", Hobby)

### Choix multiples
Hobbies = st.multiselect("Hobbies", ["Sport","Lecture","Camping","Gaming"])
st.write("You selected", len(Hobbies), "Hobbies")

### Bouton
st.button("Click me for no reason")

if st.button("Try me") :
    st.text("Hello to my world")

## Case input

name = st.text_input("Enter your name","Type here ...")

if st.button("Submit"):
    result = name.title()
    st.success(f"Bonjour {result} 😊!")

Level = st.slider("Sélectionne ton niveau",1,5)
if st.button ("Valider"):
    st.success(f"Tu as choisi le niveau {Level}")

##APPLICATION CALCUL BMI
st.title("WELCOME TO BMI CALCULATOR")
#BMI = None
# poids
Weight = st.number_input('Enter your weight in kg')
status = st.radio("Select your Height format", ('cm','m','foot'))
if status == 'cm':
    Height = st.number_input('Enter your height in cm')
    if Height > 0 :
     BMI = Weight/ (Height/100)**2


elif status == 'm':
    Height = st.number_input('Enter your height in m')
    if Height > 0 :
     BMI = Weight / (Height)**2


else:
    Height = st.number_input('Enter your height in foot')
    if Height > 0 :
     BMI = Weight/ (Height/3.28)**2

if st.button(" Calculate BMI") :
  st.success(f"Your BMI is {BMI:.2f}")

  if BMI < 16 :
     st.error("Your BMI is too low, you are extremely Underweighted.")

  elif BMI >= 16 and BMI < 18.5 :
     st.warning("Your BMI is  low, you are underweighted.")

  elif BMI >= 18.5 and BMI < 25 :
     st.info("Your BMI is  Normal")

  elif BMI >= 25 and BMI < 30:
     st.warning("Your BMI is high, you are Overweight")

  else :
     st.error("Your BMI is too high, you are Obese")
else:
  st.text("Please enter an Height > 0 to calculate the BMI")

st.write("🔁 Ceci est une mise à jour du projet")




