from flask import Flask, request, render_template 
import requests

app = Flask(__name__)
lastFmBaseUrl = 'http://ws.audioscrobbler.com/2.0/'
apiKey = 'd08b204e3587ae24e5476480cfc3a4ba'

# a function that will call the api and get top 5 track info
def searchTopTracks(singer):
    response = requests.get(f'{lastFmBaseUrl}?method=artist.gettoptracks&artist={singer}&api_key={apiKey}&format=json')
    jsonRes = response.json()
    topTenTracks = jsonRes['toptracks']['track'][:5]
    return topTenTracks

@app.route('/', methods = ['POST', 'GET'])
#return render_template('index.html')
def askUserInput():
    if request.method == 'POST':
        userInput = request.form.get('name')
        topTracksResponse = searchTopTracks(userInput)
        #return render_template('testing.html', userInput = userInput, resJson = topTracksResponse)
        #return render_template('testing.html', userInput = userInput, artistName = topTracksResponse[0]['artist']['name'], topTracksArray = topTracksResponse)
        return render_template('toptracks.html', userInput = userInput, artistName = topTracksResponse[0]['artist']['name'], topTracksArray = topTracksResponse)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)