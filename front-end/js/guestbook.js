//const host = "http://127.0.0.1:8080";
const host = "http://54.81.196.162:8080";
const ContainGuestbook = document.querySelector(`.Contain-Guestbook`);

function Guestbook() {
  axios
    .get(`${host}/guestbook`)
    .then((response) => {
      console.log(response.data);
      ShowGuestbook(response.data);
    })
    .catch((error) => {
      console.error(
        "Error fetching guestbook:",
        error.response ? error.response.data : error.message
      );
    });
}

function ShowGuestbook(messages) {
  const messageContainer = document.getElementById("messages");
  messageContainer.innerHTML = "";
  messages.forEach((msg) => {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");

    const nameElement = document.createElement("div");
    nameElement.textContent = msg.name;

    const contentElement = document.createElement("div");
    contentElement.textContent = msg.message;

    const timeElement = document.createElement("div");
    try {
      timeElement.textContent = new Date(msg.timestamp).toLocaleString();
    } catch (e) {
      console.error("Invalid time value:", msg.timestamp);
      timeElement.textContent = "Invalid date";
    }
    //timeElement.textContent = new Date(msg.timestamp).toLocaleString();
    //###살려!  timeElement.textContent = new Date(msg.timestamp).toISOString();

    //const currentTime = new Date();
    //const timeElement = currentTime.toLocaleString(); // 현재 시간을 문자열로 포맷팅

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "삭제";
    /*
    if (msg.id !== undefined) {
      deleteButton.onclick = () => DeleteMessage(msg.id);
    } else {
      console.error("Invalid message ID", msg.id);
    }
    */
    deleteButton.onclick = () => DeleteMessage(msg.id);

    messageElement.appendChild(nameElement);
    messageElement.appendChild(contentElement);
    messageElement.appendChild(timeElement);
    messageElement.appendChild(deleteButton);

    messageContainer.appendChild(messageElement);
  });
}

function AddMessage() {
  const name = document.getElementById("name").value;
  const message = document.getElementById("message").value;

  if (name && message) {
    axios
      .post(`${host}/guestbook`, { name, message })
      .then(() => {
        Guestbook();
        document.getElementById("name").value = "";
        document.getElementById("message").value = "";
      })
      .catch((error) => {
        //console.error("Error adding message:");
        console.error("Error adding message:");
      });
  }
}
/*
function DeleteMessage(id) {
  axios
    .delete(`${host}/guestbook/${id}`)
    .then(() => {
      Guestbook();
    })
    .catch((error) => {
      console.error(
        "Error deleting message:",
        error.response ? error.response.data : error.message
      );
    });
}*/

function DeleteMessage(id) {
  if (id !== undefined) {
    axios
      .delete(`${host}/guestbook/${id}`)
      .then(() => {
        Guestbook();
      })
      .catch((error) => {
        console.error("Error deleting message:");
      });
  } else {
    console.error("Invalid message ID", id);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("guestbook_form");
  const messageContainer = document.getElementById("messages");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    AddMessage();
  });
});

window.addEventListener("DOMContentLoaded", function () {
  Guestbook();
});
