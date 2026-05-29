import streamlit as st   
st.set_page_config(page_title="BMICalculator", page_icon="⚖️", layout="centered")


st.title("⚖️ BMI Calculator") 
st.subheader("Body Mass & Index Calculator")

st.write("Calculate your BMI (Body Mass Index) using your height and weight.")


name = st.text_input("Enter Your Name")
age = st.number_input("Enter Your Age", min_value=1, max_value=120, step=1)

height = st.number_input("Enter Your Height (in centimeters)", min_value=50.0, max_value=300.0)
weight = st.number_input("Enter Your Weight (in kilograms)", min_value=1.0, max_value=500.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.success(f"Hello {name}! Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        st.warning("You are Underweight")

    elif 18.5 <= bmi < 24.9:
        st.success("You have a Normal Weight")

    elif 25 <= bmi < 29.9:
        st.warning("You are Overweight")

    else:
        st.error("You are Obese")   
# Health Tips
st.markdown("### Health Suggestion")
if bmi < 18.5:
    st.write("🍎 Eat nutritious food and maintain a healthy diet.")
elif 18.5 <= bmi < 24.9:
    st.write("✅ Great! Maintain your healthy lifestyle.")
elif 25 <= bmi < 29.9:
    st.write("🏃 Exercise regularly and reduce junk food.")
else:
    st.write("💪 Consult a healthcare expert and follow a fitness plan.")



st.markdown("---")
st.caption("Created using Python & Streamlit")

