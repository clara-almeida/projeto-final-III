import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from raspador import get_epbr
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__) # Cria uma instância do Flask. 

@app.route("/epbr")
def epbr():
    run_epbr = get_epbr()
    return render_template('epbr.html')


if __name__ == "__main__":
    app.run(debug=True)
