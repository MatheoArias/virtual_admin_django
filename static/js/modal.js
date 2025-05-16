//Before beginning any process, I invoke the event DOMContentLoaded and I verify that the DOM is charged.
document.addEventListener("unicorn:updated", () => {
  //I get the element in the html and save in the variables
  const modal = document.getElementById("modal-detail");
  const buttonClose = document.querySelectorAll(".btn-close");
  const buttonDetail = document.querySelectorAll(".btn-detail");

  if (modal) {
    buttonDetail.forEach((button) => {
      button.addEventListener("click", () => {
        modal.style.display = "block";
      });
    });

    buttonClose.forEach(item => {
      item.addEventListener("click", () => {
        modal.style.display = "none";
        console.log("closeButton clicked");
      });
    });
  }else{
    console.warn("Modal with ID 'modal-detail' not found in the DOM.");
  }
});
