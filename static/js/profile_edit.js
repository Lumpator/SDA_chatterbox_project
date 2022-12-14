const uploadPhoto = document.getElementById("upload_new_photo");
const firstName = document.getElementById("first_name")
const lastName = document.getElementById("last_name")
const email = document.getElementById("email")
const aboutMe = document.getElementById("about_me")
const submitEdit = document.getElementById("submit_edit")
const cancel = document.getElementById("cancel")
const uploadPhotoSubmit = document.getElementById("upload_photo_submit")

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
    uploadPhotoSubmit.hidden = false;
})

const cancelButton = document.getElementById("cancelbutton")
cancelButton.addEventListener("click", async () =>
    location.reload())