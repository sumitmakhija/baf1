/*****************************************************************
year set on footer to update automatically
*****************************************************************/
$(document).ready(function () {
  const currentYear = new Date().getFullYear();
  $("#footer-year").text(currentYear);
  console.log(currentYear); // Outputs: 2024 (or the current year)
});

/*****************************************************************
swiper initialize
*****************************************************************/
var heroHomeSwiper = new Swiper(".heroHomeSwiper", {
  grabCursor: true,
  loop: false,
  //   autoplay: {
  //     delay: 5000,
  //   },
  pagination: {
    el: ".heroHomeSwiper-pagination",
    clickable: true,
  },
});
var solutionsSlider = new Swiper(".solutionsSlider", {
  grabCursor: true,
  loop: false,
  slidesPerView: 3.5,
  spaceBetween: 30,
  pagination: {
    el: ".solutionsSlider-pagination",
    clickable: true,
  },
  breakpoints: {
    // When the viewport width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    // When the viewport width is >= 768px
    768: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
    // When the viewport width is >= 1024px
    1024: {
      slidesPerView: 3.5,
      spaceBetween: 30,
    },
  },
});

var newsSlider = new Swiper(".newsSlider", {
  grabCursor: true,
  loop: false,
  slidesPerView: 3.5,
  spaceBetween: 30,
  //   autoplay: {
  //     delay: 5000,
  //   },
  pagination: {
    el: ".newsSlider-pagination",
    clickable: true,
  },
  breakpoints: {
    // When the viewport width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    // When the viewport width is >= 768px
    768: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
    // When the viewport width is >= 1024px
    1024: {
      slidesPerView: 3.5,
      spaceBetween: 30,
    },
  },
});
var offersSlider = new Swiper(".offersSlider", {
  grabCursor: true,
  loop: false,
  slidesPerView: 2.5,
  spaceBetween: 30,
  //   autoplay: {
  //     delay: 5000,
  //   },
  scrollbar: {
    el: ".offersSlider-scrollbar",
    hide: false,
  },
  breakpoints: {
    // When the viewport width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    // When the viewport width is >= 768px
    768: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
    // When the viewport width is >= 1024px
    1024: {
      slidesPerView: 3.5,
      spaceBetween: 30,
    },
  },
});

var seniorsSlider = new Swiper(".seniorsSlider", {
  grabCursor: true,
  loop: false,
  slidesPerView: 1.5,
  spaceBetween: 10,
  //   autoplay: {
  //     delay: 5000,
  //   },

  breakpoints: {
    // When the viewport width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 480px
    480: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 768px
    768: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 1024px
    1024: {
      slidesPerView: 1.3,
      spaceBetween: 10,
    },
  },
});

var applysSlider = new Swiper(".applysSlider", {
  grabCursor: true,
  loop: false,
  slidesPerView: 3.7,
  spaceBetween: 20,
  pagination: {
    el: ".solutionsSlider-pagination",
    clickable: true,
  },
  breakpoints: {
    // When the viewport width is >= 320px
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    // When the viewport width is >= 480px
    480: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    // When the viewport width is >= 768px
    768: {
      slidesPerView: 2,
      spaceBetween: 30,
    },
    // When the viewport width is >= 1024px
    1024: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
  },
});

/**
 * financial reports page scrollbar invert
 * */

const scrollContainer = $(".scroll-container");
// console.log(scrollContainer);
scrollContainer.on("wheel", function (evt) {
  evt.preventDefault();
  $(this).scrollLeft($(this).scrollLeft() + evt.originalEvent.deltaY);

  // console.log($(this).scrollLeft());
});

// document.addEventListener("DOMContentLoaded", function () {
//   var triggerTabList = [].slice.call(document.querySelectorAll('[data-mdb-tab-init]'))
//   triggerTabList.forEach(function (triggerEl) {
//     var tabTrigger = new mdb.Tab(triggerEl)
//     triggerEl.addEventListener('click', function (event) {
//       event.preventDefault()
//       tabTrigger.show()
//     })
//   })
// });
// document.addEventListener("DOMContentLoaded", () => {
//   const bgContainers = document.querySelectorAll(".cta-bgImage");
//   bgContainers.forEach(container => {
//     const bgImage = container.getAttribute("data-bg");
//     if (bgImage) {
//       container.style.backgroundImage = `url('${bgImage}')`;
//       container.style.backgroundSize = "cover";
//       container.style.backgroundPosition = "center";
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll("[data-bg]");

  elements.forEach((element) => {
    const bgImage = element.getAttribute("data-bg");

    if (bgImage) {
      element.style.setProperty("--bg-image", `url('${bgImage}')`);
    }
  });
});