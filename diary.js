// Find the elements from our HTML

const dateInput = document.getElementById("date");

const memoryInput = document.getElementById("memory");

const saveButton = document.getElementById("saveTicket");

const savedTickets = document.getElementById("savedTickets");


// Get previously saved tickets

let entries = JSON.parse(localStorage.getItem("bippoMemories")) || [];


// Function to show all saved tickets

function showEntries() {

    savedTickets.innerHTML = "";


    entries.forEach(function(entry) {

        const ticket = document.createElement("div");

        ticket.classList.add("saved-ticket");


        ticket.innerHTML = `
            <h3>🎟️ MEMORY TICKET</h3>

            <p><strong>Date:</strong> ${entry.date}</p>

            <p>${entry.memory}</p>
        `;


        savedTickets.appendChild(ticket);

    });
}


// Save button

saveButton.addEventListener("click", function() {

    const date = dateInput.value;

    const memory = memoryInput.value.trim();


    // Check if the user filled both fields

    if (date === "" || memory === "") {

        alert("Please choose a date and write a memory.");

        return;
    }


    // Create a new memory ticket

    const newEntry = {

        date: date,

        memory: memory

    };


    // Add the new ticket to our list

    entries.push(newEntry);


    // Save the list in the browser

    localStorage.setItem(
        "bippoMemories",
        JSON.stringify(entries)
    );


    // Clear the input boxes

    dateInput.value = "";

    memoryInput.value = "";


    // Show the new ticket on the page

    showEntries();


    alert("Memory Ticket Saved! 🎟️");

});


// Show old tickets when the page opens

showEntries();