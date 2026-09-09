from flask import Flask, render_template, abort

app = Flask(__name__)


# --------------------------------------------------
# HEALTH EDUCATION CONTENT
# --------------------------------------------------

AWARENESS_AREAS = {

    "breasts": {
        "title": "Breast Awareness",
        "image": "breasts.jpg",
        "subtitle": "Know what is normal for you.",

        "intro": (
            "Breast awareness means becoming familiar with how your "
            "breasts normally look and feel so that you can notice "
            "a new or unusual change."
        ),

        "look_for": [
            "A new lump or swelling in the breast or armpit.",
            "A change in the size or shape of the breast.",
            "A change in the appearance of the skin.",
            "A change in the nipple or nipple position.",
            "Unusual nipple discharge.",
            "A persistent change that is unusual for you."
        ],

        "what_to_do": (
            "If you notice a new or unusual change, do not try to "
            "diagnose it yourself. Arrange an assessment with a "
            "qualified healthcare professional."
        ),

        "note": (
            "Many breast changes are caused by conditions other than "
            "cancer. A healthcare professional can determine what "
            "the change means."
        )
    },


    "groin": {
        "title": "Groin & Testicular Awareness",
        "image": "groin.jpg",
        "subtitle": "Know your normal.",

        "intro": (
            "Being familiar with your normal testicular size, shape "
            "and feel can help you notice changes that may need "
            "professional assessment."
        ),

        "look_for": [
            "A new lump or swelling in a testicle.",
            "A change in the size or shape of a testicle.",
            "A feeling of heaviness or an unusual change in the scrotum.",
            "Persistent discomfort or pain.",
            "A change that is new or unusual for you."
        ],

        "what_to_do": (
            "If you notice a new or persistent change, speak with "
            "a qualified healthcare professional. Do not rely on "
            "self-checking to diagnose a condition."
        ),

        "note": (
            "There are many possible causes of changes in this area. "
            "A healthcare professional can examine the change and "
            "decide whether further tests are needed."
        )
    },


    "neck": {
        "title": "Neck Awareness",
        "image": "neck.jpg",
        "subtitle": "Pay attention to persistent changes.",

        "intro": (
            "The neck contains lymph nodes and other structures that "
            "can become swollen for many different reasons. Knowing "
            "what is normal for you can help you notice persistent changes."
        ),

        "look_for": [
            "A new lump or swelling in the neck.",
            "A lump that does not go away.",
            "A change that continues to grow or change.",
            "Persistent changes accompanied by other concerning symptoms.",
            "An unusual change that is not normal for you."
        ],

        "what_to_do": (
            "A new or persistent neck lump should be discussed with "
            "a healthcare professional, particularly if it does not "
            "settle or is getting larger."
        ),

        "note": (
            "Swollen lymph nodes are commonly caused by infections "
            "and other conditions. A lump does not automatically mean "
            "cancer."
        )
    },


    "armpits": {
        "title": "Armpit Awareness",
        "image": "armpits.jpg",
        "subtitle": "Be aware of new or persistent changes.",

        "intro": (
            "The armpits contain lymph nodes and other tissues. "
            "Becoming familiar with the area can help you notice "
            "unusual changes."
        ),

        "look_for": [
            "A new lump or swelling.",
            "A lump that remains or continues to grow.",
            "Persistent swelling or an unusual change.",
            "A change that occurs together with another unusual change.",
            "Anything that feels noticeably different from normal."
        ],

        "what_to_do": (
            "If you notice a new or persistent lump or swelling, "
            "speak with a healthcare professional for an assessment."
        ),

        "note": (
            "Lymph nodes can enlarge because of infections and other "
            "non-cancerous causes. Only a professional assessment can "
            "determine the cause of a persistent change."
        )
    },


    "skin": {
        "title": "Skin Awareness",
        "image": "skin.jpg",
        "subtitle": "Notice new or changing skin marks.",

        "intro": (
            "Skin awareness means paying attention to new or changing "
            "moles, spots, marks or other persistent changes."
        ),

        "look_for": [
            "A new mole or unusual skin mark.",
            "A mole or mark that changes in size.",
            "A change in shape or colour.",
            "A mark that looks noticeably different from your other marks.",
            "A skin change that does not heal or keeps changing."
        ],

        "what_to_do": (
            "If you notice a new or changing skin mark that concerns "
            "you, arrange an assessment with a qualified healthcare "
            "professional."
        ),

        "note": (
            "Most skin marks are not cancer. However, a new or changing "
            "mark should not be ignored simply because it does not hurt."
        )
    },


    "mouth": {
        "title": "Mouth & Throat Awareness",
        "image": "mouth.jpg",
        "subtitle": "Pay attention to persistent changes.",

        "intro": (
            "Becoming familiar with your mouth and throat can help "
            "you notice unusual changes that persist."
        ),

        "look_for": [
            "A mouth sore or ulcer that does not heal.",
            "An unusual red or white patch.",
            "A persistent lump or swelling.",
            "Persistent changes involving swallowing.",
            "A persistent change in your voice.",
            "Another unusual change that does not go away."
        ],

        "what_to_do": (
            "If an unusual mouth or throat change persists, speak "
            "with a qualified healthcare professional, dentist or "
            "other appropriate healthcare provider."
        ),

        "note": (
            "Many mouth and throat problems are caused by conditions "
            "other than cancer. Persistent changes should nevertheless "
            "be professionally assessed."
        )
    }
}


# --------------------------------------------------
# MAIN PAGES
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/self-check")
def self_check():
    return render_template(
        "self_check.html",
        areas=AWARENESS_AREAS
    )


@app.route("/area/<area_name>")
def area(area_name):

    if area_name not in AWARENESS_AREAS:
        abort(404)

    area_data = AWARENESS_AREAS[area_name]

    return render_template(
        "area.html",
        area=area_data
    )
@app.route("/warning-signs")
def warning_signs():
    return render_template("warning_signs.html")


@app.route("/myths")
def myths():
    return render_template("myths.html")


@app.route("/healthcare")
def healthcare():
    return render_template("healthcare.html")


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run()