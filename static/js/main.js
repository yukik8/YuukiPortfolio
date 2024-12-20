document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap modal
    const photoModal = new bootstrap.Modal(document.getElementById('photoModal'));
    
    // Get all photo containers
    const photoContainers = document.querySelectorAll('.photo-container');
    
    // Add click event listener to each photo
    photoContainers.forEach(container => {
        container.addEventListener('click', function() {
            const modal = document.getElementById('photoModal');
            const modalTitle = modal.querySelector('.modal-title');
            const modalImg = modal.querySelector('.modal-body img');
            const modalDescription = modal.querySelector('.photo-description');
            
            // Get photo data from data attributes
            const title = this.dataset.title;
            const description = this.dataset.description;
            const imgSrc = this.querySelector('img').src;
            
            // Set modal content
            modalTitle.textContent = title;
            modalImg.src = imgSrc;
            modalImg.alt = title;
            modalDescription.textContent = description;
            
            // Show modal
            photoModal.show();
        });
    });
    
    // Optional: Add loading animation for images
    const images = document.querySelectorAll('.photo-container img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = 1;
        });
    });
});
