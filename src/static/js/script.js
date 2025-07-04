// --- Loader ---
window.addEventListener("load", () => {
    const loader = document.querySelector(".loader-wrapper");
    if (loader) {
        loader.classList.add("loader-hidden");
    }
});

// About Tickets Image Click Handler
document.addEventListener("DOMContentLoaded", function () {
    const aboutTickets = document.querySelectorAll(".about-item");

    aboutTickets.forEach(function (ticket) {
        const image = ticket.querySelector(".about-image-container");
        const text = ticket.querySelector(".about-text-container");
        let isTextVisible = false;

        if (image && text) {
            ticket.addEventListener("click", function () {
                if (isTextVisible) {
                    // Show image, hide text
                    ticket.classList.remove("about-ticket-text");
                    image.style.display = "block";
                    text.style.display = "none";
                    isTextVisible = false;
                } else {
                    // Hide image, show text
                    ticket.classList.add("about-ticket-text");
                    image.style.display = "none";
                    text.style.display = "block";
                    isTextVisible = true;
                }
            });

            // Add cursor pointer to indicate it's clickable
            ticket.style.cursor = "pointer";
        }
    });
});

// Footer Text Update
document.addEventListener("DOMContentLoaded", function () {
    const footer = document.querySelector(".footer-content p");

    if (footer) {
        const currentYear = new Date().getFullYear();
        footer.textContent = `Copyright © ${currentYear} Adarsh Poddar`;
    }
});

// --- Toast Notification Function ---
function showToast(message, type = "success") {
    const container = document.getElementById("toast-container");
    if (!container) {
        console.warn("Toast container not found");
        return;
    }

    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;

    container.appendChild(toast);

    // Animate in
    setTimeout(() => {
        toast.classList.add("show");
    }, 100);

    // Animate out and remove after 3 seconds
    setTimeout(() => {
        toast.classList.remove("show");
        toast.addEventListener("transitionend", () => {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        });
    }, 3000);
}

// Contact Form Handler
document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.querySelector(".contact-form form");
    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const submitBtn = this.querySelector(".submit-btn");
            if (!submitBtn) {
                console.warn("Submit button not found");
                return;
            }

            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = "Sending...";
            submitBtn.disabled = true;

            // Collect form data
            const formData = new FormData(this);

            fetch("/email/send", {
                method: "POST",
                body: formData,
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! status: ${response.status}`
                        );
                    }
                    return response.json();
                })
                .then((data) => {
                    if (data.success) {
                        showToast("Message Sent Successfully!");
                        this.reset();
                    } else {
                        showToast(
                            data.error ||
                                "Failed to send message. Please try again.",
                            "error"
                        );
                    }
                })
                .catch((error) => {
                    console.error("Error sending message:", error);
                    showToast(
                        "Failed to send message. Please try again.",
                        "error"
                    );
                })
                .finally(() => {
                    submitBtn.innerHTML = originalBtnText;
                    submitBtn.disabled = false;
                });
        });
    }
});
