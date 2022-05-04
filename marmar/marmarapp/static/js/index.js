let activeZone = window.innerHeight / 2

window.addEventListener('scroll', e => {
    let why = document.querySelectorAll('.why>div')

    why.forEach((el, index) => {
        if (el.getBoundingClientRect().top < activeZone) {
            el.classList.add('active')

            if (why[index-1]) {
                why[index-1].classList.remove('active')
            }

            if (why[index+1]) {
                why[index+1].classList.remove('active')
            }
        }
    })
})


/* Устанавливаем индекс слайда по умолчанию */
let slideIndex = 1;
showSlides(slideIndex);

/* Увеличиваем индекс на 1 — показываем следующий слайд*/
function nextSlide() {
    showSlides(slideIndex += 1);
}

/* Уменьшает индекс на 1 — показываем предыдущий слайд*/
function previousSlide() {
    showSlides(slideIndex -= 1);
}

/* Устанавливаем текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Функция перелистывания */
function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("item");

    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }

    /* Проходим по каждому слайду в цикле for */
    for (let slide of slides) {
        slide.style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}



const slider = document.querySelector('.gallery');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', e => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener('mouseleave', _ => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mouseup', _ => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mousemove', e => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const SCROLL_SPEED = 3;
  const walk = (x - startX) * SCROLL_SPEED;
  slider.scrollLeft = scrollLeft - walk;
});

document.querySelector('.controls-slider.left').addEventListener('click', () => slide(-100))
document.querySelector('.controls-slider.right').addEventListener('click', () => slide(100))

function slide (pxs) {
  scrollLeft = slider.scrollLeft
  slider.scrollLeft = scrollLeft + pxs
}