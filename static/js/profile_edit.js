const uploadPhoto = document.getElementById("upload_new_photo");
const firstName = document.getElementById("first_name")
const lastName = document.getElementById("last_name")
const email = document.getElementById("email")
const aboutMe = document.getElementById("about_me")
const submitEdit = document.getElementById("submit_edit")
const cancel = document.getElementById("cancel")

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');


submitEdit.addEventListener("click", async () => {
    let formData = new FormData();
    formData.append("first_name", document.getElementById("first_name").value);
    formData.append("last_name", document.getElementById("last_name").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("about_me", document.getElementById("about_me").value);
    await fetch("/user/{{ user.username }}/update", {
        method: "POST",
        body: formData,
        headers: {"X-CSRFToken": csrftoken},
        credentials: 'same-origin'
    });
    location.reload()
})


const editButton = document.getElementById("edit");
editButton.addEventListener("click", async () => {
    uploadPhoto.hidden = false;
    firstName.disabled = false;
    lastName.disabled = false;
    email.disabled = false;
    aboutMe.disabled = false;
    editButton.hidden = true;
    submitEdit.hidden = false;
    cancel.hidden = false;
})

const cancelButton = document.getElementById("cancelbutton")
cancelButton.addEventListener("click", async () =>
    location.reload())