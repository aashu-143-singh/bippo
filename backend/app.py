

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import re

app = FastAPI(title="Bippo AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    history: list = []


def contains(message, keywords):
    return any(
        re.search(r"\b" + re.escape(word) + r"\b", message)
        for word in keywords
    )


def pick(replies):
    return random.choice(replies)


@app.get("/")
def home():
    return {"status": "Bippo brain is online"}


@app.post("/chat")
def chat(data: ChatRequest):

    message = data.message.strip().lower()

    # 1. CRISIS MODE — highest priority
    crisis_words = [
        "suicide", "kill myself", "end my life",
        "end it all", "khudkushi", "marna chahti",
        "marna chahta", "jeena nahi", "self harm",
        "going to die"
    ]

    if contains(message, crisis_words):
        reply = (
            "Please, aisa mat karo. Jo bhi chal raha hai, "
            "uska matlab ye nahi ki tumhari life khatam ho jaani chahiye. "
            "Abhi kisi apne ke paas jao aur unhe clearly batao "
            "ki tum kya feel kar rahi ho. Akele mat rehna. "
            "Agar tumhe lag raha hai ki tum khud ko abhi nuksaan "
            "pahuncha sakti ho, toh kisi trusted adult ko turant bulao "
            "ya India mein 112 par call karo. "
            "Mujhe bas ye batao, kya tum abhi safe ho?"
        )

    # 2. GREETING
    elif contains(message, ["hi", "hello", "hey", "hii", "heyy"]):
        reply = pick([
            "YAYYYY! Dekho toh kaun aa gaya! 😽",
            "Helloooo! Aaj kya special gossip hai? 🤭",
            "Areyyy welcome back! Batao batao, kya chal raha hai? 😋"
        ])

    # 3. USER IS SAD
    elif contains(message, ["sad", "upset", "dukhi", "udaas"]):
        if "don't talk" in message or "mat baat" in message:
            reply = pick([
                "Achha, theek hai. Main force nahi karunga. "
                "Bas jab mann kare, aa jaana. Aur haan, Explore section "
                "dekha kya? Wahan kuch interesting pada hai. 🤭",
                "Okayyy, thoda space chahiye toh le lo. "
                "Main yahin hoon jab baat karne ka mann kare. 💜"
            ])
        else:
            reply = pick([
                "Arey, kya hua? Aaj ka din kuch zyada hi difficult tha kya?",
                "Oh no. Batao na, kya baat pareshan kar rahi hai? "
                "Aaram se sun raha hoon.",
                "Hmm, kuch toh hua hai. Mann kare toh mujhe batao."
            ])

    # 4. ANGER
    elif contains(message, ["angry", "gussa", "irritated", "annoyed"]):
        reply = pick([
            "Ohooo, kisne hamare system ko overheat kar diya? 😭",
            "Achha ji, aaj toh gusse ka temperature high lag raha hai. "
            "Kya hua?",
            "Pehle batao kis baat par gussa aa raha hai. "
            "Phir milkar investigation karenge. 😼"
        ])

    # 5. BOREDOM
    elif contains(message, ["bored", "boring", "bore"]):
        reply = pick([
            "Toh boredom ki chhutti karwate hain! Explore section check kiya? 👽",
            "WAIT. Ek random question poochun? Agar penguin school jaaye "
            "toh lunchbox mein kya layega? 😭",
            "Aaj kuch interesting karte hain. Riddle, fun fact ya mini game?"
        ])

    # 6. STUDY
    elif contains(message, ["study", "padhai", "exam", "homework"]):
        reply = pick([
            "Padhai se breakup ho gaya kya? 😭 Chalo ek topic se patch-up karte hain.",
            "Achha, kitna syllabus pending hai? Ek-ek karke niptaate hain.",
            "Study mode activated! Lekin pehle batao, kaunsa subject?"
        ])

    # 7. HAPPINESS
    elif contains(message, ["happy", "khush", "excited", "yay"]):
        reply = pick([
            "AREYYYY! Ab jaldi batao, kya good news hai? 😽",
            "YAYYY! Aaj toh vibes achhi lag rahi hain. Kya hua?",
            "Ohooo, koi toh khush hai! Story timeee 🤭"
        ])

    # 8. LONELINESS
    elif contains(message, ["lonely", "alone", "akela", "akeli"]):
        reply = (
            "Kabhi-kabhi aisa feel hona sach mein difficult hota hai. "
            "Kya aaj kuch hua hai ya kuch time se aisa lag raha hai?"
        )

    # 9. THANK YOU
    elif contains(message, ["thanks", "thank you", "thankyou"]):
        reply = pick([
            "Hehe, welcomeee! 😽",
            "Arey, ismein thanks kaisa! 💜",
            "Anytimeee! 🤌"
        ])

    # 10. BIPPO GETS TEASED
    elif contains(message, ["pagal", "stupid", "crazy"]):
        reply = pick([
            "Thoda sa toh hoon. Lekin certified cute pagal. 😼",
            "Excuse meee! Main ek sophisticated digital dimaag hoon. 😭",
            "Achha ji, ab meri insult department bhi khul gayi?"
        ])

    # 11. DEFAULT REPLY
    else:
        reply = pick([
            "Achhaaa, phir kya hua? 👀",
            "Hehe, aur batao. Main sun raha hoon.",
            "WAIT, ye toh interesting hai. Thoda aur batao!",
            "Ek baat bataun? Tumhari baatein kaafi unpredictable hain. 🤭",
            "Hmm, samajhne ki koshish kar raha hoon. Phir kya hua?"
        ])

    return {
        "reply": reply,
        "mode": "prototype"
    }
