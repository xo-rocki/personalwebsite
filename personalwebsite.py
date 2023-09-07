
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/3bd19307-33b2-4dd7-a9c5-588b873f981d/pR6Wl6iieR.json")
img_edgerunners = Image.open("images/maxresdefault.jpg")
img_tokyoghoul = Image.open("images/alwaysthehero.jpg")
img_mobpsycho = Image.open("images/paristokyo.jpg")
img_banner = Image.open("images/rocki.png")
img_saka = Image.open("images/saka.png")
img_harper = Image.open("images/harper1.jpg")
img_book = Image.open("images/book.png")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Whattup, its Rocki")
        st.title("This is my Personal website!")
        st.write("I am passionate about sports, video games, the new age of technology," 
                + " and overall content creation")
        st.write("[Message me on Discord 👾](discordapp.com/users/426917829065834510)")
    with right_column:
        st.image(img_banner, width=600)


with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
         st.header("Stuff I do")
         st.write("##")
         st.write(
             '''
             Here are some of the many interests and/or things I pursue:
             - B.S. in Computer Science
             
             - Sports Graphics using Adobe Photoshop
             
             - Anime Edits using Premiere Pro & After Effects that are
               later updated to my personal [Youtube](https://www.youtube.com/channel/UC5wVnSzjZTfw3yaVzIwtjgQ)
               
             - Video Game Enjoyer: CSGO, Valorant, Overwatch, R6
             
             - Sometimes a [Twitch Streamer](https://www.twitch.tv/xo_rocki)
             '''
         )
     with right_column:
        st_lottie(lottie_coding, height=500, key="coding")


with st.container():
    st.write("---")
    st.header("Video Projects")
    st.write("###")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_edgerunners)
    with text_column:
        st.subheader("Dreamer - Cyberpunk: Edgerunners")
        st.write(
            '''
            Trailer-like edit of the Netflix Anime, Cyberpunk: Edgerunners
            '''
        )
        st.markdown("[Watch Video...](https://youtu.be/G9NgN_nlEbA?si=xy7dmzwVtdDHSLG5)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mobpsycho)
    with text_column:
        st.subheader("Paris to Tokyo || Mob Psycho「AMV」")
        st.write(
            '''
            AMV Edit of the anime Mob Psycho 100
            '''
        )
        st.markdown("[Watch Video...](https://youtu.be/2FKRULYJZkw?si=IP4P7dfTZT5MSNNg)")
        
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_tokyoghoul)
    with text_column:
        st.subheader("Always the Hero - Ken Kaneki")
        st.write(
            '''
            Trailer-like edit of one of my favorite characters, Ken Kaneki
            from Tokyo Ghoul
            '''
        )
        st.markdown("[Watch Video...](https://youtu.be/U80z8CVEF54?si=wvE-vFYqYxlXyrT2)")
        

with st.container():
    st.write("---")
    st.header("Photo Projects")
    st.write("###")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.image(img_book)
    with middle_column:
        st.image(img_saka)
    with right_column:
        st.image(img_harper)