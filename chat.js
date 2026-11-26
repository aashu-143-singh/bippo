/* =========================================
   BIPPO — CHAT FUNCTIONALITY
========================================= */

// AI backend URL (will be configured when backend is ready)
const API_URL = " https://bippo-1.onrender.com/  ";

// DOM elements
const chatMessages = document.getElementById("chatMessages");
const welcomeScreen = document.getElementById("welcomeScreen");
const messagesList = document.getElementById("messagesList");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");

const newChatBtn = document.getElementById("newChatBtn");
const clearChatBtn = document.getElementById("clearChatBtn");
const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
const historyBtn = document.getElementById("historyBtn");


// Conversation memory (kept only while page is open)
let conversation = [];
let isWaiting = false;


// =========================================
// TIME
// =========================================

function getTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}


// =========================================
// CREATE MESSAGE
// =========================================

function addMessage(text, sender) {

    const message = document.createElement("div");
    message.className = `message ${sender}`;

    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = sender === "bot" ? "B" : "U";

    const content = document.createElement("div");
    content.className = "message-content";

    const bubble = document.createElement("div");
    bubble.className = "message-bubble";

    // textContent prevents HTML injection
    bubble.textContent = text;

    const time = document.createElement("div");
    time.className = "message-time";
    time.textContent = getTime();

    content.appendChild(bubble);
    content.appendChild(time);

    message.appendChild(avatar);
    message.appendChild(content);

    messagesList.appendChild(message);

    scrollToBottom();

    return message;
}


// =========================================
// SCROLL
// =========================================

function scrollToBottom() {

    chatMessages.scrollTo({
        top: chatMessages.scrollHeight,
        behavior: "smooth"
    });
}


// =========================================
// TYPING INDICATOR
// =========================================

function showTyping() {

    const wrapper = document.createElement("div");
    wrapper.className = "message bot";
    wrapper.id = "typingMessage";

    const avatar = document.createElement("div");
    avatar.className = "message-avatar";
    avatar.textContent = "B";

    const content = document.createElement("div");
    content.className = "message-content";

    const indicator = document.createElement("div");
    indicator.className = "typing-indicator";

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement("span");
        indicator.appendChild(dot);
    }

    content.appendChild(indicator);
    wrapper.appendChild(avatar);
    wrapper.appendChild(content);

    messagesList.appendChild(wrapper);

    scrollToBottom();
}


function removeTyping() {
    const typing = document.getElementById("typingMessage");

    if (typing) {
        typing.remove();
    }
}


// =========================================
// INPUT CONTROLS
// =========================================

function updateSendButton() {

    const hasText = messageInput.value.trim().length > 0;

    sendBtn.disabled = !hasText || isWaiting;
}


messageInput.addEventListener("input", () => {

    // Automatically adjust textarea height
    messageInput.style.height = "auto";

    messageInput.style.height =
        Math.min(messageInput.scrollHeight, 150) + "px";

    updateSendButton();
});


// Enter = Send
// Shift + Enter = New line

messageInput.addEventListener("keydown", (event) => {

    if (
        event.key === "Enter" &&
        !event.shiftKey &&
        !event.isComposing
    ) {
        event.preventDefault();
        sendMessage();
    }
});


// =========================================
// SEND MESSAGE
// =========================================

async function sendMessage(customMessage = null) {

    if (isWaiting) return;

    const text = customMessage || messageInput.value.trim();

    if (!text) return;

    // Display welcome screen only once
    welcomeScreen.style.display = "none";

    // Display user's message
    addMessage(text, "user");

    // Store conversation context
    conversation.push({
        role: "user",
        content: text
    });

    messageInput.value = "";
    messageInput.style.height = "auto";

    isWaiting = true;
    updateSendButton();

    showTyping();


    try {

        // AI backend has not been configured yet
        if (!API_URL) {
            throw new Error("AI_NOT_CONNECTED");
        }

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: text,
                history: conversation
            })

        });


        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }


        const data = await response.json();

        const reply =
            data.reply ||
            data.message ||
            data.text;


        if (!reply || typeof reply !== "string") {
            throw new Error("Invalid AI response");
        }


        removeTyping();

        addMessage(reply, "bot");

        conversation.push({
            role: "assistant",
            content: reply
        });

    }


    catch (error) {

        removeTyping();

        console.error("Bippo AI error:", error);


        let errorMessage;


        if (error.message === "AI_NOT_CONNECTED") {

            errorMessage =
                "Hey, I'm Bippo! ♡ My AI connection is not set up yet, " +
                "but my chat interface is ready. We'll connect my brain " +
                "soon so I can properly listen and respond to you.";

        } else {

            errorMessage =
                "I'm having trouble connecting right now. " +
                "Your message hasn't been answered yet. " +
                "Please try again in a little while. ♡";
        }


        addMessage(errorMessage, "bot");
    }


    finally {

        isWaiting = false;
        updateSendButton();
        messageInput.focus();
    }
}


// =========================================
// SEND BUTTON
// =========================================

sendBtn.addEventListener("click", () => {
    sendMessage();
});


// =========================================
// SUGGESTION CARDS
// =========================================

document.querySelectorAll(".suggestion-card").forEach(card => {

    card.addEventListener("click", () => {

        const message = card.dataset.message;

        if (message) {
            sendMessage(message);
        }
    });
});


// =========================================
// NEW CHAT
// =========================================

function startNewChat() {

    conversation = [];

    messagesList.innerHTML = "";

    welcomeScreen.style.display = "block";

    messageInput.value = "";
    messageInput.style.height = "auto";

    updateSendButton();

    messageInput.focus();

    sidebar.classList.remove("open");
}


newChatBtn.addEventListener("click", startNewChat);


// =========================================
// CLEAR CHAT
// =========================================

clearChatBtn.addEventListener("click", () => {

    if (conversation.length === 0) return;

    const confirmed = confirm(
        "Clear this conversation? Messages will be removed from this chat."
    );

    if (confirmed) {
        startNewChat();
    }
});


// =========================================
// MOBILE SIDEBAR
// =========================================

menuBtn.addEventListener("click", () => {

    sidebar.classList.toggle("open");
});


// =========================================
// CONVERSATION HISTORY
// =========================================

historyBtn.addEventListener("click", () => {

    alert(
        "Conversation history is not available yet. " +
        "Your messages are kept only while this page is open."
    );
});


// =========================================
// INITIALIZATION
// =========================================

updateSendButton();

messageInput.focus();