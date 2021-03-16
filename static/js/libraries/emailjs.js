function sendEmail(contactForm) {
   // console.log("this is what I get from the form ",contactForm);
     emailjs.send("service_65vy6qi", "holiday", 
     {"from_name":contactForm.first_name.value,
         "last_name":contactForm.last_name.value,
        "from_email":contactForm.email.value,
        "message":contactForm.message.value
    })
    .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
    }, function(error) {
       console.log('FAILED...', error);
    });
}