// =========================
// MOOD SCALE
// =========================

const moodCards = document.querySelectorAll(".mood-card");
const moodMessage = document.getElementById("mood-message");

moodCards.forEach(function(card) {

    card.addEventListener("click", function() {

        // Remove selected class from all cards
        moodCards.forEach(function(item) {
            item.classList.remove("selected");
        });

        // Select clicked card
        card.classList.add("selected");

        // Get mood
        const mood = card.dataset.mood;


        // Bippo's response
        if (mood === "very-low") {

            moodMessage.textContent =
                "I'm sorry today feels a little heavy. I'm here with you. 💛";

        }

        else if (mood === "low") {

            moodMessage.textContent =
                "It's okay to have a low day. Take things one step at a time. 🌷";

        }

        else if (mood === "neutral") {

            moodMessage.textContent =
                "Some days are simply okay-ish, and that's perfectly fine. 🌱";

        }

        else if (mood === "good") {

            moodMessage.textContent =
                "I'm glad you're having a good day! Keep smiling. 💙";

        }

        else if (mood === "very-good") {

            moodMessage.textContent =
                "Yayy! Bippo is happy to see you feeling this good! ✨💛";

        }


        // Show message
        moodMessage.parentElement.classList.add("show");


        // Hide after 3 seconds
        setTimeout(function() {

            moodMessage.parentElement.classList.remove("show");

        }, 3000);

    });

});



// =========================
// BIPPO TINY BREAK GAME
// =========================

const gameArea = document.getElementById("gameArea");
const gameBippo = document.getElementById("gameBippo");
const thoughtBubble = document.getElementById("thoughtBubble");
const gameMessage = document.getElementById("gameMessage");
const startGame = document.getElementById("startGame");


// Only run game if all game elements exist
if (
    gameArea &&
    gameBippo &&
    thoughtBubble &&
    gameMessage &&
    startGame
) {

    const thoughts = [
        "breathe 🌿",
        "pause ☁️",
        "smile ✨"
    ];


    let currentThought = 0;
    let gameRunning = false;


    // =========================
    // START GAME
    // =========================

    startGame.addEventListener("click", function() {

        gameRunning = true;

        currentThought = 0;

        gameMessage.textContent =
            "Catch Bippo! 💜";

        thoughtBubble.textContent =
            thoughts[currentThought];

        startGame.textContent =
            "Game Running ✨";

        moveBippo();

    });



    // =========================
    // CLICK BIPPO
    // =========================

    gameBippo.addEventListener("click", function() {

        if (!gameRunning) {
            return;
        }


        // Go to next thought
        currentThought++;


        // =========================
        // GAME FINISHED
        // =========================

        if (currentThought >= thoughts.length) {

            gameRunning = false;

            thoughtBubble.textContent = "✨";

            gameMessage.textContent =
                "You caught them all! ✨ That was your tiny Bippo break.";

            startGame.textContent =
                "Play Again";

            return;
        }


        // =========================
        // NEXT THOUGHT
        // =========================

        thoughtBubble.textContent =
            thoughts[currentThought];

        gameMessage.textContent =
            "Yay! Now catch Bippo again! 💜";

        moveBippo();

    });



    // =========================
    // MOVE BIPPO
    // =========================

    function moveBippo() {

        const areaWidth =
            gameArea.clientWidth;

        const areaHeight =
            gameArea.clientHeight;


        const bippoWidth =
            gameBippo.offsetWidth;

        const bippoHeight =
            gameBippo.offsetHeight;


        const padding = 25;


        // Maximum position Bippo can reach
        const maxX =
            areaWidth - bippoWidth - padding;

        const maxY =
            areaHeight - bippoHeight - padding;


        // Random X position
        const randomX =
            padding +
            Math.floor(
                Math.random() *
                (maxX - padding)
            );


        // Random Y position
        const randomY =
            padding +
            Math.floor(
                Math.random() *
                (maxY - padding)
            );


        // Move Bippo
        gameBippo.style.left =
            randomX + "px";

        gameBippo.style.top =
            randomY + "px";


        // =========================
        // MOVE THOUGHT BUBBLE
        // =========================

        const bubbleX =
            Math.min(
                randomX + bippoWidth - 10,
                areaWidth - 150
            );


        const bubbleY =
            Math.max(
                randomY - 45,
                10
            );


        thoughtBubble.style.left =
            bubbleX + "px";

        thoughtBubble.style.top =
            bubbleY + "px";

    }

}