//Before beginning any process, I invoke the event DOMContentLoaded and I verify that the DOM is charged.
document.addEventListener("DOMContentLoaded", () => {

  //I get the element in the html and save in the variables
  const modal = document.getElementById("modal");
  const modalBody = document.getElementById("modal-body");
  const closeButton = document.getElementById("close-button");

  //I called the event of button that contains the btn-detail class; later, get the attribute data-url
  document.querySelectorAll(".btn-detail").forEach((button) => {
    button.addEventListener("click", () => {
      // I save  the parameter sent to URL variable, and this I pass as a parameter to request "Fetch." Then, in the response, convert the HTML into plan text; later, this text is inserted in the modal DIV. In the end, add "display: flex" style to the modal class.
      const url = button.getAttribute("data-url");
      fetch(url)
        .then((response) => response.text())
        .then((html) => {
          modalBody.innerHTML = html;
          modal.style.display = "flex";
        });
    });
  });

  //I listen the closeButton events; when i push the button; I add the "display:flex" to the modal DIV
  closeButton.addEventListener("click", () => {
    modal.style.display = "none";
  });

});
