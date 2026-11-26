

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import random

app = FastAPI(title="Bippo Mental Wellness Companion")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    history: list = Field(default_factory=list)


def pick(replies):
    return random.choice(replies)


def get_reply(message):
    message = message.lower().strip()

    # 1. Serious safety mode
    crisis_phrases = [
        "suicide",
        "kill myself",
        "end my life",
        "want to die",
        "don't want to live",
        "do not want to live",
        "dont want to live",
        "no reason to live",
        "hurt myself",
        "harm myself",
        "self harm",
        "khud ko nuksan",
        "khud ko maar",
        "jeena nahi chahti",
        "jeena nahi chahta",
        "mar jana chahti",
        "mar jana chahta",
        "zindagi khatam"
    ]

    if any(phrase in message for phrase in crisis_phrases):
        return (
            "Hey, ek minute meri baat suno. Mujhe nahi pata tum "
            "kitne mushkil waqt se guzar rahi ho, but please ye mat "
            "sochna ki tumhari kahani yahin khatam ho gayi.\n\n"
            "Life mein bahut ups and downs aate hain. Kabhi-kabhi "
            "sab kuch itna difficult lagta hai ki aage kuch achha "
            "imagine karna bhi mushkil ho jata hai. Lekin abhi tumhe "
            "apni poori life solve nahi karni. Bas is moment ko "
            "akele face mat karo.\n\n"
            "Chalo, kisi apne ke paas chalte hain — friend, family "
            "member ya trusted adult. Unse saamne baithkar baat karo. "
            "Agar bolna mushkil lag raha hai, toh unhe apna message "
            "dikha dena.\n\n"
            "Agar tumhe lag raha hai ki tum abhi khud ko safe nahi "
            "rakh paogi, toh turant kisi trusted adult ko bulao, "
            "India mein 112 par call karo ya nearest emergency "
            "department jao. Professional support ke liye "
            "Tele-MANAS 14416 bhi available hai.\n\n"
            "Bas mujhe ek baat batao: kya tum abhi safe ho, "
            "aur kya tumhare paas koi hai jiske saath tum baith sakti ho?"
        ), "serious"

    # 2. User wants space
    if any(phrase in message for phrase in [
        "don't talk to me",
        "do not talk to me",
        "leave me alone",
        "i need space",
        "mujhe akela chhod do",
        "baat nahi karni"
    ]):
        return pick([
            "Achha, koi baat nahi. Main force nahi karungi. "
            "Thoda apne liye time lo. Jab mann ho, baat kar lena.",
            "Theek hai, no pressure. Kabhi-kabhi thoda space "
            "bhi zaroori hota hai. Take your time."
        ]), "space"

    # 3. Greetings
    if any(word in message for word in [
        "hello", "hi", "hey", "hii", "heyy"
    ]):
        return pick([
            "Areyyy, tum wapas aa gayi! Batao, aaj ka din kaisa raha?",
            "Hiii! Kya haal chaal? Aaj mann kaisa hai?",
            "Ohh, look who's here! Batao kya chal raha hai?"
        ]), "greeting"

    # 4. Sadness
    if any(word in message for word in [
        "sad", "upset", "crying", "unhappy",
        "feeling low", "down", "dukhi", "rona",
        "mann udaas", "mood off"
    ]):
        return pick([
            "Ohh... kya hua? Kuch specific hua hai ya bas aaj "
            "mann thoda heavy lag raha hai? Bina jaldi kiye batao.",
            "Kabhi-kabhi bina kisi clear reason ke bhi mann udaas "
            "ho jata hai. Tum bata sakti ho, kya chal raha hai?",
            "I'm listening. Jo bhi feel ho raha hai, use explain "
            "karne ke liye perfect words ki zarurat nahi hai."
        ]), "sadness"

    # 5. Anxiety and overthinking
    if any(word in message for word in [
        "anxious", "anxiety", "nervous", "worried",
        "panic", "overthinking", "ghabrahat", "dar lag raha"
    ]):
        return pick([
            "Lag raha hai dimaag mein bahut kuch ek saath chal raha "
            "hai. Sabse zyada kis baat ki tension ho rahi hai?",
            "Ek minute, thoda slow karte hain. Abhi sab kuch "
            "figure out karna zaroori nahi hai. Kya hua?",
            "Overthinking kabhi-kabhi chhoti si baat ko bhi "
            "bahut bada bana deti hai. Batao, kya soch rahi ho?"
        ]), "anxiety"

    # 6. Stress and pressure
    if any(word in message for word in [
        "stressed", "stress", "overwhelmed",
        "too much", "pressure", "exhausted", "thak gayi"
    ]):
        return pick([
            "Uff, lagta hai bahut kuch ek saath handle karna pad "
            "raha hai. Sabse zyada heavy kya lag raha hai?",
            "Tumhe abhi sab kuch ek saath solve karne ki zarurat "
            "nahi. Ek-ek karke baat karte hain.",
            "That sounds exhausting. Tum chaho toh pehle bas "
            "apni baat share karo, solutions baad mein dekhenge."
        ]), "stress"

    # 7. Loneliness
    if any(word in message for word in [
        "lonely", "alone", "nobody cares",
        "no one understands", "akela", "tanha",
        "koi nahi hai"
    ]):
        return pick([
            "Kabhi-kabhi log aas-paas hote hain, phir bhi akelapan "
            "feel hota hai. Kya tumhare saath bhi aisa ho raha hai?",
            "Ye feeling easy nahi hoti. Kya koi aisa hai jisse "
            "tum bina judge hue baat kar pao?",
            "Main tumhari baat samajhne ki koshish kar rahi hoon. "
            "Kab se aisa feel ho raha hai?"
        ]), "loneliness"

    # 8. Anger
    if any(word in message for word in [
        "angry", "anger", "frustrated", "irritated",
        "gussa", "annoyed"
    ]):
        return pick([
            "Arey, kya ho gaya? Kis baat ne itna irritate kar diya?",
            "Sounds like something really got to you. Batao, "
            "kya hua?",
            "Theek hai, pehle gussa nikalne do. Main sun rahi hoon."
        ]), "anger"

    # 9. Feeling empty or numb
    if any(word in message for word in [
        "numb", "empty", "nothing matters",
        "feel nothing", "blank", "andar se khaali"
    ]):
        return pick([
            "Andar se empty feel hona kaafi confusing ho sakta hai. "
            "Kya ye feeling kuch time se chal rahi hai?",
            "Tumhe abhi apni feelings ko perfectly explain "
            "karne ki zarurat nahi. Thoda bataogi kya chal raha hai?",
            "I'm taking this seriously. Kya recently kuch badla hai?"
        ]), "emotional_support"

    # 10. Positive mood
    if any(word in message for word in [
        "happy", "good day", "excited",
        "feeling great", "khush", "wonderful"
    ]):
        return pick([
            "Areyyy, ye toh achhi baat hai! Aaj aisa kya hua?",
            "Oho! Aaj toh mood achha lag raha hai. Koi good news?",
            "Yay, tell me! Kya special hua aaj?"
        ]), "positive"

    # 11. Thanks
    if any(word in message for word in [
        "thank you", "thanks", "thx", "shukriya"
    ]):
        return pick([
            "Arey, you're welcome! Apna khayal rakhna.",
            "Koi baat nahi. Jab mann ho, baat kar lena.",
            "Anytime! Aur haan, khud ke saath thoda gentle rehna."
        ]), "general"

    # 12. Playful teasing
    if any(phrase in message for phrase in [
        "tum pagal ho",
        "are you mad",
        "you are crazy",
        "stupid bippo"
    ]):
        return pick([
            "Thodi si toh hoon, warna tumhari itni complicated "
            "baatein kaun sunta? 🤭",
            "Achha ji! Ab Bippo ki complaint bhi hone lagi?",
            "Main toh innocent hoon, tum hi mujhe bigaad rahe ho!"
        ]), "playful"

    # 13. Default response
    return pick([
        "Achha, phir batao... thoda aur samjhaogi?",
        "Hmm, main samajhne ki koshish kar rahi hoon. "
        "Tumhare mind mein exactly kya chal raha hai?",
        "Bina jaldi kiye batao. I'm listening.",
        "Okaay, aur batao. Main tumhari baat sun rahi hoon."
    ]), "general"


@app.get("/")
def home():
    return {"status": "Bippo brain is online"}


@app.post("/chat")
def chat(data: ChatRequest):
    reply, mode = get_reply(data.message)

    return {
        "reply": reply,
        "mode": mode
    }
