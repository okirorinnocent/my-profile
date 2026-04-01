with tab3:
    st.header("Community Wall")
    st.info("Your messages are sent directly to my private database. For privacy, previous posts are not displayed publicly.")

    if not supabase:
        st.error("Connection keys not found in Secrets.")
    else:
        # The form is now the only thing in this tab
        with st.form("guest_form", clear_on_submit=True):
            name = st.text_input("Name")
            msg = st.text_area("Leave a message")
            submit = st.form_submit_button("Submit Message")

            if submit:
                if name and msg:
                    try:
                        # This inserts the data into Supabase
                        supabase.table("guestbook").insert(
                            {"name": name, "message": msg}).execute()

                        # We show a success message but DO NOT fetch any data back
                        st.success(
                            "Message received! Thank you for reaching out.")
                        st.balloons()
                        # Note: I removed st.rerun() to prevent the page from
                        # refreshing back to the start of the app immediately.
                    except Exception as e:
                        st.error(
                            "Submission failed. Please check your connection.")
                else:
                    st.warning("Please fill in both fields.")

        # IMPORTANT: The code that used to say 'supabase.table("guestbook").select("*")'
        # has been completely deleted. This ensures the website never asks
        # for the data, so it can never show it.
