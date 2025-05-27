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
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      };

      try {
        response = await fetch(url, options);
        window.location.reload();

      } catch (error) {
        window.location.reload();

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