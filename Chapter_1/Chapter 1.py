{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0596e5ff-5fd7-4d8b-a616-be153a75faf8",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2182793953.py, line 8)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mimport streamlit-jupyter as sj\u001b[39m\n                    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Build with AI: AI-Powered Dashboards with Streamlit \n",
    "#Quick Review: Streamlit Basics for Web Apps\n",
    "\n",
    "#Import packages\n",
    "import streamlit as st\n",
    "from datetime import date, datetime\n",
    "\n",
    "import streamlit-jupyter as sj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ded0dc92-1ece-4b8e-9c86-33abd0abf9bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "#Configure page\n",
    "st.set_page_config(page_title=\"Streamlit Basics Review\",layout=\"wide\")\n",
    "\n",
    "#Write title and text\n",
    "st.title(\"Streamlit Basics Review\")\n",
    "st.write(\"Hello world!\")\n",
    "\n",
    "#Gather current date and time\n",
    "st.write(\"Current date and time:\", datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\"))\n",
    "\n",
    "#Create button\n",
    "if st.button(\"Press me!\"):\n",
    "    st.success(\"Button was pressed!\")\n",
    "\n",
    "#Create slider widget\n",
    "age = st.slider(\"Your age\", 0, 100, 30)\n",
    "st.write(f\"You are {age} years old.\")\n",
    "\n",
    "#Create text input widget\n",
    "name = st.text_input(\"Enter your name:\")\n",
    "if name:\n",
    "    st.write(f\"Hello, {name}!\")\n",
    "\n",
    "#Create checkbox widget\n",
    "toggle = st.checkbox(\"Check for a surprise\")\n",
    "if toggle:\n",
    "    st.info(\"Surprise!\")\n",
    "\n",
    "#Create multiselect widget\n",
    "options = st.multiselect(\"Choose pizza toppings\", [\"Cheese\", \"Pepperoni\", \"Onions\"])\n",
    "st.write(\"Toppings:\", options)\n",
    "\n",
    "#Create sidebar container\n",
    "st.sidebar.title(\"Sidebar Panel\")\n",
    "#Add selection widget for sidebar\n",
    "sidebar_option = st.sidebar.selectbox(\"Select an option:\", [\"Home\", \"Settings\", \"About\"])\n",
    "st.sidebar.write(\"You chose\", sidebar_option)\n",
    "\n",
    "#Create three column containers\n",
    "col1, col2, col3 = st.columns(3)\n",
    "#Create temperature container\n",
    "with col1:\n",
    "    st.metric(\"Temperature\", \"72°F\", \"-1.2°F\")\n",
    "#Create wind speed container\n",
    "with col2:\n",
    "    st.metric(\"Wind Speed\", \"10 mph\", \"+1.5 mph\")\n",
    "#Create humidity container\n",
    "with col3:\n",
    "    st.metric(\"Humidity\", \"50%\", \"-5%\")\n",
    "\n",
    "#Create expander container\n",
    "with st.expander(\"See more details\"):\n",
    "    st.write(\"Here are more details... you can put any Streamlit commands inside expanders.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f22adec8-b964-424b-8bde-dc23b2213e19",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
