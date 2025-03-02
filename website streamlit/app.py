import streamlit as st

st.set_page_config(page_title="My Webpage",page_icon=":tada:", layout="wide")


#Header Section
st.subheader("Hi,i am catee :wave")
st.title("i am a cute kitten :cat:")
st.write("you can know more about me in the sidebar :point_left:")
st.write("[learn More >]")



# what i do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write("""
        1. Attect Everything.
        Pounching on my feet when i walk.
        Attecking shoelaces,curtains,or even their own shadow.
        Sneak-attecking from behind furniture like a tiny ninja!
        2. jumping onto tables, shelves,and even my head.
        knocking things off desk just becouse they can.
        3. Zoomies at 3 Am
         Running at top speed across the house for no reason.
         Skidding across the floor like a race car.
         Bouching of walls,furniture,and even me!
         """)


 #interaction Section
    st.markdown("## Show some love! :heart:")
           
# Create columns for button 
    col1, col2, col3, col4 = st.columns(4)

# like Button
    with col1:
             if st.button("👍like"):
                 st.write("Thank you for liking :heart:")

# Comment Button
with col2:
            if st.button("Comment"):
             st.write("please leave a comment below :point_down:")
            st.text_area("Comments")

# Share Button
with col3:
            if st.button("Share"):
                 st.write("Share this page with your friends and family :point_down")
# Subscribe Button
with col4:
                if st.button("Subscribe"):
                 st.balloons()
                 st.success("Subscribe")
                 st.succes("Subscribed suucessfully")

                                
    
    
    

