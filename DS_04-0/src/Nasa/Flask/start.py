import base64
import sys
import this
from flask import Flask, render_template, redirect, url_for, request
sys.path.append("..")
from api_class.API import Api_Nasa
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
tmp = [
    {'concepts': 'concept_tags functionality turned off in current service',
     'date': '2023-01-01',
     'explanation': "There, that dot on the right, that's the largest rock known in our Solar System."
                    "It is larger than every known asteroid, moon, and comet nucleus. "
                    "It is larger than any other local rocky planet. "
                    "This rock is so large its gravity makes it into a large ball that holds heavy gases near its surface. "
                    "(It used to be the largest known rock of any type until the recent discoveries of large dense planets orbiting other stars.)"
                    " The Voyager 1 spacecraft took the featured picture -- famously called Pale Blue Dot -- of this giant space rock in 1990 from"
                    "the outer Solar System.  Today, this rock starts another orbit around its parent star, for roughly the 5 billionth time, spinning"
                    "over 350 times during each trip.  Happy Gregorian Calendar New Year to all inhabitants of this rock we call Earth.",
     'hdurl': 'https://apod.nasa.gov/apod/image/2301/PaleBlueDotOrig_Voyager1_960.jpg',
     'media_type': 'image', 'service_version': 'v1', 'title': 'The Largest Rock in our Solar System',
     'url': 'https://apod.nasa.gov/apod/image/2301/PaleBlueDotOrig_Voyager1_960.jpg'},
    {'concepts': 'concept_tags functionality turned off in current service', 'copyright': 'Tunc Tezel',
     'date': '2023-01-02',
     'explanation': "Look up tonight and see a whole bunch of planets. Just after sunset, looking west, planets Venus, Saturn, Jupiter and Mars will all be simultaneously visible. Listed west to east, this planetary lineup will have Venus nearest the horizon, but setting shortly after the Sun.  It doesn't matter where on Earth you live because this early evening planet parade will be visible through clear skies all around the globe.  Taken late last month, the featured image captured all of these planets and more: the Moon and planet Mercury were also simultaneously visible.  Below visibility were the planets Neptune and Uranus, making this a nearly all-planet panorama. In the foreground are hills around the small village of Gökçeören, Kaş, Turkey, near the Mediterranean coast.  Bright stars Altair, Fomalhaut, and Aldebaran are also prominent, as well as the Pleiades star cluster. Venus will rise higher in the sky at sunset as January continues, but Saturn will descend.",
     'hdurl': 'https://apod.nasa.gov/apod/image/2301/AllPlanets_Tezel_1680_annotated.jpg', 'media_type': 'image',
     'service_version': 'v1', 'title': 'After Sunset Planet Parade',
     'url': 'https://apod.nasa.gov/apod/image/2301/AllPlanets_Tezel_1080_annotated.jpg'},
    {'concepts': 'concept_tags functionality turned off in current service', 'copyright': 'Tommy Lease',
     'date': '2023-01-03',
     'explanation': "This line of stars is real. A little too faint to see with the unaided eye, Kemble’s Cascade of stars inspires awe when seen with binoculars.  Like the Big Dipper though, Kemble’s Cascade is an asterism, not a constellation. The asterism is visible in the northern sky toward the long-necked constellation of the Giraffe (Camelopardalis). This string of about 20 unrelated stars, each of similar brightness, spans over five times the angular width of the full moon. Stretching diagonally from the upper left to the lower right, Kemble's Cascade was popularized last century by astronomy enthusiast Lucian Kemble.  The bright object near the top left of the image is the relatively compact Jolly Roger open cluster of stars, officially designated as NGC 1502.",
     'hdurl': 'https://apod.nasa.gov/apod/image/2301/KembleCascade_Lease_3668.jpg', 'media_type': 'image',
     'service_version': 'v1', 'title': 'Kemble’s Cascade of Stars',
     'url': 'https://apod.nasa.gov/apod/image/2301/KembleCascade_Lease_960.jpg'},
    {'concepts': 'concept_tags functionality turned off in current service', 'copyright': 'Mike Selby',
     'date': '2023-01-04',
     'explanation': 'Can a gas cloud eat a galaxy?  It\'s not even close.  The "claw" of this odd looking "creature" in the featured photo is a gas cloud known as a cometary globule.  This globule, however, has ruptured.  Cometary globules are typically characterized by dusty heads and elongated tails.  These features cause cometary globules to have visual similarities to comets, but in reality they are very much different.  Globules are frequently the birthplaces of stars, and many show very young stars in their heads. The reason for the rupture in the head of this object is not yet known. The galaxy to the left of the globule is huge, very far in the distance, and only placed near CG4 by chance superposition.   Discovery + Outreach: Graduate student research position open for APOD',
     'hdurl': 'https://apod.nasa.gov/apod/image/2301/cg4_selby_5430.jpg', 'media_type': 'image',
     'service_version': 'v1', 'title': 'CG4: The Globule and the Galaxy',
     'url': 'https://apod.nasa.gov/apod/image/2301/cg4_selby_960.jpg'},
    {'concepts': 'concept_tags functionality turned off in current service', 'copyright': 'Stefan Thrun',
     'date': '2023-01-05',
     'explanation': "Hurtling through a cosmic dust cloud a mere 400 light-years away, the lovely Pleiades or Seven Sisters open star cluster is well-known for its striking blue reflection nebulae. It lies in the night sky toward the constellation Taurus and the Orion Arm of our Milky Way galaxy. The sister stars are not related to the dusty cloud though. They just happen to be passing through the same region of space. Known since antiquity as a compact grouping of stars, Galileo first sketched the star cluster viewed through his telescope with stars too faint to be seen by eye. Charles Messier recorded the position of the cluster as the 45th entry in his famous catalog of things which are not comets. In Greek myth, the Pleiades were seven daughters of the astronomical titan Atlas and sea-nymph Pleione. Their parents names are included in the cluster's nine brightest stars. This well-processed, color-calibrated telescopic image features pin-point stars and detailed filaments of interstellar dust captured in over 9 hours of exposure. It spans more than 20 light-years across the Pleiades star cluster.",
     'hdurl': 'https://apod.nasa.gov/apod/image/2301/M_45_Plejarden_Stefan_Thrun_klein4096.jpg', 'media_type': 'image',
     'service_version': 'v1', 'title': 'Messier 45: The Daughters of Atlas and Pleione',
     'url': 'https://apod.nasa.gov/apod/image/2301/M_45_Plejarden_Stefan_Thrun_klein1024.jpg'}]

content = []
@app.route("/", methods=['GET', 'POST'])
def index():
    # form1_content = 'Содержимое формы 1'
    # form2_content = 'Содержимое формы 2'
    form_content = ''
    switch = ''
    default_value = "1"
    data = []
    content = []
    if request.method == 'POST':
        form_type = request.form['form1']
        if form_type == 'data':
            form_content = 'Поле data введите дату в формате YYYY-MM-DD'
            switch = "data"
            default_value = "1"
            date = request.form.get('date0')
            if date is not None:
                data.append(date)
                date_nasa = Api_Nasa(date_str=date)
                content.append(date_nasa.get_response())

        elif form_type == 'cnt':
            form_content = 'Поле Cnt введите число n, такое что 0 < n <= 100'
            switch = "cnt"
            default_value = "2"
            num = request.form.get('num')
            if num is not None:
                data.append(num)
                date_nasa = Api_Nasa(count=num)
                content = date_nasa.get_response()

        elif form_type == 'rng':
            form_content = 'Поле Range of data: введите 2 даты в формате YYYY-MM-DD'
            switch = "rng"
            default_value = "3"
            date1 = request.form.get('date1')
            date2 = request.form.get('date2')
            if date1 is not None and date2 is not None:
                data.append(date1)
                data.append(date2)
                date_nasa = Api_Nasa(start_date=date1, end_date=date2)
                tmp = date_nasa.get_response()
                if type(tmp) == list:
                    content = tmp
                else:
                    content.append(tmp)

    else:
        form_content = ''
    # tt = request.form.items()
    # print(request.form.get('date0'))
    print(content)
    return render_template('index.html', name="Peer", elements=content,
                           form_content="", list_get=data,
                           switch=switch, default_value=default_value, develop=False)
