var detailsElements = document.querySelectorAll('details');

detailsElements.forEach(details => {
  details.addEventListener('click', () => {
    detailsElements.forEach(otherDetail => {
      if (otherDetail !== details && otherDetail.hasAttribute('open')) {
        otherDetail.removeAttribute('open');
      }
    });
  });
});

// Add an event listener for the 'loadeddata' event

var submitForm = document.getElementById("contact_us_form");
var submitButton = document.getElementById("submitBtn");

// submitButton.addEventListener("click", () => {
//   submitForm.submit();
// })

if (submitForm){
  // submitForm.addEventListener('submit', async (event) => {
  //   event.preventDefault();
  submitButton.addEventListener("click", async function(event) {
    event.preventDefault(); 
    console.log("qweqwe");

    const nameInput = document.getElementById("full_name_input");
    const emailInput = document.getElementById("email_input");
    const phoneInput = document.getElementById("phone_input");
    const companyInput = document.getElementById("company_input");
    const subjectInput = document.getElementById("subject_input");
    const msgInput = document.getElementById("msg_input");

    const nameValue = nameInput.value.trim();
    const emailValue = emailInput.value.trim();
    const phoneValue = phoneInput.value.trim();
    const companyValue = companyInput.value.trim();
    const subjectValue = subjectInput.value.trim();
    const msgValue = msgInput.value.trim();

    if (nameValue === "") {
      alert("Please enter your name!");
    } else if (emailValue === "") {
      alert("Please enter your Email!");
    } else if (phoneValue === "") {
      alert("Please enter your Phone NO.!");
    } else if (subjectValue === "") {
      alert("Please enter your Subject!");
    } else if (msgValue === "") {
      alert("Please enter your Message!");
    } else {
      // alert("Submitted Successfully!");
      const url = '/demo_msg_save';
      const body = {
        "site_name" : window.location.href,
        "full_name" : nameValue,
        "email" : emailValue,
        "phone_no" : phoneValue,
        "company_name" : companyValue,
        "subject" : subjectValue,
        "message" : msgValue
      }

      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', // Adjust content type if your API expects something different
        },
        body: JSON.stringify(body),
      };

      // fetch(url, options)
      // window.location.reload();
      try {
        response = await fetch(url, options);
        window.location.reload();

        // const result = await response.json();
        // console.log(result); // Handle successful response (data or message)
    
        // Display success message or redirect the page based on your preference
        // var popup = document.getElementById('messagePopup');
        // if (popup) {
        //   popup.classList.add('show');
        //   popup.innerText = "Demo request submitted successfully!"
        //   setTimeout(function() {
        //       popup.classList.remove('show');
        //   }, 3000);
        // }
      } catch (error) {
        window.location.reload();
        // var popup = document.getElementById('messagePopup');
        // if (popup) {
        //   popup.innerText = "Error submitting Demo request!"
        //   popup.style.color = 'red';
        //   popup.classList.add('show');
        //   setTimeout(function() {
        //       popup.classList.remove('show');
        //   }, 3000);
        // }
      }
  }
});
}

var callBtn = document.getElementById("callbtn");

if(callBtn){
callBtn.addEventListener("click", function() {
  const text = '+91 81188 66530'; // Get text content to copy

  navigator.clipboard.writeText(text)
    .then(() => {
      alert(text + " copied to clipboard!");
    })
    .catch(err => {
      alert("Failed to copy text: " + err);
    });
});
}

var mailBtn = document.getElementById("mailbtn");

if(mailBtn){
mailBtn.addEventListener("click", function() {
  const text = 'support@doctunes.io'; // Get text content to copy

  navigator.clipboard.writeText(text)
    .then(() => {
      alert(text + " copied to clipboard!");
    })
    .catch(err => {
      alert("Failed to copy text: " + err);
    });
});
}

function onScreenTypewrite() {
  var on_screen_typewrite = document.querySelectorAll(".onscreentypewrite");

  for (var i = 0; i < on_screen_typewrite.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = on_screen_typewrite[i].getBoundingClientRect().top;
    var elementVisible = 100;

    if (elementTop < windowHeight - elementVisible) {
      on_screen_typewrite[i].classList.remove("onscreentypewrite")
      textAnimation(on_screen_typewrite[i].id)
    }
  }
}

function navWidthChange(){
  var navBar = document.querySelector("#id-5564");
  currentHeigth = window.scrollY;
  if(currentHeigth > 500){
    navBar.style.width = '35rem';
  } else {
    navBar.style.width = '25rem';
  }
}

window.addEventListener("scroll", function(){
  // navWidthChange();
  onScreenTypewrite();
});


let customers_card_1_text = document.getElementById("customers-card-1");
let customers_card_2_text = document.getElementById("customers-card-2");
let customers_card_3_text = document.getElementById("customers-card-3");

let customers_card_state_1 = document.getElementById("customers-card-state-1");
let customers_card_state_2 = document.getElementById("customers-card-state-2");
let customers_card_state_3 = document.getElementById("customers-card-state-3");

let customers_card_name_1 = document.getElementById("customers-card-name-1");
let customers_card_name_2 = document.getElementById("customers-card-name-2");
let customers_card_name_3 = document.getElementById("customers-card-name-3");

let customers_card_img_1 = document.getElementById("id-bg-69272");
let customers_card_img_2 = document.getElementById("id-bg-69276");
let customers_card_img_3 = document.getElementById("id-bg-69280");

function change_text_next(){
  [customers_card_1_text.innerText,customers_card_2_text.innerText,customers_card_3_text.innerText] = [customers_card_3_text.innerText,customers_card_1_text.innerText,customers_card_2_text.innerText];

  [customers_card_state_1.innerText,customers_card_state_2.innerText,customers_card_state_3.innerText] = [customers_card_state_3.innerText,customers_card_state_1.innerText,customers_card_state_2.innerText];

  [customers_card_name_1.innerText,customers_card_name_2.innerText,customers_card_name_3.innerText] = [customers_card_name_3.innerText,customers_card_name_1.innerText,customers_card_name_2.innerText];

  [customers_card_img_1.style.backgroundImage, customers_card_img_2.style.backgroundImage, customers_card_img_3.style.backgroundImage] = [customers_card_img_3.style.backgroundImage, customers_card_img_1.style.backgroundImage, customers_card_img_2.style.backgroundImage];
}
 
function change_text_prev(){
  [customers_card_1_text.innerText,customers_card_2_text.innerText,customers_card_3_text.innerText] = [customers_card_2_text.innerText,customers_card_3_text.innerText,customers_card_1_text.innerText];

  [customers_card_state_1.innerText,customers_card_state_2.innerText,customers_card_state_3.innerText] = [customers_card_state_2.innerText,customers_card_state_3.innerText,customers_card_state_1.innerText];

  [customers_card_name_1.innerText,customers_card_name_2.innerText,customers_card_name_3.innerText] = [customers_card_name_2.innerText,customers_card_name_3.innerText,customers_card_name_1.innerText];

  [customers_card_img_1.style.backgroundImage, customers_card_img_2.style.backgroundImage, customers_card_img_3.style.backgroundImage] = [customers_card_img_2.style.backgroundImage, customers_card_img_3.style.backgroundImage, customers_card_img_1.style.backgroundImage];
}