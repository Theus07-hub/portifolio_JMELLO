function scrollCarousel(direction) {
    const carousel = document.getElementById('photoCarousel');
    if (carousel) {
        const scrollAmount = 280;
        carousel.scrollBy({
            left: direction * scrollAmount,
            behavior: 'smooth'
        });
    }
}

// ================= CARROSSEL AUTOMÁTICO INFINITO =================
let autoPlayInterval;

function startAutoPlay() {
    autoPlayInterval = setInterval(() => {
        const carousel = document.getElementById('photoCarousel');
        if (carousel) {
            const firstItem = carousel.querySelector('.carousel-item');
            if (firstItem) {
                // Roda suavemente para o lado
                carousel.scrollBy({ left: 250, behavior: 'smooth' });

                // Loop infinito perfeito: quando chega ao fim, move o primeiro item para o final
                setTimeout(() => {
                    const maxScrollLeft = carousel.scrollWidth - carousel.clientWidth;
                    if (carousel.scrollLeft >= maxScrollLeft - 10) {
                        carousel.appendChild(firstItem);
                        carousel.scrollLeft -= 280;
                    }
                }, 400);
            }
        }
    }, 3500); // Passa a cada 3.5 segundos
}

function stopAutoPlay() {
    clearInterval(autoPlayInterval);
}

document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('photoCarousel');
    if (carousel) {
        carousel.addEventListener('mouseenter', stopAutoPlay);
        carousel.addEventListener('mouseleave', startAutoPlay);
        startAutoPlay();
    }
});


// ================= ADICIONAR FOTOS DINAMICAMENTE =================
function addPhoto(event) {
    event.preventDefault();

    const titleInput = document.getElementById('photoTitle');
    const descInput = document.getElementById('photoDesc');
    const fileInput = document.getElementById('photoFile');
    const carousel = document.getElementById('photoCarousel');

    if (fileInput.files && fileInput.files.length > 0) {
        const titleBase = titleInput.value;
        const descBase = descInput.value;
        const files = Array.from(fileInput.files);

        files.forEach((file, index) => {
            const reader = new FileReader();

            reader.onload = function(e) {
                const imageUrl = e.target.result;
                const photoTitle = files.length > 1 ? `${titleBase} (${index + 1})` : titleBase;

                const item = document.createElement('div');
                item.className = 'carousel-item';
                item.innerHTML = `
                    <div class="item-actions">
                        <button class="edit-btn" title="Editar" onclick="editPhoto(this)"><i class="fa-solid fa-pen"></i></button>
                        <button class="delete-btn" title="Remover" onclick="deletePhoto(this)"><i class="fa-solid fa-trash"></i></button>
                    </div>
                    <h2>${photoTitle}</h2>
                    <p>${descBase}</p>
                    <div class="img"><img src="${imageUrl}" alt="${photoTitle}"></div>
                `;

                // Clicar na imagem abre o Lightbox
                item.querySelector('.img').addEventListener('click', () => {
                    openLightbox(imageUrl, photoTitle, descBase);
                });

                carousel.appendChild(item);

                if (index === files.length - 1) {
                    carousel.scrollTo({
                        left: carousel.scrollWidth,
                        behavior: 'smooth'
                    });
                }
            };

            reader.readAsDataURL(file);
        });

        titleInput.value = '';
        descInput.value = '';
        fileInput.value = '';
    }
}

// ================= REMOVER FOTO =================
function deletePhoto(button) {
    const item = button.closest('.carousel-item');
    if (item) {
        item.remove();
    }
}

// ================= MODAL DE EDIÇÃO =================
let currentEditItem = null;

function editPhoto(button) {
    currentEditItem = button.closest('.carousel-item');
    const h2 = currentEditItem.querySelector('h2');
    const p = currentEditItem.querySelector('p');

    const editModal = document.getElementById('editModal');
    const editTitleInput = document.getElementById('editTitleInput');
    const editDescInput = document.getElementById('editDescInput');

    if (editModal && editTitleInput && editDescInput) {
        editTitleInput.value = h2.textContent;
        editDescInput.value = p.textContent;
        editModal.classList.add('active');
    }
}

function saveEdit(event) {
    event.preventDefault();
    if (currentEditItem) {
        const h2 = currentEditItem.querySelector('h2');
        const p = currentEditItem.querySelector('p');
        const editTitleInput = document.getElementById('editTitleInput');
        const editDescInput = document.getElementById('editDescInput');

        if (editTitleInput && editDescInput) {
            h2.textContent = editTitleInput.value;
            p.textContent = editDescInput.value;
        }
    }
    closeEditModal();
}

function closeEditModal(event) {
    const editModal = document.getElementById('editModal');
    if (!event || event.target === editModal || event.target.classList.contains('lightbox-close')) {
        if (editModal) {
            editModal.classList.remove('active');
        }
        currentEditItem = null;
    }
}

// ================= LIGHTBOX (AMPLIAR FOTO) =================
function openLightbox(imgSrc, title, desc) {
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxDesc = document.getElementById('lightboxDesc');

    if (lightboxModal && lightboxImg && lightboxTitle && lightboxDesc) {
        lightboxImg.src = imgSrc;
        lightboxTitle.textContent = title;
        lightboxDesc.textContent = desc;
        lightboxModal.classList.add('active');
    }
}

function closeLightbox(event) {
    const lightboxModal = document.getElementById('lightboxModal');
    if (!event || event.target === lightboxModal || event.target.classList.contains('lightbox-close')) {
        if (lightboxModal) {
            lightboxModal.classList.remove('active');
        }
    }
}

// ================= LIGHTBOX VÍDEO (AMPLIAR VÍDEO) =================
function openVideoModal(videoSrc, title, desc) {
    const videoModal = document.getElementById('videoModal');
    const modalVideoPlayer = document.getElementById('modalVideoPlayer');
    const modalVideoSource = document.getElementById('modalVideoSource');
    const modalVideoTitle = document.getElementById('modalVideoTitle');
    const modalVideoDesc = document.getElementById('modalVideoDesc');

    if (videoModal && modalVideoPlayer && modalVideoSource && modalVideoTitle && modalVideoDesc) {
        modalVideoSource.src = videoSrc;
        modalVideoPlayer.load();
        modalVideoTitle.textContent = title;
        modalVideoDesc.textContent = desc;
        videoModal.classList.add('active');
        modalVideoPlayer.play();
    }
}

function closeVideoModal(event) {
    const videoModal = document.getElementById('videoModal');
    const modalVideoPlayer = document.getElementById('modalVideoPlayer');
    if (!event || event.target === videoModal || event.target.classList.contains('lightbox-close')) {
        if (videoModal) {
            videoModal.classList.remove('active');
            if (modalVideoPlayer) {
                modalVideoPlayer.pause();
            }
        }
    }
}

// Atribuir evento de clique aos itens de foto ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.carousel-item');
    items.forEach(item => {
        const imgTag = item.querySelector('img');
        const imgContainer = item.querySelector('.img');
        if (imgContainer && imgTag) {
            imgContainer.addEventListener('click', () => {
                const imgSrc = imgTag.src;
                const title = item.querySelector('h2').textContent;
                const desc = item.querySelector('p').textContent;
                openLightbox(imgSrc, title, desc);
            });
        }
    });
});
