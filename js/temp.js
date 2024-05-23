const host = "http://127.0.0.1.:8080";
axios.get(`${host}/temp`).then((response) => {});

function AddMessage() {
  const name = document.getElementById("name").value;
  const message = document.getElementById("message").value;
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementByIDv("guestbook_form");
  const message = document.getElementById("messages");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    AddMessage();
  });
});
