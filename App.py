from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
@app.route('/<show_title>'
           '<show_image_height>'
           '<show_image_imageUrl>'
           '<show_image_width>'
           'show_rank'
           'show_yr')
def overlay(show_title=None,
            show_image_height=None,
            show_image_imageUrl=None,
            show_image_width=None,
            show_rank=None,
            show_yr=None):

    url = "https://imdb8.p.rapidapi.com/auto-complete"

    try_variable = True

    while try_variable:
        try:
            query = input("What show would you like a poster for: ")

            querystring = {"q": query}

            headers = {
                'x-rapidapi-key': "fb82ae7848msh91722b54eeeec8cp17c717jsn08b7a3ab507e",
                'x-rapidapi-host': "imdb8.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            load_variable = json.loads(response.text)

            show_title = str(load_variable["d"][0]["l"])

            show_image_height = str(load_variable["d"][0]["i"]["height"])
            show_image_imageUrl = str(load_variable["d"][0]["i"]["imageUrl"])
            show_image_width = str(load_variable["d"][0]["i"]["width"])

            show_rank = str(load_variable["d"][0]["rank"])

            show_yr = str(load_variable["d"][0]["yr"])

            try_variable = False
        except KeyError:
            print("Please enter a valid show\n")

    return render_template('Overlay.html',
                           show_title=show_title,
                           show_image_height=show_image_height,
                           show_image_imageUrl=show_image_imageUrl,
                           show_image_width=show_image_width,
                           show_rank=show_rank,
                           show_yr=show_yr)


if __name__ == '__main__':
    app.run()
