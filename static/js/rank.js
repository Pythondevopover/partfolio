let slideIndex = 1;
showSlides(slideIndex);

// Tugmalarni bosganda funksiyani chaqirish
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Hozirgi slaydni ko‘rsatish
function showSlides(n) {
    let slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) { slideIndex = 1; }    
    if (n < 1) { slideIndex = slides.length; }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slides[slideIndex-1].style.display = "block";  
}
