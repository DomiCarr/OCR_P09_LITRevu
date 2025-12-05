// reviews/static/reviews/js/review.js
document.addEventListener('DOMContentLoaded', () => {
    // ---------------- Ticket fields ----------------
    const titleInput = document.getElementById("title");
    const descInput = document.getElementById("description");
    const inputImage = document.getElementById("image");
    const preview = document.getElementById("image_preview");
    const fileBtn = document.getElementById("fileBtn");

    if (fileBtn && inputImage) {
        fileBtn.addEventListener("click", () => inputImage.click());
        inputImage.style.display = "none";
    }

    // ---------------- Review fields ----------------
    const reviewTitre = document.getElementById("titre");
    const reviewCommentaire = document.getElementById("commentaire");
    const reviewRadios = document.querySelectorAll('input[name="note"]');

    const submitBtn = document.getElementById("submitBtn");

    // ---------------- Check function ----------------
    function checkFields() {
        const hasTicketForm = titleInput || descInput || inputImage;

        let okTicket = true;
        if (hasTicketForm) {
            okTicket =
                titleInput?.value.trim().length > 0 &&
                descInput?.value.trim().length > 0 &&
                preview?.src && preview.src.trim() !== "";
        }

        const okReview =
            reviewTitre && reviewTitre.value.trim().length > 0 &&
            reviewCommentaire && reviewCommentaire.value.trim().length > 0 &&
            Array.from(reviewRadios).some(r => r.checked);

        submitBtn.disabled = !(okTicket && okReview);
    }

    // ---------------- Event listeners ----------------
    [titleInput, descInput, reviewTitre, reviewCommentaire].forEach(el => {
        if (el) el.addEventListener("input", checkFields);
    });

    reviewRadios.forEach(r => r.addEventListener("change", checkFields));

    if (inputImage) {
        inputImage.addEventListener("change", () => {
            const file = inputImage.files[0];
            if (file) {
                preview.src = URL.createObjectURL(file);
                preview.style.display = "block";
            } else {
                preview.src = "";
                preview.style.display = "none";
            }
            checkFields();
        });
    }

    // Initial check
    checkFields();
});
