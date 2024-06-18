{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d70b5d0-0404-4310-bdb3-bffb93cad42b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d81ace9-cba9-418d-8223-211410178f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "## LOVE CALCULATOR USNIG GPT ##\n",
    "\n",
    "from flask import Flask, render_template, request\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "def calculate_love_score(name1, name2):\n",
    "    couple_name = (name1 + name2).lower()\n",
    "    t = couple_name.count(\"t\")\n",
    "    r = couple_name.count(\"r\")\n",
    "    u = couple_name.count(\"u\")\n",
    "    e = couple_name.count(\"e\")\n",
    "    first_digit = t + r + u + e\n",
    "\n",
    "    l = couple_name.count(\"l\")\n",
    "    o = couple_name.count(\"o\")\n",
    "    v = couple_name.count(\"v\")\n",
    "    e = couple_name.count(\"e\")\n",
    "    second_digit = l + o + v + e\n",
    "\n",
    "    score = int(str(first_digit) + str(second_digit))\n",
    "    return score\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/result', methods=['POST'])\n",
    "def result():\n",
    "    name1 = request.form['name1']\n",
    "    name2 = request.form['name2']\n",
    "    love_score = calculate_love_score(name1, name2)\n",
    "    if love_score <= 10:\n",
    "        result_text = \"YOUR LOVE SCORE IS\"\n",
    "    elif love_score <= 15:\n",
    "        result_text = \"YOUR LOVE SCORE IS\"\n",
    "    else:\n",
    "        result_text = \"GREAT COUPLE\"\n",
    "    return render_template('result.html', love_score=love_score, result_text=result_text)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1ad87b1-37cf-44b8-b77e-05116741d4b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
