document.addEventListener("DOMContentLoaded", function () {
    const quotes = [
        "Meditation is the key to a peaceful mind.",
        "Breathe in positivity, exhale stress.",
        "Calmness is the cradle of power.",
        "In stillness, the universe speaks.",
        "Inner peace begins the moment you choose not to allow anything to control your emotions."
    ];

    let index = 0;
    const quoteElement = document.getElementById("quote");

    function changeQuote() {
        quoteElement.style.opacity = "0";  // Fade Out
        setTimeout(() => {
            quoteElement.innerText = quotes[index];
            quoteElement.style.opacity = "1";  // Fade In
            index = (index + 1) % quotes.length;
        }, 1000);
    }

    setInterval(changeQuote, 4000); // Change quote every 4 seconds
});



// Tab Navigation Function
function openTab(event, tabName) {
    let i, tabContent, tabLinks;

    // Hide all tab content
    tabContent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }

    // Remove active class from all tab links
    tabLinks = document.getElementsByClassName("tab-link");
    for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].classList.remove("active");
    }

    // Show the clicked tab's content
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.classList.add("active");
}

// Set default active tab
document.addEventListener("DOMContentLoaded", () => {
    document.getElementsByClassName("tab-link")[0].click();
});
