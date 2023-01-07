import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="cricket_tournament"
)
mycursor=mydb.cursor()

st.set_page_config(page_title="CRICKET TOURNAMNET DATABASE",layout="wide")

st.markdown('<h1 <p style="background-color:BLACK;color:WHITE;font-size:50px;text-align:center">CRICKET TOURNAMENT DATABASE</p></h1>',unsafe_allow_html=True)
st.markdown("""---""")

selected = option_menu(
    menu_title="Main Menu",
    menu_icon="cast",
    options=["---","Insert","---","Update","---","Delete","---","Query","---"],
    icons=["","capslock-fill","","arrow-repeat","","backspace-reverse","","arrow-left-right"],
    orientation="horizontal",
    default_index=-1
)

col1,col2,col3 = st.columns([2,8,1])
image =Image.open("C:/Users/91961/Desktop/DBMS Project/Image.jpg")
with col2:
    image=st.image(image=image)


def run_query(query):
        mycursor.execute(query)
        return mycursor.fetchall()

def clear_text():
    st.session_state["text"]=""

if selected == "Insert":
    image.empty()
    st.markdown('<h1 <p style="color:Blue;font-size:40px;text-align:center">INSERT</p></h1>',unsafe_allow_html=True)
    
    rows = [["Select.."]]
    out = run_query("show tables;")
    rows.extend(out)
    rows = pd.DataFrame(rows)

    st.subheader("Select the table to which you want to insert the values")
    table=st.selectbox('Choose table',(rows),index=0)
    
    if table=='Select..':
        st.write("Please select the table")
    
    else:
        query = "desc "+table+" ;"
        output_1 = run_query(query)
        output_2 = pd.DataFrame(output_1,columns=["Field","Type","Null","Key","Default","Extra"])
        st.write('\n')
        st.write('\n')
        st.write("The schema of selected table ",table," looks like this..")
        st.write(output_2)

        st.write('\n')
        st.write("Enter the appropriate values : ")
        if table=='owner':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.text_input(output_1[2][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into owner values (%s,%s,%s)",(input1,input2,input3))
                    mydb.commit()
                    st.success("Insertion successfull")
                
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Owner_ID","First_Name","Last_Name"])
            st.write(last)
        
        if table=='coach':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.selectbox(output_1[2][0],["Batting","Bowling"])
                input4=st.text_input(output_1[3][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into coach values (%s,%s,%s,%s)",(input1,input2,input3,input4))
                    mydb.commit()
                    st.success("Insertion successfull")
        
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Coach_ID","Coach_Name","Coach_Type","Team_ID"])
            st.write(last)

        if table=='matches':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.date_input(output_1[1][0])
                input3=st.text_input(output_1[2][0])
                input4=st.text_input(output_1[3][0])
                input5=st.text_input(output_1[4][0])
                submission = st.form_submit_button(label="Submit")
               
                if submission==True:
                    mycursor.execute("Insert into matches values (%s,%s,%s,%s,%s)",(input1,input2,input3,input4,input5))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Match_ID","Match_Date","Winning_Team","POTM","Stadium"])
            st.write(last)

        if table=='players':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.text_input(output_1[2][0])
                input4=st.number_input(output_1[3][0],step=1)
                input5=st.text_input(output_1[4][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into players values (%s,%s,%s,%s,%s)",(input1,input2,input3,input4,input5))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Player_ID","First_Name","Last_Name","Age","Team_ID"])
            st.write(last)

        if table=='stat':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.number_input(output_1[2][0],step=1)
                input4=st.number_input(output_1[3][0],step=1)
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into stat values (%s,%s,%s,%s)",(input1,input2,input3,input4))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Player_ID","Match_ID","Runs","Wickets"])
            st.write(last)

        if table=='team':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.text_input(output_1[2][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into team values (%s,%s,%s)",(input1,input2,input3))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Team_ID","Team_Name","Owner_ID"])
            st.write(last)

        if table=='umpire':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                input3=st.number_input(output_1[2][0],step=1)
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into umpire values (%s,%s,%s)",(input1,input2,input3))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Umpire_ID","Umpire_Name","Experience"])
            st.write(last)

        if table=='plays':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into plays values (%s,%s)",(input1,input2))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Team_ID","Match_ID"])
            st.write(last)
        
        if table=='referee':
            with st.form(key="Insert_form",clear_on_submit=True):
                input1=st.text_input(output_1[0][0])
                input2=st.text_input(output_1[1][0])
                submission = st.form_submit_button(label="Submit")

                if submission==True:
                    mycursor.execute("Insert into referee values (%s,%s)",(input1,input2))
                    mydb.commit()
                    st.success("Insertion successfull")
            
            st.write("\n")
            st.write("\n")
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Match_ID","Umpire_ID"])
            st.write(last)

if selected == "Update":
    image.empty()
    st.markdown('<h1 <p style="color:Blue;font-size:40px;text-align:center">UPDATE</p></h1>',unsafe_allow_html=True)
    
    st.subheader("Select the table from which you want to update the records..")
    table=st.selectbox('Choose table',('Select..','players','team','matches','coach','owner','umpire'),index=0)
    
    if table=='Select..':
        st.write("Please select the table")
    
    else:
        if table=='owner':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Owner_ID","First_Name","Last_Name"])
            st.write(last)

            mycursor.execute("select Owner_ID,First_Name from owner;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM owner WHERE Owner_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Owner_ID = selected_record[0][0]
                First_Name = selected_record[0][1]
                Last_Name = selected_record[0][2]

            new_Owner_ID = st.text_input("Owner_ID : ",Owner_ID)
            new_First_Name = st.text_input("First_Name : ",First_Name)
            new_Last_Name = st.text_input("Last_Name : ",Last_Name)

            if st.button("Update"):
                mycursor.execute("UPDATE owner SET Owner_ID=%s, First_Name=%s, Last_Name=%s WHERE "
                "Owner_ID=%s and First_Name=%s and Last_Name=%s", (new_Owner_ID,new_First_Name,new_Last_Name,Owner_ID,First_Name,Last_Name))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM owner')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)
            
        if table=='players':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Player_ID","First_Name","Last_Name","Age","Team_ID"])
            st.write(last)

            mycursor.execute("select Player_ID,First_Name from players;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM players WHERE Player_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Player_ID = selected_record[0][0]
                First_Name = selected_record[0][1]
                Last_Name = selected_record[0][2]
                Age = selected_record[0][3]
                Team_ID = selected_record[0][4]

            new_Player_ID = st.text_input("Player_ID : ",Player_ID)
            new_First_Name = st.text_input("First_Name : ",First_Name)
            new_Last_Name = st.text_input("Last_Name : ",Last_Name)
            new_Age = st.number_input("Age : ",Age,step=1)
            new_Team_ID = st.text_input("Team_ID : ",Team_ID)

            if st.button("Update"):
                mycursor.execute("UPDATE players SET Player_ID=%s, First_Name=%s, Last_Name=%s, Age=%s, Team_ID=%s WHERE "
                "Player_ID=%s and First_Name=%s and Last_Name=%s and Age=%s and Team_ID=%s", (new_Player_ID,new_First_Name,new_Last_Name,new_Age,new_Team_ID,Player_ID,First_Name,Last_Name,Age,Team_ID))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM players')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)

        if table=='team':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Team_ID","Team_Name","Owner_ID"])
            st.write(last)

            mycursor.execute("select Team_ID,Team_Name from team;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM team WHERE Team_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Team_ID = selected_record[0][0]
                Team_Name = selected_record[0][1]
                Owner_ID = selected_record[0][2]

            new_Team_ID = st.text_input("Team_ID : ",Team_ID)
            new_Team_Name = st.text_input("Team_Name : ",Team_Name)
            new_Owner_ID = st.text_input("Owner_ID : ",Owner_ID)

            if st.button("Update"):
                mycursor.execute("UPDATE team SET Team_ID=%s, Team_Name=%s, Owner_ID=%s WHERE "
                "Team_ID=%s and Team_Name=%s and Owner_ID=%s", (new_Team_ID,new_Team_Name,new_Owner_ID,Team_ID,Team_Name,Owner_ID))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM team')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)

        if table=='matches':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Match_ID","Match_Date","Winning_Team","POTM","Stadium"])
            st.write(last)

            mycursor.execute("select Match_ID from matches;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM matches WHERE Match_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Match_ID = selected_record[0][0]
                Match_Date = selected_record[0][1]
                Winning_Team = selected_record[0][2]
                POTM = selected_record[0][3]
                Stadium = selected_record[0][4]

            new_Match_ID = st.text_input("Match_ID : ",Match_ID)
            new_Match_Date = st.date_input("Match_Date : ",Match_Date)
            new_Winning_Team = st.text_input("Winning_Team : ",Winning_Team)
            new_POTM = st.text_input("POTM : ",POTM)
            new_Stadium = st.text_input("Stadium : ",Stadium)

            if st.button("Update"):
                mycursor.execute("UPDATE matches SET Match_ID=%s, MDate=%s, Winning_Team=%s, POTM=%s, Stadium=%s WHERE "
                "Match_ID=%s and MDate=%s and Winning_Team=%s and POTM=%s and Stadium=%s", (new_Match_ID,new_Match_Date,new_Winning_Team,new_POTM,new_Stadium,Match_ID,Match_Date,Winning_Team,POTM,Stadium))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM matches')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)

        if table=='coach':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Coach_ID","Coach_Name","Type","Team_ID"])
            st.write(last)

            mycursor.execute("select Coach_ID,Coach_Name from coach;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM coach WHERE Coach_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Coach_ID = selected_record[0][0]
                Name = selected_record[0][1]
                Type = selected_record[0][2]
                Team_ID = selected_record[0][3]

            new_Coach_ID = st.text_input("Coach_ID : ",Coach_ID)
            new_Name = st.text_input("Coach_Name : ",Name)
            new_Type = st.selectbox("Type : ",["Batting","Bowling"])
            new_Team_ID = st.text_input("Team_ID : ",Team_ID)

            if st.button("Update"):
                mycursor.execute("UPDATE coach SET Coach_ID=%s, Coach_Name=%s, CType=%s, Team_ID=%s WHERE "
                "Coach_ID=%s and Coach_Name=%s and CType=%s and Team_ID=%s", (new_Coach_ID,new_Name,new_Type,new_Team_ID,Coach_ID,Name,Type,Team_ID))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM coach')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)
            
        if table=='umpire':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Umpire_ID","Umpire_Name","Experience"])
            st.write(last)

            mycursor.execute("select Umpire_ID,Umpire_Name from umpire;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            upd = st.selectbox("Update record : ",list)
            mycursor.execute('SELECT * FROM umpire WHERE Umpire_ID="{}"'.format(upd))
            selected_record = mycursor.fetchall()
            if selected_record:
                Umpire_ID = selected_record[0][0]
                Umpire_Name = selected_record[0][1]
                Experience = selected_record[0][2]

            new_Umpire_ID = st.text_input("Umpire_ID : ",Umpire_ID)
            new_Umpire_Name = st.text_input("Umpire_Name : ",Umpire_Name)
            new_Experience = st.text_input("Experience : ",Experience)

            if st.button("Update"):
                mycursor.execute("UPDATE umpire SET Umpire_ID=%s, Umpire_Name=%s, Experience=%s WHERE "
                "Umpire_ID=%s and Umpire_Name=%s and Experience=%s", (new_Umpire_ID,new_Umpire_Name,new_Experience,Umpire_ID,Umpire_Name,Experience))
                mydb.commit()
                st.success("Successfully updated")

            mycursor.execute('SELECT * FROM umpire')
            data = mycursor.fetchall()
            data = pd.DataFrame(data, columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(data)

if selected == "Delete":
    image.empty()
    st.markdown('<h1 <p style="color:Blue;font-size:40px;text-align:center">DELETE</p></h1>',unsafe_allow_html=True)

    st.subheader("Select the table from which you want to delete the records..")
    table=st.selectbox('Choose table',('Select..','players','team','matches','coach','owner','umpire'),index=0)
    
    if table=='Select..':
        st.write("Please select the table")
    
    else:
        if table=='owner':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Owner_ID","First_Name","Last_Name"])
            st.write(last)

            mycursor.execute("select Owner_ID,First_Name from owner;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete Owner"):
                mycursor.execute('DELETE FROM owner WHERE Owner_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Owner has been deleted successfully..")
            mycursor.execute('SELECT * FROM owner')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)
            
        if table=='coach':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Coach_ID","Name","Type","Team_ID"])
            st.write(last)

            mycursor.execute("select Coach_ID,Coach_Name from coach;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete coach"):
                mycursor.execute('DELETE FROM coach WHERE Coach_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Coach has been deleted successfully..")
            mycursor.execute('SELECT * FROM coach')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)
            
        if table=='matches':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Match_ID","Match_Date","Winning_Team","POTM","Stadium"])
            st.write(last)

            mycursor.execute("select Match_ID from matches;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete Match"):
                mycursor.execute('DELETE FROM matches WHERE Match_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Match has been deleted successfully..")
            mycursor.execute('SELECT * FROM matches')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)

        if table=='players':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Player_ID","First_Name","Last_Name","Age","Team_ID"])
            st.write(last)

            mycursor.execute("select Player_ID,First_Name from players;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete Player"):
                mycursor.execute('DELETE FROM players WHERE Player_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Player has been deleted successfully..")
            mycursor.execute('SELECT * FROM players')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)
        
        if table=='team':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Team_ID","Team_Name","Owner_ID"])
            st.write(last)

            mycursor.execute("select Team_ID,Team_Name from team;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete Team"):
                mycursor.execute('DELETE FROM team WHERE Team_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Team has been deleted successfully..")
            mycursor.execute('SELECT * FROM team')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)

        if table=='umpire':
            st.subheader("Present Records")
            query = "select * from "+ table
            last = run_query(query)
            last = pd.DataFrame(last,columns=["Umpire_ID","Umpire_Name","Experience"])
            st.write(last)

            mycursor.execute("select Umpire_ID,Umpire_Name from umpire;")
            list = mycursor.fetchall()
            list = [i[0] for i in list]
            dele = st.selectbox("Delete record : ",list)
            st.warning("Do you want to delete ::{}".format(dele))
            if st.button("Delete Umpire"):
                mycursor.execute('DELETE FROM umpire WHERE Umpire_ID="{}"'.format(dele))
                mydb.commit()
                st.success("Umpire has been deleted successfully..")
            mycursor.execute('SELECT * FROM umpire')
            new_table = mycursor.fetchall()
            new_table = pd.DataFrame(new_table,columns=[i[0] for i in mycursor.description])
            with st.expander("Updated data"):
                st.dataframe(new_table)
            

if selected == "Query":
    image.empty()
    st.markdown('<h1 <p style="color:Blue;font-size:40px;text-align:center">QUERY</p></h1>',unsafe_allow_html=True)
    
    with st.form(key="Query_form",clear_on_submit=False):
        query = st.text_area("Enter your query : ")
        queries = query.split(";")
        submission = st.form_submit_button(label="Submit")
        if submission==True:
            for query in queries:
                if query==" \n" or query=="\n" or query==" ":
                    st.write()
                else:
                    mycursor.execute(query)
                    if 'select' in query or 'Select' in query or "SELECT" in query or 'desc' in query or 'Desc' in query or 'DESC' in query or 'show' in query or 'Show' in query or 'SHOW' in query:
                        output=mycursor.fetchall()
                        output=pd.DataFrame(output,columns=[i[0] for i in mycursor.description])
                        out = 'Results of your query ( '+ query + ')'
                        st.write(out)
                        st.write(output)
                    
                    else:
                        mydb.commit()
                        st.success("Query executed successfully..")

mydb.close()